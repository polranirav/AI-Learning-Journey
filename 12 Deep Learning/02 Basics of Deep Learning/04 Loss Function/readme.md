# Loss Functions — A Single, Simple, One-File Guide

## 1) What a loss function is (and why it matters)
A loss function turns “how wrong the model is” into a single number. Training tries to minimize this number by changing the model’s weights and biases. Backpropagation uses the gradient of the loss to decide which way and how much to change each parameter.

Notation (per sample): input x, label y, prediction ŷ.  
Loss per sample: L(ŷ, y).  
Over a batch: average (or sum) the per-sample losses.

## 2) Where loss fits in training
1) Forward: compute ŷ from x.  
2) Loss: compute L(ŷ, y).  
3) Backward: compute gradients ∂L/∂θ for all parameters θ.  
4) Update: θ := θ − η · (∂L/∂θ)  (η = learning rate).

Pick a loss that matches your task and output activation.

---

# Loss Functions 


| Group | Name | Use for | Core formula (per sample) | Output/Activation | Gradient (at output/logit) | Robustness & notes | Knobs / defaults |
|---|---|---|---|---|---|---|---|
| Regression | **MSE** (Mean Squared Error) | Numeric target, smooth errors | \(L=\tfrac12(\hat y-y)^2\) | Linear output | \(\partial L/\partial \hat y=\hat y-y\) | Simple, convex; **sensitive to outliers** | Scale targets if large; report RMSE |
| Regression | **MAE** (Mean Absolute Error) | Numeric target, outliers present | \(L=|\hat y-y|\) | Linear output | subgrad \(\in[-1,1]\), use \(\mathrm{sign}(\hat y-y)\) | **Robust** to outliers; can train slower far from target | Lower LR than MSE; consider smooth alt (Huber) |
| Regression | **Huber(δ)** | Mix of MSE (small err) + MAE (large err) | \(e=\hat y-y\)\; \(L=\begin{cases}\tfrac12 e^2,&|e|\le \delta\\ \delta|e|-\tfrac12\delta^2,&\text{else}\end{cases}\) | Linear output | \(\partial L/\partial \hat y=\begin{cases}e,&|e|\le\delta\\ \delta\,\mathrm{sign}(e),&\text{else}\end{cases}\) | Smooth near 0, **robust** on big errors | \(\delta\approx 1\) (or ~1–2× noise std) |
| Regression | **Log-cosh** | Smooth robust alt to MSE | \(L=\log\!\cosh(\hat y-y)\) | Linear output | \(\partial L/\partial \hat y=\tanh(\hat y-y)\) | MSE-like small errors, MAE-like large | No knob; good default if Huber not handy |
| Regression | **Poisson** (deviance) | Counts (non-neg.) | \(L=\lambda-y\log\lambda\) (ignore const) | \(\lambda=\exp(z)\) (log link) | \(\partial L/\partial z=\lambda-y\) | Use for events/rates; ensure positivity | Clip extreme \(z\); check dispersion |
| Binary class | **BCE + sigmoid** | 0/1 label | Stable form: \(L=\mathrm{softplus}(z)-y\,z\) | \(p=\sigma(z)\) | \(\partial L/\partial z=p-y\) | Standard choice; supports class weights | Use weights for imbalance; avoid plain \(\log p\) |
| Multi-label | **Sum BCE (K sigmoids)** | Many independent 0/1 labels | \(L=\sum_k[-y_k\log p_k-(1-y_k)\log(1-p_k)]\) | \(p_k=\sigma(z_k)\) | \(\partial L/\partial z_k=p_k-y_k\) | One-vs-rest; per-class weights ok | Calibrate thresholds per class |
| Multiclass | **Softmax + CE** | One true class among K | \(L=-\log p_{\text{true}}\) with \(p_k=\exp(z_k)/\sum_j\exp(z_j)\) | Softmax | \(\partial L/\partial z_k=p_k-y_k\) | Shift logits by \(\max(z)\) for stability | Try **label smoothing** \(\varepsilon=0.1\) |
| Multiclass | **Label smoothing** (target trick) | Regularize CE targets | \(y^*=(1-\varepsilon)y+\varepsilon/K\) then CE | Softmax | \(\partial L/\partial z=p-y^*\) | Reduces over-confidence; better gen | \(\varepsilon\in[0.05,0.2]\) |
| Margin | **Hinge** (binary) | Large-margin linear score | \(L=\max(0,1-y\,s)\) with \(y\in\{-1,+1\}\) | Linear score \(s\) | subgrad: 0 if margin ok; else \(-y\) | SVM style; not prob-calibrated | Use with linear heads; tune C via decay |
| Margin | **Multiclass hinge** | Margin on true vs others | \(L=\max_{j\ne y}[1+s_j-s_y]_+\) | Linear scores | Push up \(s_y\), down worst violator | Works with linear classifiers | Add weight decay |
| Imbalance | **Focal(γ,α)** | Class imbalance, hard cases | Binary: \(L=-\alpha(1-p)^\gamma y\log p -(1-\alpha)p^\gamma(1-y)\log(1-p)\) | Sigmoid (or softmax var.) | (use autodiff) | Down-weights easy, focus on hard | \(\gamma=2\), \(\alpha=0.25\) (tune) |
| Regularize | **L2 (weight decay)** | Shrink weights | Add \(\tfrac{\lambda_2}{2}\|W\|_2^2\) to loss | Any | Adds grad \(+\lambda_2 W\) (or decouple) | Use **AdamW/LAMB** for decoupled decay | Start \(\lambda=0.01\) (AdamW) |
| Regularize | **L1** | Sparsity | Add \(\lambda_1\|W\|_1\) | Any | Adds subgrad \(+\lambda_1\,\mathrm{sign}(W)\) | Promotes zeros; can hurt smoothness | Small \(\lambda_1\), combine with L2 |
| How-to | **Match loss ↔ head** | Pick right pair | — | — | — | Regr: linear+MSE/Huber; Binary: sigmoid+BCE; Multiclass: softmax+CE; Multi-label: K sigmoids+BCE | Avoid MSE on probabilities |
| How-to | **Reduction** | Sample→batch | Batch loss = **mean** of sample losses | — | — | Mean keeps LR scale stable vs batch size | If using sum, lower LR |
| Stability | **Safe BCE/CE** | Avoid \(\log(0)\) | Use softplus/log-sum-exp; shift logits by \(\max(z)\) | Sigmoid/Softmax | — | Clip probs to \([ε,1-ε]\), \(ε\approx10^{-7}\) | Prefer library “*_with_logits” APIs |
| Delta | **Output delta rule** | Last-layer gradient | — | — | For MSE: \(\hat y-y\); BCE(sigmoid): \(p-y\); CE(softmax): \(p-y\) | Same simple pattern: **pred − target** | Remember this shape |
| Imbalance | **Class weights / sampling** | Skewed data | Weighted BCE/CE; re-sample | — | — | Combine with focal or weights, not both too strong | Keep validation unskewed |

