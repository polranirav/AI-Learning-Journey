# Artificial Neural Networks (ANN)

## 1) What is an ANN?
- A **neural network** is a stack of simple math units (“neurons”) that learn a mapping from **inputs** to **outputs**.
- Each neuron takes numbers, multiplies by **weights**, adds a **bias**, passes through an **activation**.
- With enough data and the right setup, the network **learns** useful patterns.

---

## 2) One neuron (the basic unit)
- Input vector `x ∈ ℝ^d`
- Weights `w ∈ ℝ^d`, bias `b ∈ ℝ`
- Linear score: `z = w·x + b`
- Activation (non-linear): `a = f(z)` (e.g., ReLU, sigmoid, tanh)
- Output `a` is the neuron’s value that flows to the next layer.

---

## 3) Layers and shapes (dense/fully-connected)
- Layer `ℓ` takes vector `a^{ℓ-1}` and produces `a^{ℓ}`:
  - `z^{ℓ} = W^{ℓ} a^{ℓ-1} + b^{ℓ}`
  - `a^{ℓ} = f^{ℓ}(z^{ℓ})`
- Shapes:
  - If previous layer has `n_{ℓ-1}` units and this layer has `n_{ℓ}` units:
    - `W^{ℓ}` shape = `[n_{ℓ} × n_{ℓ-1}]`
    - `b^{ℓ}` shape = `[n_{ℓ}]`
    - `a^{ℓ}` shape = `[n_{ℓ}]`

---

## 4) Common architectures
- **Single-Layer Perceptron (SLP):** input → output (linear); only solves linearly separable tasks.
- **Multi-Layer Perceptron (MLP):** input → hidden layer(s) → output; can learn complex, non-linear mappings.
- **Deep MLP:** several hidden layers (depth lets the net build features step by step).

---

## 5) Forward pass (predict)
Given input `x`:
1. Set `a^{0} = x`
2. For each layer `ℓ = 1..L`:
   - `z^{ℓ} = W^{ℓ} a^{ℓ-1} + b^{ℓ}`
   - `a^{ℓ} = f^{ℓ}(z^{ℓ})`
3. Final `a^{L}` is the **prediction** (e.g., logits or probabilities).

---

## 6) Loss (how wrong) — pick to match the task
- **Regression:** MSE or Huber
- **Binary class:** Sigmoid + Binary Cross-Entropy (BCE)
- **Multiclass (one label):** Softmax + Cross-Entropy (CE)
- **Multi-label:** Sigmoid (per class) + BCE

*(Use numerically stable forms in code; see your loss guide.)*

---

## 7) Backpropagation (core training math)
- Compute loss `L`.
- Compute gradients from output to input using chain rule.
- Useful last-layer shortcuts:
  - **MSE + linear:** `δ^{L} = a^{L} − y`
  - **Sigmoid + BCE:** `δ^{L} = a^{L} − y`
  - **Softmax + CE:** `δ^{L} = a^{L} − y`
- For any layer `ℓ`:
  - Grad wrt weights: `∂L/∂W^{ℓ} = δ^{ℓ} (a^{ℓ-1})^T`
  - Grad wrt bias: `∂L/∂b^{ℓ} = δ^{ℓ}`
  - Backprop to previous activations: `δ^{ℓ-1} = (W^{ℓ})^T δ^{ℓ} ⊙ f'^{ℓ-1}(z^{ℓ-1})`

---

## 8) Optimizers (update rule idea)
- Simple SGD: `θ ← θ − η · ∂L/∂θ`
- Popular: **Adam**, **SGD+Momentum**, **RMSProp** (use Adam as a safe start).
- `η` = learning rate (small step size). Start `1e−3` (Adam) or `1e−2` (SGD) then tune.

---

## 9) Activations (quick pick)
- **Hidden layers:** ReLU (simple, fast). If dead units, try LeakyReLU/ELU/GELU.
- **Output layer:**
  - Regression → **Linear**
  - Binary class → **Sigmoid**
  - Multiclass → **Softmax**
  - Multi-label → **Sigmoid** per class

---

## 10) Feature scaling (helps training)
- Standardize inputs: zero mean, unit variance per feature.
- For images: scale to `[0,1]` or standardize by dataset mean/std.
- Keep the same transform for train/val/test.

---

## 11) Weight init (good start)
- **He/Kaiming** for ReLU-like activations.
- **Xavier/Glorot** for tanh/sigmoid.
- Bias often `0`.
- Proper init reduces vanishing/exploding signals at start.

---

## 12) Regularization (controls overfitting)
- **Weight decay (L2):** add `λ · ‖W‖²`
- **Dropout:** randomly drop units at train time (e.g., `p=0.1–0.5`)
- **Early stopping:** stop when val loss stops improving
- **Data augmentation:** create varied training examples (images/text/audio)

---

