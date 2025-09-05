# Activation Functions 
---

## What to use by default

- **Binary classification (1 output):** `Sigmoid` on the output.  
- **Multi-class (mutually exclusive classes):** `Softmax` on the output.  
- **Regression (real number output):** **Linear** (no activation) on the output.  
- **Hidden layers (general):** start with **ReLU** or **SiLU/Swish** (often better), try **GELU** for Transformers/NLP.  
- **Self-normalizing nets:** **SELU** + **AlphaDropout** + **LeCunNormal** init.  
- If neurons “die” with ReLU → try **LeakyReLU / PReLU / ELU / SiLU**.  
- If training is unstable or gradients tiny → prefer **ReLU-family / SiLU / GELU**, avoid saturating (Sigmoid/Tanh) in deep hidden layers.

---

## Why activations matter (30-second view)

- Without them, a deep net reduces to a **linear** model (can’t learn curves/complex patterns).
- Activations decide **range**, **smoothness**, **gradient flow**, **speed**, and **stability**.
- Bad picks → **vanishing gradients**, **dead neurons**, slow training, or poor accuracy.

---

## Quick decision guide

1) **What is your output type?**
- Real number → **Linear**
- Probability of “yes/no” → **Sigmoid**
- Probabilities over classes that sum to 1 → **Softmax**
- Log-probabilities (for NLL loss) → **LogSoftmax**

---