## 3) Regression losses (predict a number)

### 3.1 Mean Squared Error (MSE)
Definition (½ simplifies gradients):  
L = ½ (ŷ − y)²  
Derivative: ∂L/∂ŷ = (ŷ − y)  
Good for smooth errors (Gaussian-like); sensitive to outliers.

### 3.2 Mean Absolute Error (MAE)
L = |ŷ − y|  
Subgradient: ∂L/∂ŷ = sign(ŷ − y) (undefined at 0; use 0 or any value in [−1, 1])  
Robust to outliers; can train slower far from the target.

### 3.3 Huber loss (robust and smooth)
Parameter δ > 0 (e.g., 1.0).

Piecewise definition:
L(ŷ,y) =
    ½ (ŷ − y)²                  if |ŷ − y| ≤ δ
    δ|ŷ − y| − ½δ²              otherwise

Derivative:
∂L/∂ŷ =
    (ŷ − y)                     if |ŷ − y| ≤ δ
    δ · sign(ŷ − y)             otherwise

Smooth like MSE near zero, robust like MAE for large errors.

### 3.4 Log-cosh
L = log(cosh(ŷ − y))  
Derivative: ∂L/∂ŷ = tanh(ŷ − y)  
MSE-like near zero, MAE-like for large errors.

### 3.5 Poisson (for counts; positive mean)
Rate λ = ŷ > 0, label y ∈ {0,1,2,...}.  
L = λ − y · log(λ)  (ignoring constants)  
∂L/∂λ = 1 − y/λ  
Often predict z and set λ = exp(z) to keep positivity; backprop via chain rule.

