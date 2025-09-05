# learning rate.md — simple, one-file guide (GitHub-friendly)

## 1) What is the learning rate (η)
- It is the step size in weight updates: `w := w − η * gradient`.
- Too small → slow learning. Too large → loss explodes or bounces.

## 2) Quick signs
- **Too high**: loss spikes/NaN, accuracy stuck near chance, gradients very large, training unstable run-to-run.
- **Too low**: loss goes down very slowly, many epochs needed, plateaus early.
- **A bit high** (common): train loss falls then rises; val loss noisy; weights/activations show big jumps.

## 3) Good starting points (pick closest row, then tune)
| Scenario | Optimizer | Start η (batch≈32–64 unless noted) | Weight decay (wd) | Notes |
|---|---|---:|---:|---|
| CNN from scratch (images) | SGD+momentum(0.9) | 0.1 at batch 256 (scale linearly) | 1e-4 | Warmup 5 epochs, cosine decay 100–300 epochs |
| Small/medium CNN | AdamW | 1e-3 | 1e-4 | If overfit, raise wd; if slow, try 3e-3 |
| Transformers (NLP/ViT) | AdamW (β=(0.9,0.999), ε=1e-8) | 3e-4 | 0.01 | Linear warmup 5% steps, cosine decay |
| Fine-tune Transformer (full) | AdamW | 1e-5–1e-4 | 0.01 | Smaller data → smaller η (e.g., 1e-5) |
| Fine-tune with adapters/LoRA | AdamW | 1e-4–1e-3 | 0.01 | Often 2e-4–5e-4 works well |
| Linear probe (freeze body, train head) | SGD or AdamW | 1e-2 (SGD) or 3e-3 (AdamW) | 1e-4 | Reduce η if head overfits fast |
| RNN/LSTM | Adam | 1e-3 | 0–1e-4 | Use grad clipping (e.g., norm 1.0) |
| GAN (generator/disc) | Adam(β=(0.5,0.999)) | 2e-4 | 0 | Keep G and D η equal; tune stability |

**Linear batch scaling rule (first try)**: `η_new = η_ref * (batch_new / batch_ref)`. If unstable, scale less aggressively.

## 4) Warmup (helps stability at start)
- **Linear warmup** for `T_warm` steps: `η_t = η_target * t / T_warm` (for `t=1..T_warm`), then follow your decay.
- Typical: 1–5% of total steps (Transformers), or 1–5 epochs (vision).
- If you see early spikes/divergence, increase warmup length.

## 5) Schedules (decay plans)
| Schedule | Formula (after warmup) | Knobs to set | Use when | Notes |
|---|---|---|---|---|
| Constant | `η_t = η0` | `η0` | Small tasks, quick tests | Simple, but often suboptimal |
| Step | `η_t = η0 * γ^(⌊t/s⌋)` | step `s`, factor `γ` (e.g., 0.1) | Classic CNNs | Big drops at milestones |
| Exponential | `η_t = η0 * exp(−k t)` | rate `k` | General | Smooth version of step |
| Cosine | `η_t = η_min + 0.5(η_max−η_min)(1+cos(π t/T))` | `η_max`, `η_min≈0`, `T` | Vision, Transformers | Works well; pair with warmup |
| Cosine restarts | Cosine on cycles | cycle length | Escaping plateaus | Good if training very long |
| Cyclical LR (triangular) | Up/down between `η_low, η_high` | bounds, cycle len | Small data, SGD | Acts like built-in exploration |
| OneCycle | Warmup to `η_high`, then cosine down below start | `η_high`, total steps | Many tasks | Very effective with SGD/AdamW |
| Polynomial | `η_t = η0*(1−t/T)^p` | power `p` | Segmentation | Widely used in semantic seg |

**Practical picks**:  
- Vision/Transformers: **Warmup + Cosine** (simple, strong).  
- SGD on images: **OneCycle** (fast, stable).  
- Old-style ResNets: **Step** at epoch 30/60/90 (γ=0.1).

## 6) LR range test (fast way to pick η)
1) Start from very small `η_start` (e.g., 1e−7).  
2) Increase η each mini-batch by a constant multiplicative factor until `η_end` (e.g., 10).  
3) Record loss; plot loss vs η (log scale).  
4) Choose η where loss first drops steeply; set max η near where loss starts to blow up.  
**Defaults**: run for ~100–200 steps, pick `η_base` ≈ 0.1–0.3 of the max-stable η.

