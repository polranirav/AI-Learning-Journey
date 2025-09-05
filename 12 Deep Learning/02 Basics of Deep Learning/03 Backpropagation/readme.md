# Backpropagation (What, How, Why + Examples)

## 1) The 30-second idea

**Backpropagation** (“backprop”) is the method that **tells every weight and bias in a neural network how to change** so the model gets better.

It does three things, in this order:

1. **Forward pass** – make a prediction `ŷ` from the input `x`.
2. **Loss** – measure “how wrong” the prediction is: `L(ŷ, y)`.
3. **Backward pass** – send the error **backwards** through the network using the **chain rule** from calculus to compute the **gradient** (slope) of `L` with respect to **every** weight and bias.

Finally, we **update** each parameter a little **opposite** its gradient:

- `parameter := parameter - learning_rate * gradient`.

That’s it.

---

## 2) Ingredients you should know (super quick)

**Forward propagation (a 2-layer example):**

- Hidden pre-activation: `z1 = W1 x + b1`
- Hidden activation: `a1 = φ(z1)`  (e.g., ReLU, sigmoid, tanh, or linear)
- Output pre-activation: `z2 = W2 a1 + b2`
- Prediction: `ŷ = g(z2)`  (linear for regression; sigmoid/softmax for classification)

**Loss (how wrong):**
- Regression: mean squared error (MSE) like `L = (ŷ - y)²` (or average over a batch)
- Binary classification: binary cross-entropy (BCE)
- Multiclass: cross-entropy (CE) with softmax

**Gradient descent (one step):**
- For any parameter `θ`:  `θ := θ - η * ∂L/∂θ`  (η = learning rate)

> Reading tip: “∂L/∂θ” just means “how much the loss would change if θ changes a tiny bit.” That’s the gradient.

---

## 3) Picture in your head (text sketch)

Input `x` goes **forward** to a prediction `ŷ`, we compute **Loss**, then a signal `δ` travels **backward**, layer by layer, telling each weight/bias the direction to move.

- Forward: `x → [layer 1] → [layer 2] → ŷ`
- Backward: `Loss → δ₂ → δ₁ → (gradients for W’s and b’s)`

---

## 4) Backprop in one paragraph (the chain rule in words)

You can’t change the true label `y`. You **can** change `ŷ` by changing weights and biases.  
The **chain rule** says: “If changing `W` changes `z`, and changing `z` changes `ŷ`, and changing `ŷ` changes `L`, then changing `W` changes `L` by the product of those effects.”  
Backprop applies this principle efficiently to **all** parameters in a few matrix multiplications.

---

## 5) Our tiny running network (notation we’ll reuse)

We’ll use a 2-2-1 network (easy but general):

- Inputs: `x ∈ R²`
- Hidden: 2 units (activation `φ`)
- Output: 1 unit (activation `g`)
- `W1 ∈ R^{2×2}`, `b1 ∈ R²`; `W2 ∈ R^{1×2}`, `b2 ∈ R`

Forward step:
- `z1 = W1 x + b1`, `a1 = φ(z1)`
- `z2 = W2 a1 + b2`, `ŷ = g(z2)`

---

## 6) The essential backprop formulas (cheat-sheet you will use a lot)

**Output layer error signal (`δ2 = ∂L/∂z2`):**

- Regression (MSE, linear output): `δ2 = ŷ - y`
- Binary classification (BCE + sigmoid): `δ2 = ŷ - y`
- Multiclass (CE + softmax with one-hot `y`): `δ2 = ŷ - y`

**Gradients at output:**

- `∂L/∂W2 = δ2 · a1ᵀ`
- `∂L/∂b2 = δ2`

**Back-propagate to hidden:**

- `δ1 = (W2ᵀ δ2) ⊙ φ'(z1)`  (⊙ is element-wise product)

Common `φ'(z)`:
- ReLU: `1` if `z>0`, else `0`
- Sigmoid: `σ(z)(1-σ(z))`
- Tanh: `1 - tanh²(z)`
- Linear: `1`

**Gradients at hidden:**

- `∂L/∂W1 = δ1 · xᵀ`
- `∂L/∂b1 = δ1`

**Update rule (any layer):**

- `W := W - η * ∂L/∂W`
- `b := b - η * ∂L/∂b`

> Memory trick: **“error × inputᵀ gives the weight gradient.”**  
> For the output layer: input is `a1`. For the hidden layer: input is `x`.