---

## 4) Classification losses

### 4.1 Binary Cross-Entropy (BCE) with sigmoid
Output activation: σ(z) = 1/(1+e^(−z)), prediction p = ŷ = σ(z).  
Loss (y ∈ {0,1}):  L = −[ y log p + (1 − y) log(1 − p) ]

Numerically stable with logit z:  
softplus(z) = log(1 + e^z)  
L = softplus(z) − y · z

Key gradient: ∂L/∂z = p − y  
Last-layer gradients: ∂L/∂W = (p − y) · a_prevᵀ,  ∂L/∂b = (p − y)

### 4.2 Multi-label BCE (independent sigmoids)
For K labels, y ∈ {0,1}^K, p = σ(z) element-wise:  
L = − Σ_k [ y_k log p_k + (1 − y_k) log(1 − p_k) ]  
Per-class gradient: ∂L/∂z_k = p_k − y_k

### 4.3 Softmax + Cross-Entropy (multiclass, single label)
Logits z ∈ R^K, softmax p_k = exp(z_k)/Σ_j exp(z_j)  
One-hot y: L = − Σ_k y_k log p_k = −log(p_true)

Stability: let m = max(z); use z − m inside exp and log-sum-exp.  
Key gradient: ∂L/∂z_k = p_k − y_k

### 4.4 Hinge losses (margin-based)
Binary hinge (y ∈ {−1,+1}, score s = z):  
L = max(0, 1 − y · s) ; subgrad ∂L/∂s = 0 if margin ok, else −y

Multiclass hinge (Crammer–Singer):  
L = max_{j≠y} [1 + s_j − s_y]_+ ; subgrad pushes up s_y and down the highest violator.

### 4.5 Focal loss (imbalance; focus on hard cases)
Binary focal:  
L = − α (1 − p)^γ y log p − (1 − α) p^γ (1 − y) log(1 − p)  
γ ≥ 0 (e.g., 2) down-weights easy samples; α balances classes.

### 4.6 Label smoothing (regularizes targets)
Replace one-hot y with y* = (1 − ε) y + ε/K.  
Use standard CE with y*; gradient becomes p − y* (reduces overconfidence).

---

## 5) Match activation to loss (compatibility)
Regression: linear output + MSE/Huber.  
Binary: sigmoid + BCE (then ∂L/∂z = p − y).  
Multiclass single-label: softmax + CE (then ∂L/∂z = p − y).  
Multi-label: sigmoid per class + summed BCE.  
Avoid MSE on sigmoid/softmax probabilities unless you have a reason.

---

## 6) Regularization (penalties added to loss)
Let L_data be the data loss. Full objective often:

L_total = L_data + λ₂ · (½‖W‖₂²) + λ₁ · ‖W‖₁

L2 (weight decay): gradient adds λ₂ · W  
L1 (sparsity): subgradient adds λ₁ · sign(W)  
Reduces overfitting by discouraging large weights.

---

## 7) Reduction: sample → batch → epoch
Per-sample loss L_i  
Batch loss = mean_i L_i  (or sum_i L_i)  
Mean reduction makes LR tuning less sensitive to batch size.  
Report epoch metrics (means across all batches).

---

## 8) Class imbalance
Weighted CE/BCE: multiply per-class terms by weights.  
Focal loss: emphasize hard/rare samples.  
Sampling: over-sample minority or under-sample majority (use carefully with validation).

---

