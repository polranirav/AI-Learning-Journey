# Feature Scaling — Simple, One-File Guide (featurescalling.md)

Feature scaling puts numeric features on comparable ranges so models train faster, behave stably, and make fair distance/gradient comparisons.

---

## Why scale?
- **Faster training:** smoother loss for gradient methods.
- **Stable math:** fewer overflows/underflows; nicer learning rates.
- **Fair distances:** needed for k-NN, k-means, SVM (RBF), PCA, cosine.
- **Regularization behaves well:** penalties treat features evenly.

**Often not needed:** tree models (Decision Tree, Random Forest, XGBoost/LightGBM) care about splits, not distances. You can skip scaling there (but scaling doesn’t hurt much).

---

## Methods at a glance

| Method | Formula (per feature) | Output range | Use when | Outlier sensitivity | Sparse OK?* | Notes |
|---|---|---|---|---|---|---|
| **Standardization (Z-score)** | `(x - mean) / std` | ~N(0,1) if near-normal | Default for many models | Medium | Yes (set `with_mean=False`) | Works well for linear models, neural nets, PCA. |
| **Min–Max [0,1]** | `(x - min) / (max - min)` | `[0,1]` | Need bounded range or image pixels | **High** | Yes | Simple; very sensitive to extreme values. |
| **Robust (median/IQR)** | `(x - median) / IQR`, `IQR=Q3-Q1` | centered, not bounded | Heavy outliers / skew | **Low** | Yes (no centering) | Good when few huge values exist. |
| **MaxAbs** | `x / max_abs` | `[-1,1]` | Sparse data | Medium | **Yes** | Preserves sparsity; no centering. |
| **Unit Vector (L2 norm)** | `x / ||x||₂` (row-wise) | length = 1 | Cosine/SVM-lin text vectors | Medium | Yes | Often used after TF-IDF. |
| **Log / log1p** | `log(x)` or `log1p(x)` | shrinks large values | Counts, positive skew | — | No (densifies) | Use `log1p` for zeros; combine with Z-score. |
| **Power (Box-Cox / Yeo-Johnson)** | learned monotonic transform | variance stabilizing | Non-normal, skewed | Medium-Low | No | YJ handles zeros/negatives; then Z-score. |
| **Quantile / Rank Gaussian** | map quantiles → target dist | chosen (e.g., normal) | Weird/heavy tails | Low | No | Very robust; breaks linearity between samples. |

\*Sparse OK? = can be applied without turning sparse matrices dense.

---

## Pick the scaler (quick rules)

- **General tabular, few outliers:** **Standardization**.
- **Many outliers / long tail:** **Robust** (optionally clip) → then **Standardization**.
- **Counts (0,1,2,..), heavy skew:** **log1p** → **Standardization**.
- **Sparse bag-of-words / TF-IDF:** usually already scaled; maybe **MaxAbs** or **L2** row-norm.
- **Image pixels:** divide by 255 (→ [0,1]); sometimes channel-wise **Standardization**.
- **Time series:** scale using **training-only** history; never peek into the future.

---

## Where scaling fits (no leakage)

1) **Split** your data (train/valid/test).  
2) **Fit** scaler on **train only** (compute mean/std, min/max, etc.).  
3) **Transform** train, valid, test with the **same** fitted scaler.  
4) Save scaler params to apply on new data; for regression, inverse-transform predictions if you scaled **y**.

**Time series:** fit on past window only; transform each next step with scalers fitted on earlier data.

---

## Formulas (tiny examples)

- **Standardization**  
  Suppose values: 8, 10, 14. Mean = 10.67, Std ≈ 2.49.  
  Scaled(14) = (14 − 10.67) / 2.49 ≈ **1.34**.

- **Min–Max [0,1]**  
  Min = 8, Max = 14. Scaled(14) = (14 − 8) / (14 − 8) = **1.0**.