---

## 7) Worked example #1 — Regression with MSE (numbers shown)

**Setup**
- `x = [1, 1]`, target `y = 1`
- Hidden activation: **linear** (so `φ'(z1)=1`)
- Output activation: **linear**
- Initialize: every weight = `0.1`, every bias = `0.0`
  - `W1 = [[0.1, 0.1],[0.1, 0.1]]`, `b1 = [0, 0]`
  - `W2 = [[0.1, 0.1]]`, `b2 = [0]`
- Learning rate `η = 0.1`
- Loss: `L = (ŷ - y)²`

**Forward**
- `z1 = W1 x + b1 = [0.2, 0.2]`
- `a1 = z1 = [0.2, 0.2]`
- `z2 = W2 a1 + b2 = 0.1*0.2 + 0.1*0.2 = 0.04`
- `ŷ = 0.04`
- `L = (0.04 - 1)² = 0.9216`

**Backward**
- Output error: `δ2 = ŷ - y = -0.96`
- Output grads:
  - `∂L/∂W2 = δ2 a1ᵀ = [-0.192, -0.192]`
  - `∂L/∂b2 = -0.96`
- Hidden error: `δ1 = (W2ᵀ δ2) ⊙ 1 = [0.1, 0.1]*(-0.96) = [-0.096, -0.096]`
- Hidden grads:
  - `∂L/∂W1 = δ1 xᵀ = [[-0.096,-0.096],[-0.096,-0.096]]`
  - `∂L/∂b1 = [-0.096, -0.096]`

**Update**
- `W2 := 0.1 - 0.1*(-0.192) = 0.1192` (both entries)
- `b2 := 0   - 0.1*(-0.96)  = 0.096`
- `W1 := 0.1 - 0.1*(-0.096) = 0.1096` (all four)
- `b1 := 0   - 0.1*(-0.096) = 0.0096` (both)

**What changed?** Every parameter moved in the direction that raises `ŷ` toward `1`, so the next loss will be smaller.

---

## 8) Worked example #2 — Binary classification with BCE + sigmoid

**Setup**
- Same 2-2-1 shape, but **sigmoid** at hidden and output.
- Initialize: every weight `0.1`, every bias `0.0`, learning rate `η=0.1`.
- `x=[1,1]`, label `y=1`.
- Loss: `L = -[ y log(ŷ) + (1-y) log(1-ŷ) ]`.

**Forward**
- `z1 = W1 x + b1 = [0.2, 0.2]`
- `a1 = σ(z1) ≈ [0.5498, 0.5498]`
- `z2 = W2 a1 + b2 ≈ 0.1*0.5498 + 0.1*0.5498 ≈ 0.1100`
- `ŷ = σ(z2) ≈ 0.5275`
- `L ≈ -log(0.5275) ≈ 0.639`

**Backward (nice shortcut)**
- For **BCE + sigmoid**, output error is **`δ2 = ŷ - y`** (same simple form).
  - `δ2 ≈ 0.5275 - 1 = -0.4725`
- Output grads:
  - `∂L/∂W2 = δ2 a1ᵀ ≈ [-0.259, -0.259]`
  - `∂L/∂b2 = -0.4725`
- Hidden error:
  - `σ'(z1) = a1 ⊙ (1 - a1) ≈ [0.2475, 0.2475]`
  - `(W2ᵀ δ2) ≈ [0.1, 0.1]*(-0.4725) = [-0.04725, -0.04725]`
  - `δ1 = (W2ᵀ δ2) ⊙ σ'(z1) ≈ [-0.0117, -0.0117]`
- Hidden grads:
  - `∂L/∂W1 ≈ [[-0.0117,-0.0117],[-0.0117,-0.0117]]`
  - `∂L/∂b1 ≈ [-0.0117,-0.0117]`

**Update**
- `W2 := 0.1 - 0.1*(-0.259)  ≈ 0.1259` (both)
- `b2 := 0   - 0.1*(-0.4725) ≈ 0.04725`
- `W1 := 0.1 - 0.1*(-0.0117) ≈ 0.10117` (all four)
- `b1 := 0   - 0.1*(-0.0117) ≈ 0.00117` (both)

**What changed?** Updates push `ŷ` upward toward `1`. The loss will drop over steps/epochs.

---

## 9) The algorithm in small steps (single sample and mini-batch)