## 13) Batch size, epochs, learning rate (simple starts)
- **Batch size:** 32 or 64 (adjust to memory)
- **Epochs:** 10–100 (use early stopping)
- **LR (Adam):** `1e−3` start; reduce on plateau by ×0.1
- **LR (SGD+Momentum):** `1e−2` start; try cosine decay or step decay

---

## 14) Output by task (activation + loss + metric)
| Task | Output activation | Loss (train) | Typical metric |
|---|---|---|---|
| Regression (real value) | Linear | MSE / Huber | MAE / RMSE |
| Binary classification | Sigmoid | BCE (stable form) | Accuracy, AUC, F1 |
| Multiclass (1 label) | Softmax | Cross-Entropy | Accuracy, Top-k |
| Multi-label | Sigmoid per class | BCE (sum over classes) | F1 (macro/micro) |

---

## 15) Minimal training loop (pseudo)
```
init W, b  (good init)
for epoch:
for batch (X, y):
# forward
a = forward(X)
L = loss(a, y)
# backward
grads = backprop(L)
# update
optimizer.step(params, grads)
check val metrics; save best; early stop if needed
```



---

## 16) Quick design recipe (dense MLP)
1. **Input**: match feature count (after scaling).
2. **Hidden**: 2–4 layers, width 2–8× input size (start modest).
3. **Activation**: ReLU on hidden.
4. **Regularize**: L2 (e.g., `λ=1e−4`), Dropout (e.g., `p=0.1–0.3` if overfit).
5. **Output**: choose per task (see table).
6. **Loss/Metric**: match task.
7. **Optimizer**: Adam (`lr=1e−3`).
8. **Batch/Epochs**: 32–64 / with early stopping.
9. **LR schedule**: reduce on plateau ×0.1 (patience 3–5).

---

## 17) Debug checklist (symptoms → fixes)
| Symptom | Likely cause | Quick fixes |
|---|---|---|
| Train loss flat high | LR too low; bad init; no scaling | Scale features; increase LR; use He/Xavier; check data/labels |
| Train loss `NaN` or explodes | LR too high; exploding grads | Lower LR; gradient clipping; use Adam; check loss code |
| Train ↓ but Val ↑ (overfit) | Model too big; weak regularization | Add L2/Dropout; early stop; more data/augmentation; reduce width/depth |
| Both Train and Val bad | Model too simple; underfitting | Add layers/units; try better features; raise training time |
| Accuracy stuck near class prior | Wrong output/loss pairing | Sigmoid+BCE (binary), Softmax+CE (multiclass) |
| ReLU units “dead” | LR high; init poor | Lower LR; LeakyReLU; He init |
| Very slow training | Batch too small; no vectorization | Increase batch; use vectorized ops/GPU; use Adam |

---

## 18) Tiny worked example (1-D regression, MSE)
- Model: `ŷ = w x + b`
- Start: `w=0.5, b=0.0`, sample: `x=2, y=5`, `η=0.1`
- Forward: `ŷ=1`, error `e=ŷ−y=−4`, loss `L=½ e²=8`
- Grads: `∂L/∂w = e·x = −8`, `∂L/∂b = e = −4`
- Update: `w ← 0.5 − 0.1·(−8)=1.3`, `b ← 0 − 0.1·(−4)=0.4`
- New `ŷ=1.3·2+0.4=3.0`, new loss `½(−2)²=2` (down).

---

## 19) Common layer blocks (dense MLP)
| Block | What it does | When to use |
|---|---|---|
| Dense (Linear) | `z = W a + b` | Core computation |
| Activation | Non-linearity (ReLU etc.) | After Dense |
| Dropout | Randomly zero activations | Reduce overfitting |
| BatchNorm/LayerNorm | Normalize activations | Smoother training |

---

## 20) Minimal PyTorch-style sketch (for reference)

```class MLP(nn.Module):
def init(self, din, dh, dout, p=0.2):
super().init()
self.net = nn.Sequential(
nn.Linear(din, dh), nn.ReLU(),
nn.Dropout(p),
nn.Linear(dh, dh), nn.ReLU(),
nn.Dropout(p),
nn.Linear(dh, dout)  # add Sigmoid/Softmax outside if needed
)
def forward(self, x): return self.net(x)
```

Train with Adam (`lr=1e−3`), right loss, early stopping.

---

## 21) Quick FAQs
- **How many layers?** Start 2–4 hidden; add if underfitting.
- **How wide?** 2–8× input size; widen if underfitting.
- **Which activation?** ReLU first; try LeakyReLU/ELU if issues.
- **Which optimizer?** Adam is a safe default.
- **Do I need scaling?** Yes, almost always.
- **How to stop overfit?** L2, Dropout, Early stopping, Augmentation.
- **Why val loss doesn’t move?** Check data split, scaling leakage, LR, loss/activation match.

---

## 22) Summary (one line)
**Right data + right loss + right activation + good init + a sane optimizer + regularization + tuned LR = a solid ANN.**