# Regularization — Simple, One-File Guide (regularization.md)

Regularization = ways to **reduce overfitting**. It makes your model **simpler**, **more stable**, and **better on unseen data**. You do this by adding **penalties**, **constraints**, or **noise**, and by **stopping early** when validation stops improving.

---

## 1) Quick idea
- Train loss ↓ fast, but val loss ↑ or stalls ⇒ **overfitting**.
- Regularization adds a “cost” for **too flexible** models or **too confident** predictions.
- Works best when features are **scaled** (Z-score or Robust) and data is **clean**.

---

## 2) Core math (penalties)
Let `L_data` be the usual loss (MSE, CE, …). We train with:
`L_total = L_data + λ2 * (1/2)||W||₂² + λ1 * ||W||₁`

- **L2 (weight decay):** gradient adds `λ2 * W`. In SGD update:

`W := W - η * (∇W L_data + λ2 * W) `    (classic)

`W := (1 - η*λ2) * W - η * ∇W L_data `    (same thing)

- **L1 (sparsity):** subgradient adds `λ1 * sign(W)` (soft-thresholds small weights to 0).
- **Elastic Net:** `λ2*L2 + λ1*L1` (mix of both).

**Tip:** Do **not** decay **biases** or **BatchNorm γ/β**. Decay only real weights. With Adam, use **AdamW** (decoupled weight decay) instead of L2 inside the gradient.

---

## 3) Big picture table (neural nets)

| Method | What it does | Use for | Key knobs (good starts) | Notes |
|---|---|---|---|---|
| **L2 / weight decay** | Shrinks weights | Most nets | `weight_decay=1e-4` to `1e-2` | Stable, scale-aware; use **AdamW** or SGD+wd. |
| **L1** | Makes weights zero | Sparse features, feature selection | `λ1` small: `1e-6`–`1e-4` | Can hurt accuracy if too strong. |
| **Elastic Net** | Mix of L1+L2 | Want small+ sparse | `λ`, `l1_ratio` (0.1–0.5) | Often easier to tune than pure L1. |
| **Dropout** | Drops units at train time | Dense layers, some CNN heads | `p=0.1–0.3` (shallow), `0.3–0.5` (deep FC) | Use **inverted dropout** (scale by `1/(1-p)` at train). Off at eval. |
| **Label smoothing** | Soft targets reduce over-confidence | CE with softmax | `ε=0.05–0.1` | Helps calibration; also mild reg. |
| **Data augmentation** | More varied inputs | Vision, audio, text | Basic flips/crops; RandAug/AutoAug | Increases data size “for free”. |
| **Mixup / CutMix** | Blend inputs & labels | Vision, tabular (mixup) | `α=0.2–0.4` (Beta) | Strong regularizer; improves robustness. |
| **Early stopping** | Stop when val stops improving | Any | `patience=5–10`, restore best | Simple, powerful; always safe. |
| **BatchNorm / LayerNorm** | Normalizes hidden activations | Deep nets | default settings | Not a penalty, but reduces overfit often. Don’t decay γ/β. |
| **Weight noise / Gaussian noise** | Adds noise to weights/inputs | Small data | noise std small (e.g., 0.01) | Acts like Tikhonov reg. |
| **Stochastic depth / DropPath** | Randomly skip blocks | Deep ResNets/Transformers | drop rate grows with depth | Speeds and regularizes very deep nets. |
| **Max-norm constraint** | Clamp `||w||` to a bound | Some CNN/FC nets | `||w||₂ ≤ c` (e.g., 3.0) | Enforce small weights explicitly. |
| **Spectral norm** | Limit layer Lipschitz | Stability/robustness | default from library | Advanced; slower. |
| **SWA / EMA (weight averaging)** | Average weights over time | Any | SWA last 20–30% epochs; EMA 0.999 | Flatter minima, better generalization. |

---

## 4) Classic ML knobs (not NN)

| Model | Regularizer / knob | Effect | Good starts | Tips |
|---|---|---|---|---|
| **Linear/Logistic (Ridge)** | L2 (`alpha`) | Shrinks coefficients | `alpha=1.0` (scale features first) | Use CV to choose `alpha`. |
| **Linear/Logistic (Lasso)** | L1 (`alpha`) | Sparsity | small `alpha` | Can zero useful features if too strong. |
| **Elastic Net** | `alpha`, `l1_ratio` | Mix L1+L2 | `alpha=0.1–1.0`, `l1_ratio=0.1–0.7` | Robust default when unsure. |
| **SVM (linear/RBF)** | `C` (inverse of reg) | Smaller `C` = more reg | `C=1.0` | Scale features; tune `C` (+ `γ` for RBF). |
| **k-NN** | `n_neighbors` | Larger k = smoother | `k=5–15` | Scale features; odd k for binary. |
| **Trees** | `max_depth`, `min_samples_leaf` | Limit complexity | depth 3–10 | No scaling needed. |
| **XGBoost/LightGBM** | `max_depth`, `min_child_weight`/`min_data_in_leaf`, `subsample`, `colsample_bytree`, `reg_alpha` (L1), `reg_lambda` (L2) | Reduce variance | depth 4–10; subsample 0.8; colsample 0.8 | Lower `learning_rate`, raise `n_estimators` for smoother fits. |

---

## 5) When to use what (quick rules)