- **Robust (median/IQR)**  
  Values: 2, 3, 100. Median = 3, Q1=2.5, Q3=51.5 → IQR=49.  
  Scaled(100) = (100 − 3) / 49 ≈ **1.98** (less extreme than Min–Max).

---

## Model notes

- **Distance-based:** k-NN, k-means, SVM (RBF), DBSCAN → **must scale**.  
- **Linear models:** Logistic/Linear Regression, Lasso/Ridge → **scale** (penalties fair).  
- **Neural nets:** scale inputs (zero-mean, unit-std).  
  - **BatchNorm/LayerNorm** do **not** replace input scaling; they stabilize **hidden** layers.  
- **Trees/boosting:** can skip scaling.

---

## Targets (y)

- **Regression:** scaling **y** can help (e.g., log1p counts, Z-score target).  
  - Remember to **inverse-transform** predictions.  
- **Classification:** do **not** scale labels.

---

## Handling special cases

- **Missing values:** impute **before** scaling (mean/median or model-based).  
- **Outliers:** clip to reasonable bounds **after** fitting scaler on train (e.g., clip Z-scores to ±5).  
- **Mixed units:** scale numeric; **do not scale** one-hot categories.  
- **Sparse matrices:** avoid centering (keeps sparsity). Use **MaxAbs** or Standardization with `with_mean=False`.

---

## Simple checklists

**Before scaling**
- [ ] Split data (train/valid/test) or set up time-series splits.
- [ ] Decide feature types: numeric (scale), categorical (encode), text (TF-IDF), images (divide by 255).
- [ ] Handle missing values.

**Choose method**
- [ ] Mostly clean, normal-ish → **Standardization**.  
- [ ] Heavy outliers → **Robust** (maybe clip) → optional **Standardization**.  
- [ ] Counts/heavy skew → **log1p** → **Standardization**.  
- [ ] Sparse → **MaxAbs** or Z-score without centering.

**Apply correctly**
- [ ] Fit scaler **on train only** (no leakage).  
- [ ] Reuse same scaler for valid/test.  
- [ ] Save scaler with the model.

**Sanity checks**
- [ ] After scaling, each numeric feature has reasonable center/spread.  
- [ ] No NaNs created; no overflow/inf.  
- [ ] For time series, no future info leaked.

---

## Small “recipes” you can reuse

- **Tabular (mixed, with outliers):**  
  Impute → RobustScaler (per feature) → (optional) clip Z to ±5 → model.

- **Counts (Poisson-like):**  
  Impute zeros → log1p → Standardize → model.

- **Text (sparse):**  
  TF-IDF → (optional) L2 row-normalize → linear classifier/SVM.

- **Images:**  
  `x = x / 255.0` → per-channel mean/std Standardization → CNN.

- **Time series regression:**  
  Fit scaler on train window → transform rolling windows → model → inverse-scale `ŷ`.

---

## FAQ (quick answers)

- **Do I scale one-hot features?** No. They’re already 0/1.  
- **Do I scale booleans?** Usually no (keep 0/1).  
- **Different scalers per feature?** Yes; pick what fits each feature’s distribution.  
- **Can I chain transforms?** Yes (e.g., log1p → Z-score).  
- **Why does validation drop after scaling?** Check for leakage or different scaler fitted on val/test by mistake.

---

## Mini math corner (stable forms you’ll see)
- Z-score uses running `(mean, std)`; for streaming you can update them online (Welford’s algorithm).  
- Soft models (logistic/NNs) like inputs roughly **zero-mean** with **unit variance**.

---

## Short glossary
- **Leakage:** using future/test info when fitting transforms.  
- **IQR:** interquartile range = Q3 − Q1.  
- **Whitening:** decorrelating and scaling to unit variance (e.g., PCA + scale). Often overkill.

---

## Summary
- Pick **Standardization** by default.  
- Use **Robust** (or **log1p**) when outliers/skew dominate.  
- Always **fit on train, apply everywhere**.  
- For distance/gradient-heavy models, **scaling is mandatory**.