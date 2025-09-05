# normalization

Goal: keep activations and gradients in a good range so training is stable and fast.

---

## 1) Core idea (short)
For some values `x`:
- Mean: `μ = mean(x)`
- Var: `σ² = var(x)`
- Normalize: `x_hat = (x − μ) / sqrt(σ² + ε)`
- Affine: `y = γ * x_hat + β` (learned `γ` scale, `β` shift; start `γ=1, β=0`)
- `ε` avoids divide-by-zero (use `1e-5` or `1e-6`)

---

## 2) Train vs Inference
- Train: use batch/group/layer stats from the current mini-batch.
- Inference: BatchNorm uses saved running stats; LayerNorm/GroupNorm recompute per sample.
- Always set correct mode: `train()` for training, `eval()` for inference.

---

## 3) Where to place it
- Typical order: Layer (Conv/Linear) → Norm → Activation (e.g., ReLU).
- Residual blocks: Conv → Norm → ReLU, then add skip.
- Transformers: Pre-LN (Norm before attention/MLP) is standard.

---

## 4) Main variants at a glance

| Norm type | What it averages over | Best for | Batch-size need | Running stats | Learnable γ,β | Notes |
|---|---|---|---|---|---|---|
| BatchNorm (BN) | Over batch and spatial per channel | CNNs | Likes larger batches (≥16) | Yes | Yes | Use SyncBN for multi-GPU small per-GPU batches |
| SyncBatchNorm | Same as BN but synced across GPUs | Multi-GPU CNNs | Any per-GPU; sync helps | Yes | Yes | Reduces noisy stats when per-GPU batch is small |
| GroupNorm (GN) | Groups of channels per sample | CNNs with small batch | Any | No | Yes | Pick groups so each group has ~8–32 channels (e.g., 32 groups) |
| InstanceNorm (IN) | Spatial per sample+channel | Style transfer, image gen | Any | No | Yes | Removes instance contrast/style |
| LayerNorm (LN) | All features of a single sample | NLP, Transformers, RNNs | Any | No | Yes | Stable with small batch |
| RMSNorm | Like LN but uses RMS only | Large language models | Any | No | γ only (β often omitted) | Cheaper than LN; no mean subtraction |
| WeightNorm | Reparameterize weights, not data | General use | Any | No | g param | `W = g * v / ||v||`; speeds/steadies training |
| SpectralNorm | Constrain largest singular value | GANs (disc), stability | Any | No | No | Regularizer; controls Lipschitz constant |

---

## 5) Quick picks
- CNN with decent batch: BatchNorm.
- CNN with tiny batch (≤8): GroupNorm (or InstanceNorm for style tasks).
- Transformers / NLP / RNNs: LayerNorm (or RMSNorm for big LMs).
- GAN discriminator: SpectralNorm (plus GN/IN as needed).
- Multi-GPU with small per-GPU batch: SyncBatchNorm or switch to GroupNorm.

---

## 6) Good defaults
- ε: `1e-5` (BN/LN), `1e-6` (many Transformer configs).
- BN momentum (running stats): `0.1` (PyTorch default). Lower (e.g., `0.01`) = smoother but slower to adapt.
- GroupNorm groups: `32` groups, or choose so each group has 8–32 channels.
- Init: `γ=1`, `β=0`. In deep residual blocks, set the **last norm’s** `γ=0` to start as identity (helps very deep nets).
- Weight decay: often exclude `γ, β` from weight decay (safe default).

---

## 7) BatchNorm details
Per channel `c` in CNNs:
- Training stats: `μ_c = mean over (N,H,W)`, `σ²_c = var over (N,H,W)`.
- Normalize: `y_c = γ_c * (x_c − μ_c) / sqrt(σ²_c + ε) + β_c`.
- Update running stats:  
  `running_mean = (1−m)*running_mean + m*μ_batch`,  
  `running_var  = (1−m)*running_var  + m*σ²_batch`.
- Inference: use `running_mean`, `running_var`.
- Small-batch issues: stats are noisy → accuracy drops. Use SyncBN, GroupNorm, or “Ghost BN” (compute BN over virtual sub-batches).

---

## 8) LayerNorm vs RMSNorm (Transformers)
- LayerNorm per sample across features: `y = γ * (x − μ) / sqrt(σ² + ε) + β`.
- RMSNorm per sample RMS only: `r = sqrt(mean(x²) + ε)`, `y = γ * x / r` (β often skipped).
- LN is robust; RMSNorm is leaner (used in many LLMs).

---

## 9) GroupNorm and InstanceNorm (small-batch CNNs)
- GroupNorm: split channels into G groups per sample; normalize within each group. Works well when BN is unstable (tiny batch).
- InstanceNorm: normalize each channel per sample across spatial; common in style transfer to remove instance-specific contrast.

---

## 10) Optimizer and LR notes
- Norm layers often allow slightly larger learning rates than raw nets; still tune LR.
- If using weight decay, consider excluding `γ, β`.
- Mixed precision: keep ε not too tiny to avoid underflow.

---

## 11) Multi-GPU and accumulation
- SyncBatchNorm synchronizes batch stats across devices; helps when per-GPU batch is small.
- Gradient accumulation by itself does not fix BN noise; prefer SyncBN or GN.

---

## 12) Common pitfalls → fixes
- Wrong mode at eval (BN in train mode): predictions degrade → call `eval()`.
- Too small batch with BN: unstable stats → use SyncBN or GroupNorm.
- ε too small: NaNs → use `1e-5` or `1e-6`.
- BN momentum too low for fast data shifts: slow adaptation → increase momentum `m`.
- Deep residuals explode early: set last norm `γ=0` inside each residual block.
- Old post-LN Transformer blocks unstable: use Pre-LN (norm before sublayers).

---

## 13) Mini recipes
- CNN big batch: Conv → BN → ReLU. ε=`1e-5`, momentum=`0.1`. LR tune normally.
- CNN tiny batch: Conv → GN(32) → ReLU. No running stats. Batch size independent.
- Transformer block: Pre-LN (LN or RMSNorm) before attention and MLP. ε=`1e-5` or `1e-6`. Consider excluding norms from weight decay.
- GAN D: add SpectralNorm to conv/linear; consider IN/GN in G.

---

## 14) One-screen summary
- Pick by model and batch size: BN (big-batch CNN), GN/IN (small-batch CNN), LN/RMSNorm (Transformers/RNNs).
- Use order Layer → Norm → Activation.
- Defaults: ε≈`1e-5`, BN momentum≈`0.1`, GN groups≈`32`, init `γ=1, β=0` (residual last norm `γ=0`).
- Ensure correct train/eval modes, use SyncBN for multi-GPU small batches, and consider excluding `γ, β` from weight decay.