## 9) Numerical stability
BCE (sigmoid): use L = softplus(z) − y · z (no log(σ) directly).  
Softmax CE: use log-sum-exp with shifted logits z − max(z).  
Clip probabilities p to [ε, 1−ε] (e.g., 1e−7) before log if needed.  
Never compute log(0).

---

## 10) Loss vs metric
Loss is optimized (must be differentiable almost everywhere).  
Metrics (accuracy, F1, AUC, MAE, RMSE, etc.) describe performance; many are non-differentiable.  
Train with loss; monitor both loss and metrics.

---

## 11) Output-layer gradient cheat-sheet (for backprop)
MSE + linear:          ∂L/∂z = (ŷ − y)   if L = ½(ŷ − y)²  
BCE + sigmoid:         ∂L/∂z = (σ(z) − y)  
Softmax + CE:          ∂L/∂z = (softmax(z) − y)  
In all three, the output “delta” equals prediction minus target.

---

## 12) Worked examples

### 12.1 Regression (MSE), 1-D linear model
Model: ŷ = w x + b  
Example: x = 2.0, y = 5.0, w = 0.5, b = 0.0, η = 0.1

Forward: ŷ = 0.5·2 + 0 = 1.0; error e = ŷ − y = −4.0; loss L = ½·(−4)² = 8.0  
Gradients: ∂L/∂ŷ = e = −4.0 ; ∂L/∂w = e·x = −8.0 ; ∂L/∂b = e·1 = −4.0  
Update: w := 0.5 − 0.1·(−8.0) = 1.3 ; b := 0.0 − 0.1·(−4.0) = 0.4  
Check: ŷ_new = 1.3·2 + 0.4 = 3.0; new loss = ½·(−2)² = 2.0 (down from 8.0)

### 12.2 Binary (BCE + sigmoid), 1 feature
Model: z = w x + b ; p = σ(z)  
Example: x = 1.0, y = 1, w = 0.0, b = 0.0, η = 0.1

Forward: z = 0; p = 0.5; loss L = −log p ≈ 0.6931  
Shortcut gradient: ∂L/∂z = p − y = −0.5  
Param grads: ∂L/∂w = (p − y)·x = −0.5 ; ∂L/∂b = −0.5  
Update: w := 0 + 0.05 = 0.05 ; b := 0 + 0.05 = 0.05  
Check: z = 0.10 → p ≈ 0.525; loss ≈ 0.645 (down)

### 12.3 Multiclass (softmax + CE)
Logits z = [2, 1, 0], true class = 0 (y = one-hot [1,0,0])

Shift: z' = [0, −1, −2] ; exp = [1, e^(−1), e^(−2)] ≈ [1, 0.368, 0.135]  
Sum ≈ 1.503 → p ≈ [0.665, 0.245, 0.090]  
Loss: L = −log(0.665) ≈ 0.407  
Gradient wrt logits: ∂L/∂z = p − y ≈ [−0.335, 0.245, 0.090]  
For class-k weights in last layer: ∂L/∂W_k = (p_k − y_k) · a_prevᵀ

---

## 13) Fast picker (what to use)
Numeric target: MSE; try Huber if outliers hurt.  
Binary label: BCE + sigmoid.  
Multiclass single label: CE + softmax; consider label smoothing.  
Multi-label: BCE + per-class sigmoid.  
Counts: Poisson deviance with exp link.  
Imbalanced: BCE/CE + class weights or focal loss.  
Add L2 (weight decay) for most nets; L1 for sparsity.

---

## 14) Quick reference
MSE:             ½(ŷ − y)² ; grad: (ŷ − y)  
MAE:             |ŷ − y| ; subgrad: sign(ŷ − y)  
Huber(δ):        quad near 0, linear outside; see piecewise above  
BCE + sigmoid:   L = softplus(z) − y·z ; ∂L/∂z = σ(z) − y  
Softmax + CE:    L = −y·log softmax(z) ; ∂L/∂z = softmax(z) − y  
Hinge:           max(0, 1 − y·s)  
Focal:           down-weights easy examples  
Regularization:  add λ₂·½‖W‖² (+ λ₁‖W‖₁ if needed)