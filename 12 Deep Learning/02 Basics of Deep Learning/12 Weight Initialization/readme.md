# Weight Initialization — Simple, One-File Guide (Weight Initialization.md)

Good init makes gradients and activations **not explode** and **not vanish**. It also **breaks symmetry** so units learn different things. Use the right rule for your activation and layer.

---

## 1) Problems init must avoid
- **Symmetry:** if all weights are the same, all neurons stay the same → no learning.
- **Vanishing:** tiny activations/gradients as depth grows → learning stalls.
- **Exploding:** huge activations/gradients → training blows up.

---

## 2) Key terms (short)
- `fan_in` = number of inputs to a neuron (for conv: `in_channels × kH × kW`).  
- `fan_out` = number of outputs from a neuron (for conv: `out_channels × kH × kW`).  
- **Gain (`g`)** = scale factor that depends on activation (e.g., ReLU gain ≈ √2).  
- **Uniform vs Normal:** if `Var(W) = v` then  
  • **Normal:** `W ~ N(0, v)` → `std = √v`  
  • **Uniform:** `W ~ U[−a, a]` with `a = √(3v)`

---

## 3) The three classic rules (core formulas)

| Name (use when) | Target variance | Normal std | Uniform limit `a` |
|---|---|---:|---:|
| **LeCun** (SELU, linear; keeps unit variance) | `v = 1 / fan_in` | `√(1 / fan_in)` | `√(3 / fan_in)` |
| **Xavier/Glorot** (tanh/sigmoid/softsign; keeps in↔out balance) | `v = 2 / (fan_in + fan_out)` | `√(2 / (fan_in + fan_out))` | `√(6 / (fan_in + fan_out))` |
| **He/Kaiming** (ReLU, ELU, Swish, GELU family) | `v = 2 / fan_in` | `√(2 / fan_in)` | `√(6 / fan_in)` |

> **Leaky ReLU (slope `a`)**: use **He** but with gain `g = √(2 / (1 + a²))`.  
> Effective variance: `v = g² / fan_in`.

---

## 4) Match activation → init (quick table)

| Last nonlinearity in the layer | Recommended init |
|---|---|
| **ReLU / GELU / ELU / Swish** | **He (Kaiming)** (normal or uniform). For leaky ReLU(α), use He with `g = √(2/(1+α²))`. |
| **tanh / sigmoid / softmax logits** | **Xavier (Glorot)** (prefer **uniform** for logits/linear heads). |
| **SELU (self-normalizing nets)** | **LeCun normal** (not He/Xavier). |
| **Linear (no activation)** | **LeCun** (conservative) or **Xavier** (balanced); pick based on fan usage. |
| **RNN with tanh** | Xavier for input weights; **orthogonal** for recurrent weights. |
| **RNN with ReLU** | He for input weights; **orthogonal** for recurrent weights. |

---

## 5) Bias, norm, and special layers

- **Biases:** start at **0** (safe default).  
  • LSTM/GRU: set **forget gate bias** to **1.0–2.0** (helps retain info).  
- **BatchNorm / LayerNorm:** `gamma = 1`, `beta = 0`.  
  • Deep residual nets: set **last BN gamma = 0** in each block to start as identity (stabilizes early training).  
- **Embeddings:** `std ≈ 1/√d` or `U[−1/√d, 1/√d]` (where `d` is embedding dim).  
- **Output heads:**  
  • Regression: small **Xavier/LeCun**; bias = target mean if known.  
  • Binary/multiclass logits: **Xavier uniform** is a strong default.

---

## 6) Convs and fans (how to count)
For conv weight of shape `[out_ch, in_ch, kH, kW]`:
- `fan_in = in_ch × kH × kW`  
- `fan_out = out_ch × kH × kW`  
Then plug into LeCun/Xavier/He formulas above.

---

## 7) Orthogonal, LSUV, and friends (when depth is large)
- **Orthogonal init:** make weight matrices orthonormal (`WᵀW=I`); good for **RNN recurrent** weights and deep linear/conv stacks (often with a **gain**: `g = √2` for ReLU).  
- **LSUV (Layer-Sequential Unit-Variance):** run 1–2 mini-batches and **rescale each layer** so output variance ≈ 1 before training; helps very deep nets.  
- **FixUp / scaled residuals (no norm nets):** initialize residual branches small and scale by depth so signals stay stable.

---

## 8) Tiny “how to pick” recipe