- **Small data, complex model:** add more reg: **L2 + dropout + early stop + aug**.
- **Large data:** mild reg: **L2 + early stop**; stronger aug if images/audio.
- **Model over-confident (peaky softmax):** **label smoothing** or **mixup**.
- **Weights explode / sharp minima:** **weight decay**, **SWA/EMA**, **smaller LR**.
- **Sparse high-dim:** try **L1/Elastic Net**.
- **Transformers / ResNets:** **AdamW (wd=0.01)**, **DropPath/Stochastic Depth**, **label smoothing**.

---

## 6) Tuning cheats

- **Weight decay (AdamW):** start `0.01` (vision, transformers), `1e-4` (small MLP/CNN); search ×/÷10.
- **Dropout p:** search `0.1, 0.2, 0.3, 0.5`. Too high ⇒ underfit.
- **Label smoothing ε:** `0.05–0.1`. Too high ⇒ hurts accuracy.
- **Mixup α:** `0.2–0.4`. Lower if classes very similar.
- **Early stop patience:** `5–10` epochs; **restore best** weights.
- **Elastic Net:** grid over `alpha ∈ {1e-3…1e+1}`, `l1_ratio ∈ {0.1,0.5,0.9}`.

---

## 7) Good patterns (recipes)

- **Vision CNN (image classification):**  
AdamW `lr=3e-4`, `wd=0.01`; **RandAug**; **label smoothing 0.1**; **Dropout 0.2** on head; **early stop**; optional **SWA** last 30%.
- **Tabular MLP (small data):**  
Z-score → AdamW `wd=1e-4`; **Dropout 0.2–0.5** on hidden; **L2 1e-4**; **early stop**.
- **Logistic regression (imbalanced):**  
Standardize → **Elastic Net** via CV; add **class weights**; threshold tune on PR-curve.
- **XGBoost:**  
`max_depth=6–8`, `min_child_weight=1–5`, `subsample=0.8`, `colsample_bytree=0.8`, `reg_lambda=1`, `reg_alpha=0–1`, `eta=0.05`, large `n_estimators`, early stop.

---

## 8) Dropout in one minute
- Train: each unit kept with prob `q=1-p`. Output is scaled by `1/q` (**inverted dropout**).
- Eval: no dropout, no scaling.  
This keeps the **expected activation** the same at train and eval.

---

## 9) Label smoothing (CE)
One-hot `y` becomes `y* = (1-ε) y + ε/K`.  
Use normal cross-entropy with `y*`. It lowers over-confidence and adds a small, constant push toward uniform.

---

## 10) Overfit vs underfit signs

| Symptom | Likely issue | Fix first |
|---|---|---|
| Train ↓, Val ↑ | Overfit | More **reg** (wd↑, dropout↑), **aug**, **early stop**, model simpler |
| Train ≈ Val but high | Underfit | Bigger model, **train longer**, **LR tune**, **less reg** |
| Train stuck, Val bad | Opt problem | **LR schedule**, **normalization**, **init**, **wd tune** |

---

## 11) Common pitfalls

- Decaying **biases/BN** hurts; turn off weight decay for them.
- Too strong **dropout** or **L1** ⇒ underfit fast.
- **Feature scaling** missing ⇒ L1/L2 behave oddly; always scale linear models and MLP inputs.
- **Early stopping without restore** ⇒ you keep a worse checkpoint.
- Augment **train only**; never augment validation/test.

---

## 12) Short math / gradients

| Penalty | Term | Gradient wrt `W` |
|---|---|---|
| L2 | `(λ2/2)||W||₂²` | `λ2 * W` |
| L1 | `λ1 ||W||₁` | `λ1 * sign(W)` (subgrad) |
| Elastic Net | `λ2 L2 + λ1 L1` | `λ2 * W + λ1 * sign(W)` |

**AdamW vs L2:** AdamW uses `W := W - η*∇W L_data - η*λ2 * W` (decoupled). This is better than mixing L2 into the adaptive gradient.

---

## 13) Checklists

**Before training**
- [ ] Scale numeric features where needed.
- [ ] Pick base model size that trains at all.
- [ ] Choose metric and validation split (or CV).

**Add regularization**
- [ ] Turn on **weight decay** (AdamW/SGD+wd).
- [ ] Add **dropout** on dense layers / heads.
- [ ] Add **label smoothing** for softmax CE.
- [ ] Set up **early stopping** (restore best).

**If still overfitting**
- [ ] Add **data aug** (stronger if images/audio).
- [ ] Try **mixup/CutMix** (vision) or **noise**.
- [ ] Raise `wd` a bit or `p_dropout` a bit.
- [ ] Consider **smaller model** / **stochastic depth**.

**If underfitting**
- [ ] Lower `wd` / `p_dropout`.
- [ ] Increase width/depth a bit.
- [ ] Train longer; try LR schedule.

---

## 14) Quick glossary
- **Weight decay:** another name for L2 on weights.
- **SWA/EMA:** weight averaging over time.
- **Stochastic depth / DropPath:** randomly skip blocks at train.
- **Max-norm:** cap the norm of each weight vector.

---

## 15) Summary
- Start simple: **AdamW + small weight decay + early stopping**.
- Add **dropout** on dense parts; use **label smoothing** for softmax.
- Use **data augmentation**; try **mixup** for vision.
- Tune a little: decay (×/÷10), dropout (0.1–0.5), smoothing (0.05–0.1).
- Keep an eye on **val curves**; **restore best**; avoid decaying biases/BN.