2) **What about hidden layers?**
- Start with **ReLU**/**SiLU**.  
- If you see many zeros (“dead” units) → **LeakyReLU** or **PReLU**.  
- Need smoother grads / Transformer-like models → **GELU** (or **SiLU**).  
- Want built-in normalization behavior → **SELU** (with AlphaDropout + LeCun init).

---

## Core activations (with where/why)

### 1) Linear (a.k.a. Identity)
- **Formula:** `f(x) = x`
- **Range:** (−∞, +∞)
- **Use:** Regression outputs.
- **Pros:** No squashing; outputs can be any real value.  
- **Cons:** If used everywhere, model stays linear → can’t learn non-linear patterns.

### 2) Sigmoid (Logistic)
- **Formula:** `f(x) = 1 / (1 + e^(−x))`
- **Range:** (0, 1), **not zero-centered**
- **Use:** Binary classification **output** (probability).
- **Pros:** Interpretable probability.
- **Cons:** **Vanishing gradients** for large |x|; slower training if used in deep **hidden** layers.

### 3) Tanh
- **Formula:** `f(x) = (e^x − e^(−x)) / (e^x + e^(−x))`
- **Range:** (−1, 1), **zero-centered**
- **Use:** Sometimes in shallow nets or RNNs; better than Sigmoid in hidden layers (still saturates).
- **Pros:** Zero-centered; stronger gradients than Sigmoid near 0.
- **Cons:** Still saturates → **vanishing gradients** in deep stacks.

### 4) ReLU (Rectified Linear Unit)
- **Formula:** `f(x) = max(0, x)`
- **Range:** [0, +∞)
- **Use:** Default for hidden layers in many CNNs/MLPs.
- **Pros:** Simple, fast, mitigates vanishing (positive side has grad 1).  
- **Cons:** **Dying ReLU** (units stuck at 0) if learning rate/initialization is off.

### 5) Leaky ReLU
- **Formula:** `f(x) = x` if `x>0`, else `αx` (α ~ 0.01)
- **Use:** Fix dead ReLUs.
- **Pros:** Keeps small gradient for negative x → fewer dead units.
- **Cons:** Need to pick α; slight bias in negative region.

### 6) PReLU (Parametric ReLU)
- **Like Leaky ReLU,** but α is **learned**.
- **Pros:** Learns best negative slope per channel/layer → often better than fixed α.
- **Cons:** Adds parameters; potential overfitting on tiny datasets.

### 7) ELU (Exponential Linear Unit)
- **Formula:** `x` if `x>0`; `α(e^x − 1)` if `x<=0`
- **Use:** Alternative to ReLU with negative saturation.
- **Pros:** Outputs can be negative (more zero-centered); smoother than ReLU.
- **Cons:** Uses `exp` → slightly slower; α tuning.

### 8) SELU (Scaled ELU)
- **Use:** **Self-normalizing** networks (keep activations near zero mean & unit variance).  
- **Recipe:** **SELU + AlphaDropout + LeCunNormal init** + proper dense stacks.
- **Pros:** Helps stabilize deep nets.  
- **Cons:** Conditions must be met (architecture/init/dropout type).

### 9) SiLU / Swish
- **Formula:** `f(x) = x * sigmoid(x)`  (PyTorch name: **SiLU**)
- **Use:** Modern default; widely used in vision/NLP.
- **Pros:** Smooth, non-monotonic; often **better than ReLU**; good gradient flow.
- **Cons:** Slightly slower than ReLU (needs sigmoid).

### 10) GELU (Gaussian Error Linear Unit)
- **Approx:** `0.5 * x * (1 + tanh(√(2/π) * (x + 0.044715x^3)))`
- **Use:** Transformers (BERT, etc.), NLP, large models.
- **Pros:** Very smooth; strong empirical results in Transformers.
- **Cons:** More compute than ReLU.

### 11) Softplus
- **Formula:** `f(x) = log(1 + e^x)`  (smooth ReLU)
- **Use:** When you need a smooth ReLU; also to ensure **positive** outputs by pairing with transformations.
- **Pros:** Always positive, smooth gradient.
- **Cons:** Slower; can be numerically large for big x (use stable implementations).

### 12) Softsign
- **Formula:** `x / (1 + |x|)`  (smooth, bounded)
- **Use:** Rare today; alternative smooth squashing with gentler tails.

### 13) Hard variants (efficient on edge devices)
- **HardTanh, HardSigmoid, HardSwish:** piecewise-linear approximations.  
- **Use:** Mobile/edge inference where speed matters.  
- **Trade-off:** Faster, but less smooth.

### 14) Softmax (for multi-class probabilities)
- **Formula:** `softmax(z_i) = exp(z_i / T) / Σ_j exp(z_j / T)` (often T=1)
- **Use:** Output layer for single-label multi-class classification.
- **Notes:** Combine with **Cross-Entropy** loss. Consider **label smoothing** for regularization.

### 15) LogSoftmax
- **Use:** With **NLLLoss** (negative log likelihood) for numerical stability vs. `log(softmax)`.

### 16) Maxout (less common now)
- **Idea:** Output = max over a set of learned linear units.  
- **Pros:** Can approximate many activations.  
- **Cons:** More parameters/compute.

### 17) Gated activations (GLU/GEGLU/Swish-GLU)
- **Idea:** `output = A(x) ⊙ Gate(x)` with Gate often `sigmoid` or `SiLU`.  
- **Use:** NLP/Transformers; improves expressiveness.  
- **Cons:** More params/compute.

---

## Classic pitfalls & how activations affect them

- **Vanishing gradients:** Sigmoid/Tanh saturate (grad → 0) at large |x|.  
  **Fix:** ReLU/LeakyReLU/PReLU/ELU/SiLU/GELU; proper init; normalization.
- **Dying ReLU:** Units stuck at 0.  
  **Fix:** Lower LR; better init; switch to **LeakyReLU/PReLU/ELU/SiLU**.
- **Exploding gradients:** (less about activation, more about init/optimizer).  
  **Fix:** Gradient clipping; normalization; smaller LR.
- **Shifted distributions across layers:**  
  **Fix:** **BatchNorm/LayerNorm/SELU** (with its recipe).

---

## Choosing by task (simple recipes)

- **Vision CNNs:** ReLU → try **SiLU**/**GELU** for a bump.  
- **Transformers/NLP:** **GELU** (common) or **SiLU**.  
- **Tabular MLPs:** Start **ReLU/SiLU**; if over-regularized, try **Tanh** in shallow nets.  
- **Self-normalizing MLP:** **SELU** (+ AlphaDropout + LeCunNormal).  
- **Edge/mobile:** **HardSwish/HardSigmoid** for speed.

---

## Output layer mapping (don’t mix these up)

- **Regression:** Linear + MSE/MAE/Huber loss.  
- **Binary class (1 logit):** Sigmoid + BinaryCrossEntropy.  
- **K-class, single label:** Softmax + CrossEntropy.  
- **K independent labels (multi-label):** Sigmoid per class + BinaryCrossEntropy.

---



# Activation Functions — Cheat Sheet (Properties)