## 7) How to tune (short workflow)
1) Pick optimizer + schedule (e.g., AdamW + warmup+cosine).  
2) Do LR range test → pick `η_base`.  
3) Set warmup: 1–5% steps; choose total steps/epochs.  
4) Train for a few epochs; watch train/val loss curves.  
5) If unstable → lower `η_base` or lengthen warmup; add grad clipping.  
6) If too slow → raise `η_base` a bit or shorten decay; check weight decay is not too high.  
7) Lock LR, then tune other knobs (batch size, wd, augmentation).

## 8) Safety knobs that interact with LR
- **Gradient clipping** (by global norm): e.g., clip to 1.0 or 0.5 (RNNs, Transformers, GANs).  
- **Weight decay**: too high wd looks like η too low; too low wd can overfit even with good η.  
- **Mixed precision**: use appropriate loss scaling; if NaNs → lower η or increase warmup/clipping.  
- **Norm layers**: with BatchNorm, larger η is often OK; with Group/LayerNorm, tune η normally.

## 9) Per-layer LR (optional, advanced)
- **Layer-wise decay** (Transformers): smaller η for early layers, larger for later (e.g., decay factor 0.9 per layer).  
- **Heads vs body**: fine-tuning often uses bigger η for the new head and smaller for the pre-trained body (e.g., 10× head LR).

## 10) Typical “good” numbers (quick memory)
- AdamW: `3e-4` pretrain, `1e-5–1e-4` fine-tune, wd `0.01`.  
- SGD+mom on images: `0.1` at batch 256 (scale with batch), wd `1e-4`.  
- OneCycle (AdamW/SGD): `η_high` ≈ 5–10× `η_base`, total steps = all train steps.  
- Warmup length: 1–5% of total steps (NLP), 1–5 epochs (vision).  
- Cosine `η_min`: 0 or `η_base/100`.

## 11) Debug table (symptom → action)
| Symptom | Likely cause | Fix |
|---|---|---|
| Loss diverges/NaN | η too high, no warmup, no clipping | Lower η, add/lengthen warmup, add grad clipping, check data/NaNs |
| Loss zig-zags, no clear downtrend | η a bit high | Reduce η 2×, or use cosine/OneCycle |
| Loss very slow | η too low, wd too high | Raise η 2–3×, or lower wd; consider OneCycle |
| Train ↓, Val ↑ (early) | Overfitting or noisy LR | Try smaller η and/or more decay/aug; use cosine; early stop |
| Big run-to-run variance | LR or batch too aggressive | Lower η, increase batch or clipping, fix seeds |

## 12) Simple math (for reference)
- Update step: `w := w − η * g`.  
- Momentum (v): `v := μ v + g ; w := w − η v`.  
- AdamW (simplified): `m := β1 m + (1−β1) g ; v := β2 v + (1−β2) g² ; m̂ := m/(1−β1^t) ; v̂ := v/(1−β2^t) ; w := w − η * m̂/(sqrt(v̂)+ε) − η*wd*w`.

## 13) Mini recipes
- **Image classifier (from scratch, SGD)**: η=0.1 @256 batch (scale with batch), mom=0.9, wd=1e-4, warmup 5 epochs, cosine to 0, 200 epochs, optional label smoothing.  
- **Transformer fine-tune (AdamW)**: η=2e-5 (small data) or 5e-5 (more data), wd=0.01, warmup 5%, cosine decay, clip grad norm 1.0.  
- **Linear probe on frozen backbone**: η=1e-2 (SGD) or 3e-3 (AdamW), cosine 50–100 epochs, wd=1e-4.

## 14) Checklist (before training)
- [ ] Pick optimizer (SGD+mom / AdamW).  
- [ ] Choose schedule (warmup + cosine / OneCycle).  
- [ ] Decide epochs/steps and warmup length.  
- [ ] Run LR range test → set `η_base`.  
- [ ] Set grad clipping (esp. RNN/Transformer/GAN).  
- [ ] Verify mixed precision/loss scaling if used.  
- [ ] Log LR over time and loss/metrics.

## 15) One-screen memory
- Tune η first (LR range test).  
- Warmup a little, then decay (cosine or OneCycle).  
- Scale η with batch (then check stability).  
- Clip grads if unstable.  
- Fine-tune with smaller η; adapters with larger η.  
- If in doubt: AdamW `3e-4` (pretrain) or `1e-5–1e-4` (fine-tune) + warmup+cosine.