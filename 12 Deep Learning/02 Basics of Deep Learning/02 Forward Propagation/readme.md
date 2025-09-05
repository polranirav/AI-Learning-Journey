# 03 — Forward Propagation (Easy & Clear)

>  Forward propagation is the step where an MLP takes your input, pushes it **layer by layer** through **Linear → Activation** blocks, and produces an output (ŷ). At each layer we compute `z = W·a + b` and then `a = g(z)`.

---

## 1) What forward prop does (in plain words)
- Starts with your **input features**.
- Each hidden layer **mixes** the previous layer’s outputs with weights (W) and bias (b), then applies a **nonlinear activation** (ReLU, Tanh, Sigmoid).
- The final layer converts to the **right output** for your task (a number for regression, a probability for binary, a probability vector for multi-class).

---

## 2) Notation you’ll see everywhere
- `L` = number of layers with learnable parameters (hidden layers + output layer).
- `a^(0)` = input vector (features).
- For layer `ℓ = 1 … L`:
  - `W^(ℓ)` has shape `(n_ℓ × n_(ℓ−1))`.
  - `b^(ℓ)` has shape `(n_ℓ × 1)`.
  - `z^(ℓ) = W^(ℓ) · a^(ℓ−1) + b^(ℓ)` (linear part).
  - `a^(ℓ) = g^(ℓ)(z^(ℓ))` (activation).
- Final prediction: `ŷ = a^(L)`.

**Batch version (m examples at once):**
- Stack examples column-wise: `A^(ℓ)` has shape `(n_ℓ × m)`.
- `Z^(ℓ) = W^(ℓ) · A^(ℓ−1) + b^(ℓ)` where `b^(ℓ)` is broadcast to all columns.
- `A^(ℓ) = g^(ℓ)(Z^(ℓ))`.

---

## 3) A tiny worked example (shapes you can copy)
Imagine a 3-layer network for binary classification:
- Input size `n0 = 3`, first hidden `n1 = 3`, second hidden `n2 = 2`, output `n3 = 1`.

Layer 1:
- `W^(1): (3×3)`, `b^(1): (3×1)`.
- `z^(1) = W^(1)a^(0) + b^(1) → (3×1)`.
- `a^(1) = ReLU(z^(1)) → (3×1)`.

Layer 2:
- `W^(2): (2×3)`, `b^(2): (2×1)`.
- `z^(2) = W^(2)a^(1) + b^(2) → (2×1)`.
- `a^(2) = ReLU(z^(2)) → (2×1)`.

Layer 3 (output):
- `W^(3): (1×2)`, `b^(3): (1×1)`.
- `z^(3) = W^(3)a^(2) + b^(3) → (1×1)`.
- `a^(3) = σ(z^(3)) = ŷ` (sigmoid gives a probability).

This mirrors the hand-drawn shape flow: `(3→3→2→1)` with linear + activation at every step.

---

## 4) Which activation where?
- **Hidden layers:** ReLU is a strong default (simple, fast, good gradients). Tanh works but can saturate; Sigmoid in hidden layers is rarely preferred now.
- **Output layer:**
  - **Regression:** identity (no activation) or sometimes Tanh if you want a bounded range.
  - **Binary classification:** Sigmoid.
  - **Multi-class (K classes):** Softmax (length-K output whose entries sum to 1).

---

## 5) Forward pass — step-by-step procedure
1) Set `a^(0)` to your input vector (or `A^(0)` for a batch).
2) For each layer `ℓ = 1 … L`:
   - Compute `z^(ℓ) = W^(ℓ) · a^(ℓ−1) + b^(ℓ)`.
   - Apply activation: `a^(ℓ) = g^(ℓ)(z^(ℓ))`.
3) Return `a^(L)` as the prediction `ŷ`.

Keep (cache) the `z` and `a` values — you’ll need them for **backprop**.

---

## 6) Sanity checks that save hours
- **Shapes match:** `(W^(ℓ) : n_ℓ × n_(ℓ−1)) · (a^(ℓ−1) : n_(ℓ−1) × 1) + (b^(ℓ) : n_ℓ × 1)` must produce `(n_ℓ × 1)`. Mismatch = bug.
- **No activation on regression outputs:** applying Sigmoid there can crush numeric range.
- **Vectorize:** operate on batches `(A, Z)` to speed up training.
- **Initialization matters:** use Xavier/Glorot for Tanh/Sigmoid, He for ReLU to keep signals from dying or exploding early.
- **Numerical stability:** for Softmax, subtract the columnwise max of `Z` before exponentials.

---

## 7) What forward prop is NOT (but connects to)
- It **does not** change weights; it only computes predictions.
- Learning happens when you pair forward prop with a **loss** and then run **backprop + optimizer** to update `W, b`.

---

## 8) Quick recap in one line
Forward propagation is just repeating **Linear (W·a + b) → Activation** from the input to the output, producing `ŷ` with the right shape and meaning for your task.