# data_augmentation.md

## 1) What it is
- Make **new training samples** from old ones by safe changes (flip, crop, noise, etc.).
- Goal: **better generalization**, **less overfitting**, **stronger models** without new labels.
- **Only for training**. Do **not** augment validation/test (except optional TTA; see §11).

---

## 2) Core rules (do these first)
- **After split**: split data → then augment **train** only.
- **Label stays valid**: if you change the input, fix its label/targets too (e.g., boxes, masks, keypoints).
- **Random each time**: sample new augment params every epoch/batch.
- **Keep it realistic**: do not break task truth (e.g., don’t rotate digits 180° for “6/9”).
- **Start light** → add more until validation gets worse.
- **Log the pipeline** and set a seed for reproducibility.

---

## 3) Quick picker (by problem)
| Problem | Use first | Maybe add later | Avoid |
|---|---|---|---|
| Image classification | Flip, random crop+resize, color jitter (light) | Mixup/CutMix, RandAugment, Blur/Noise | Heavy rotation for orientation-sensitive classes |
| Object detection | Horizontal flip, small scale/translate, mosaic (advanced) | Color jitter (light), CutMix (bbox-aware) | Crops that cut out the target without label update |
| Segmentation | Flip, crop, scale; apply **same** transform to mask | Elastic/affine, color jitter | Mismatch between image/mask transforms |
| NLP text classification | Word dropout, synonym/EDA (light) | Back-translation, paraphrase | Heavy changes that flip sentiment/meaning |
| Audio (speech/keyword) | Time shift, noise, SpecAugment (time/freq mask) | Pitch/tempo (small), reverb | Large tempo/pitch if label depends on it |
| Tabular (imbalance) | Class weights, **SMOTE** (train only) | Mixup, noise on numeric cols | Random shuffles that break feature meaning |
| Time series | Window crop, jitter (small), scaling, time-warp (small) | Permute segments (task-aware) | Leaking future info across time |

---

## 4) Vision: common ops (safe ranges)
| Op | What it does | Typical knobs | Safe start |
|---|---|---|---|
| Horizontal flip | Mirror image | p | p = 0.5 |
| Random crop + resize | Crop patch then resize back | scale, ratio | scale 0.8–1.0; keep aspect near 1 |
| Rotate | Rotate a bit | degrees | ±10° (avoid for text/medical if orientation matters) |
| Translate | Shift x/y | px or pct | up to 10% |
| Scale | Zoom in/out | factor | 0.9–1.1 |
| Color jitter | Change brightness/contrast/saturation/hue | ranges | ±0.2 (hue ±0.05) |
| Gaussian blur | Blur lightly | kernel, σ | small (σ ≤ 1.0) |
| Noise | Add small Gaussian/Poisson | σ | σ ≈ 5/255 |
| Cutout/Erase | Zero random square | size, count | 1–2 holes, 10–20% side |
| Mixup | Blend two images+labels | α | α = 0.2 |
| CutMix | Cut patch from B into A, mix labels by area | α | α = 1.0 |
| RandAugment | N random ops with strength | N, M | N=2, M=7–9 |
| AugMix | Mix several light augmentations | prob, width | defaults |

**Tips**
- For detection/segmentation: update **bboxes/masks/keypoints** after any spatial change.
- Keep **test-time** resizing/normalization identical to training preprocessing (before aug).

---

## 5) Text (NLP): simple ops
| Op | What it does | Notes |
|---|---|---|
| Word dropout | Delete a few non-key words | small rate 0.05–0.1 |
| Synonym replace (EDA) | Swap with synonym | use domain-safe lists |
| Random swap/insert (EDA) | Reorder or insert | keep small (1–2 edits) |
| Back-translation | Translate out-and-back | good but slower |
| Paraphrase (model) | Generate variant sentence | check label still correct |
| Char noise | typos, keyboard noise | for robust OCR/ASR text |

**Guardrails**
- Keep **entity labels** consistent in NER (do not touch labeled spans unless you update tags).
- Do **not** change words that flip label (e.g., “good” → “bad” in sentiment).

---