**Single sample (one update):**

1. Forward: compute `z1, a1, z2, ŷ`.
2. Loss: compute `L(ŷ, y)`.
3. Backward:
   - `δ2` (use the simple forms in Section 6).
   - `∂L/∂W2 = δ2 a1ᵀ`, `∂L/∂b2 = δ2`.
   - `δ1 = (W2ᵀ δ2) ⊙ φ'(z1)`.
   - `∂L/∂W1 = δ1 xᵀ`, `∂L/∂b1 = δ1`.
4. Update all parameters: `W -= η * grad`, `b -= η * grad`.

**Mini-batch (preferred in practice):**

- Do the same but **average** the per-sample gradients across the batch (size 32–256 is common), then update. This gives smoother progress and uses hardware efficiently.

---

## 10) Why the update has a **minus** sign (intuition)

- The gradient points in the direction of **increase** of the loss.  
- We want to **decrease** the loss, so we move **opposite** the gradient.  
- If a partial derivative is positive, we step the parameter **down**.  
- If it’s negative, we step the parameter **up**.  
The single minus sign handles both cases automatically.

---

## 11) Common gotchas (and quick fixes)

- **Learning rate too big** → loss explodes or jumps: try `1e-2` → `1e-3` → `5e-4`.
- **Learning rate too small** → loss barely moves: increase it 2–10×.
- **Wrong activation/derivative** → gradients are wrong: double-check `φ` vs `φ'`.
- **No bias terms** → model underfits: keep biases unless you truly don’t need them.
- **Unscaled inputs** → slow or unstable training: normalize or standardize features.
- **Using MSE with sigmoid/softmax outputs** → slow learning: prefer BCE/CE.
- **Batch size of 1 only** → noisy steps: try 32–256 for stability.

---

## 12) Practical training tips you can remember

- Start simple: **2-layer** network, tiny hidden size, confirm loss goes down.
- Use **ReLU** (or GELU) in hidden layers for many problems (it keeps φ′ simple).
- Initialize weights small (e.g., Kaiming/He for ReLU, Xavier/Glorot for tanh/sigmoid).
- Track the **training loss curve**; if it’s flat or exploding, adjust the learning rate.
- Use **early stopping** and **validation** to avoid overfitting.
- Prefer built-in optimizers later (Adam, RMSProp), but learn **vanilla backprop first**.

---

## 13) Tiny glossary (fast meanings)

- **Activation**: the number a neuron outputs after applying `φ(z)`.
- **Loss**: a single number that says how wrong the model is.
- **Gradient**: slope of the loss with respect to a parameter.
- **δ (“delta”)**: the error signal at a layer (`∂L/∂z`).
- **Chain rule**: multiply links of influence to get `∂L/∂(earlier thing)`.
- **Epoch**: one full pass over the dataset.

---

## 14) Quick recap checklist (say it out loud)

1. I can write the **forward pass** (`z1, a1, z2, ŷ`).
2. I can compute the **loss** for my task (MSE/BCE/CE).
3. At the output: **`δ2 = ŷ - y`** (for the standard cases).
4. I know: `∂L/∂W2 = δ2 a1ᵀ`, `∂L/∂b2 = δ2`.
5. I can backpropagate: `δ1 = (W2ᵀ δ2) ⊙ φ'(z1)`.
6. I know: `∂L/∂W1 = δ1 xᵀ`, `∂L/∂b1 = δ1`.
7. I update with a **minus**: `W -= η * gradient`, `b -= η * gradient`.
8. I watch the loss go **down** across steps/epochs.

If you can tick these 8 boxes, you understand backpropagation.

---

## 15) One-screen summary (copy to your notes)

- **Forward:** `z1=W1x+b1`, `a1=φ(z1)`, `z2=W2a1+b2`, `ŷ=g(z2)`
- **Loss:** pick MSE/BCE/CE
- **Output error:** `δ2 = ŷ - y`  (for MSE+linear, BCE+sigmoid, CE+softmax)
- **Output grads:** `dW2 = δ2 a1ᵀ`, `db2 = δ2`
- **Hidden error:** `δ1 = (W2ᵀ δ2) ⊙ φ'(z1)`
- **Hidden grads:** `dW1 = δ1 xᵀ`, `db1 = δ1`
- **Update:** `W -= η dW`, `b -= η db`

Backpropagation is just these lines, repeated for each layer and each batch.

---