1) **Choose activation** per layer.  
2) **Compute `fan_in`/`fan_out`.**  
3) **Pick rule:** LeCun (SELU/linear), Xavier (tanh/sigmoid), He (ReLU-like).  
4) **Pick distribution:** **uniform** for classifiers/logits; **normal** elsewhere (both fine).  
5) **Set bias:** zero (or forget bias > 0 for LSTM).  
6) **If RNN:** make recurrent matrices **orthogonal**.  
7) **If very deep:** consider **LSUV** pass or zero-init last BN in residual blocks.

---

## 9) Sanity checks (5 minutes)

- **Activation stats (per layer on 1 batch):** mean ≈ 0, std ≈ 1 (roughly).  
  • If std shrinks layer-by-layer → too small init (vanishing) → move from LeCun→Xavier→He or increase gain.  
  • If std grows → too large (exploding) → pick smaller rule (He→Xavier→LeCun) or reduce gain.  
- **Grad norms across depth:** should be in the same ballpark.  
- **First forward loss finite:** no NaNs/Infs.  
- **Training starts moving in first few steps:** if flat, increase scale (within rule) or check optimizer/lr.

---

## 10) Ready-to-use cheats (copy values)

**Uniform limits (`a`)**
- LeCun: `a = √(3 / fan_in)`  
- Xavier: `a = √(6 / (fan_in + fan_out))`  
- He: `a = √(6 / fan_in)`  
- He (leaky α): `a = √(6 / fan_in) × √(1 / (1 + α²))`

**Normal std**
- LeCun: `σ = √(1 / fan_in)`  
- Xavier: `σ = √(2 / (fan_in + fan_out))`  
- He: `σ = √(2 / fan_in)`  
- He (leaky α): `σ = √(2 / fan_in) × √(1 / (1 + α²))`

**Common gains (`g`)**
- Linear / sigmoid: `1`  
- **tanh:** `5/3` (for orthogonal)  
- **ReLU:** `√2`  
- **leaky ReLU(α):** `√(2 / (1 + α²))`  
- **SELU:** `1` (but use **LeCun normal**)

---

## 11) Architecture quick table

| Model piece | Do this |
|---|---|
| MLP (ReLU/GELU) | **He** (normal or uniform) for all hidden; bias 0. |
| CNN (ReLU) | **He** with conv fans; classifier head **Xavier uniform**. |
| RNN (tanh) | Input weights **Xavier**; recurrent **orthogonal**; LSTM forget bias **1–2**. |
| RNN (ReLU) | Input **He**; recurrent **orthogonal**; consider leaky ReLU with proper gain. |
| Residual nets + BN | Usual He/Xavier; set **last BN gamma = 0** in blocks. |
| Residual nets no norm | Use **scaled residual** or FixUp-style small init; test LSUV. |
| Transformers | Linear/attention **Xavier**; embeddings `std ≈ 0.02–1/√d`; LayerNorm `γ=1, β=0`. |
| Output: regression | Small **Xavier/LeCun**; bias = target mean (optional). |
| Output: logits | **Xavier uniform**; bias 0 (or log-prior for class imbalance). |

---

## 12) Small pitfalls to avoid
- Using **He** with **tanh/sigmoid** (too large → saturation).  
- Using **Xavier** with **ReLU** in very deep nets (can shrink/vanish).  
- Forgetting **orthogonal** for recurrent weights.  
- Setting **all biases to big constants** (hurts symmetry; except LSTM forget bias).  
- Mixing **SELU** with **non-LeCun** init (breaks self-normalization).  
- Ignoring conv fans (must include kernel area).

---

## 13) Minimal pseudo-flow (framework-agnostic)

For each layer:
- compute fan_in, fan_out
- choose rule by activation  # LeCun / Xavier / He
- v = chosen_variance(fan_in, fan_out, activation)
- if normal:  W ~ N(0, v)
- if uniform: W ~ U[-sqrt(3v), +sqrt(3v)]
- bias = 0 (except LSTM forget bias = 1..2)
- if recurrent: make W_hh orthogonal (optionally with gain)

  ---

## 14) One-screen summary
- **Pick by activation:** ReLU-family → **He**; tanh/sigmoid → **Xavier**; SELU → **LeCun**.  
- **Fans matter:** use correct `fan_in`/`fan_out` (conv uses kernel area).  
- **RNNs:** orthogonal recurrent; forget bias > 0.  
- **Residuals:** zero last BN gamma or use small residual scale.  
- **Check stats:** per-layer std ~ 1; adjust rule/gain if it drifts.