## 6) Audio: simple ops
| Op | What it does | Safe start |
|---|---|---|
| Time shift | Roll waveform | ≤ 10% length |
| Add noise | Background noise / SNR control | SNR 10–30 dB |
| Time mask (SpecAugment) | Zero time bands | width ≤ 10% |
| Freq mask (SpecAugment) | Zero mel bands | width ≤ 10% |
| Pitch shift | Semitone change | ±1 semitone |
| Tempo change | Speed up/down | ±5% |
| Reverb/RIR | Room effect | light preset |

---

## 7) Tabular & time series
- **Tabular (numeric)**: small Gaussian noise on scaled features; **SMOTE** or class-weight for imbalance; **Mixup** can help.
- **Categorical**: do **not** randomize categories; you may drop rare noisy rows, not mutate labels.
- **Time series**: crop windows, jitter, scale, time-warp (small), **never leak future**. Keep time order.

---

## 8) Mixup & CutMix (quick math)
- **Mixup**:  
  `λ ~ Beta(α, α)`  
  `x' = λ x_i + (1−λ) x_j`  
  `y' = λ y_i + (1−λ) y_j`  (use one-hot or soft labels)
- **CutMix**:  
  Cut rectangle R from `x_j` into `x_i`.  
  `λ = area(outside R) / total_area`  
  `y' = λ y_i + (1−λ) y_j`
- Start with **mixup α=0.2** (cls). For detection/segmentation use toolkit support that adjusts boxes/masks.

---

## 9) Tuning plan (fast)
1) Start with **flip + crop + light color jitter** (vision) or **SpecAugment** (audio) or **word dropout** (NLP).  
2) Watch **val loss/metric**. If overfitting: increase aug strength or add mixup/CutMix.  
3) If training becomes unstable: lower aug strength, lower LR a bit.  
4) Keep the **best policy** (smallest val loss). Use **early stopping**.

---

## 10) Debug checklist
- [ ] Augment **after** train/val/test split.
- [ ] Apply **same geometry** to image and its **labels** (boxes, masks, keypoints).
- [ ] Keep **class balance** in minibatches even with heavy aug.
- [ ] Keep **pixel/feature scaling** consistent before/after aug.
- [ ] Log **probabilities and ranges** for each op.
- [ ] Try **no-aug baseline** and **tiny-aug** to confirm gains.
- [ ] Overfit on **tiny subset**; if you still can’t fit, pipeline has a bug.

---

## 11) Test-Time Augmentation (TTA) (optional)
- Run model on a few simple transforms (e.g., original + horizontal flip).  
- **Average** predictions (or majority vote).  
- Keep TTA **small** to avoid artifacts; only if it **improves** validation.

---

## 12) Small recipes
**Image classification (general)**  
- Resize → random crop (scale 0.8–1.0) → horizontal flip (p=0.5) → color jitter (±0.2) → normalize  
- If overfitting: add mixup (α=0.2) or RandAugment (N=2, M=7).

**Object detection (COCO-like)**  
- Mosaic/large-scale jitter (toolkit) → random horizontal flip → color jitter (light) → box-safe crop/resize  
- Validate that boxes are inside image and non-empty.

**Text sentiment**  
- Word dropout (0.05) → light EDA synonym swap (1 edit)  
- Back-translation if you can afford it.

**Speech commands**  
- Time shift (≤10%) → noise (SNR ≥15 dB) → SpecAugment (time/freq mask width ≤10%).

**Tabular imbalance**  
- Use **class weights** or **SMOTE** (train only) → optional mixup (α=0.2) on numeric features.

---

## 13) When to avoid
- Orientation matters (medical, OCR, road signs): avoid rotation/flip that change meaning.  
- Color is label (ripe/unripe): limit color jitter.  
- Small objects near borders: avoid strong crops without careful rules.  
- Legal/ethical: don’t synthesize data that misleads labels.

---

## 14) Minimal code sketch (pseudocode)
- for epoch:
- for batch in train_loader:
- x, y = batch
- x_aug, y_aug = augment(x, y, policy)
- loss = model.loss(x_aug, y_aug)
step(loss)

- `augment` is **random**, **stateless**, and updates labels when needed.

---

## 15) One-page memory
- Train-only, after split.  
- Keep labels consistent.  
- Start light; add more if overfitting.  
- Mixup/CutMix are strong, use modest α.  
- Validate each change; stop if val drops.