| Activation | Definition `f(x)` | Output Range | Zero-Centered | Saturates (where) | Smooth | f′(0) | Typical Init | Notes / When to Use | Watch-outs |
|---|---|---|---|---|---|---|---|---|---|
| **Linear** | `x` | (−∞, +∞) | ✅ | No | ✅ | 1 | Xavier/He | Regression outputs; final layer for real values | Unbounded outputs can explode if loss/targets unscaled |
| **Sigmoid** | `1/(1+e^(−x))` | (0, 1) | ❌ | Both tails | ✅ | 0.25 | **Xavier/Glorot** | Binary **output** (with BCE) | Vanishing gradients; don’t use in deep hidden layers |
| **Tanh** | `tanh(x)` | (−1, 1) | ✅ | Both tails | ✅ | 1 | **Xavier/Glorot** | Sometimes shallow hidden layers | Still saturates; can vanish in deep nets |
| **ReLU** | `max(0, x)` | [0, +∞) | ❌ | x<0 (dead zone) | ❌ | ~1/0 | **He/Kaiming** | Default for many hidden layers; cheap and strong | “Dead ReLU” if LR too high or bad init |
| **Leaky ReLU** | `max(ax, x)` (a≈0.01) | (−∞, +∞) | ~✅ | No (small neg slope) | ❌ | +:1 / −:a | **He/Kaiming** | Fix for dead ReLUs; small extra robustness | Choose `a` (0.01–0.2); not fully smooth |
| **PReLU** | `max(ax, x)` (a learnable) | (−∞, +∞) | ~✅ | No | ❌ | +:1 / −:a | **He/Kaiming** | Lets model learn negative slope | Slight overfit risk; more params |
| **ELU** | `x` if x>0 else `α(e^x−1)` | (−α, +∞) | ✅ | Neg side | ✅ | 1 | **He/Kaiming** | Mean-shifting to ~0; helps gradients | Uses `exp` (slower); pick α (≈1) |
| **SELU** | `λ * (x if x>0 else α(e^x−1))` | (~−1.76, +∞) | ✅ | Neg side | ✅ | ~1 | **LeCun Normal** | Self-normalizing MLPs (+ **AlphaDropout**) | Works best w/ dense layers; avoid BN with SELU |
| **SiLU / Swish** | `x * sigmoid(x)` | (−∞, +∞) | ✅ | Soft tails | ✅ | 0.5 | **He/Kaiming** | Strong general default; often better than ReLU | Slightly slower than ReLU |
| **GELU** | `x * Φ(x)` ≈ `0.5x(1+tanh(√(2/π)(x+0.044715x^3)))` | (−∞, +∞) | ✅ | Soft tails | ✅ | 0.5 | **He/Kaiming** | SOTA in many Transformers/CNNs | Heavier compute than ReLU/Leaky |
| **Hard-Swish** | `x * hard_sigmoid(x)` | (−∞, +∞) | ✅ | Soft tails | piecewise | ~0.5 | **He/Kaiming** | Mobile/edge (fast approx to Swish) | Piecewise approx; minor accuracy loss |
| **Softplus** | `ln(1+e^x)` | (0, +∞) | ❌ | Neg side | ✅ | 0.5 | **He/Kaiming** | Smooth ReLU alternative; positive outputs | Always positive; may shift means |
| **Softsign** | `x/(1+(mode(x))` | (−1, 1) | ✅ | Both tails | ✅ | 1 | **Xavier** | Smooth tanh-like; gentle saturation | Weaker gradients far from 0 |
| **Hard-Sigmoid** | piecewise linear approx of sigmoid | (0, 1) | ❌ | Ends | piecewise | ~0.2–0.25 | **Xavier** | Very fast probability proxy on devices | Cruder; use only where speed critical |
| **Softmax** (output) | `e^{x_i}/Σ_j e^{x_j}` | (0,1), sums to 1 | — | — | ✅ | — | — | **Multi-class output** with Cross-Entropy | Use only on last layer (classes) |
| **LogSoftmax** (output) | `log(softmax(x))` | (−∞, 0) | — | — | ✅ | — | — | Stable with **NLLLoss** | Output-only; not for hidden layers |

### Quick Pairing Guide (outputs)
- **Binary / multi-label:** Sigmoid + BCE/BCEWithLogits  
- **Single-label multi-class:** Softmax + CrossEntropy (or LogSoftmax + NLLLoss)  
- **Regression (ℝ):** Linear + MSE/MAE/Huber  
- **Strictly positive regression:** Softplus/Exp + appropriate loss/scale  
or label smoothing for classification.

## Practical tips (that save hours)

1) **Keep hidden activations non-saturating** in deep nets → ReLU/SiLU/GELU.  
2) **Watch your learning rate.** Too big LR can cause dying ReLUs or instabilities.  
3) **Initialization matters.**  
   - ReLU/Leaky/PReLU/ELU/SiLU/GELU → **Kaiming/He** init.  
   - SELU → **LeCunNormal**.  
4) **Normalization helps.** BatchNorm/LayerNorm can let you use simpler activations safely.  
5) **Monitor activations.** If many zeros with ReLU → try LeakyReLU/PReLU or reduce LR.  
6) **Numerics:** Use framework’s **stable** Softmax/LogSoftmax; avoid manual exp/sum.

---