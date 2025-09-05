# Dropout — Simple, One-File Guide (dropout.md)

Dropout is a **regularization** method. During training it **randomly turns off** some neurons to prevent co-adaptation and overfitting. At inference, **nothing is dropped**.

---

## 1) Core idea (short)
- Train time: randomly keep each unit with prob `q = 1 - p` (where `p` is dropout rate).  
- Scale kept activations by `1/q` (**inverted dropout**) so expectations match.
- Test time: use the full network (no dropout, no scaling).
- Effect: behaves like averaging many thinned networks → better generalization.

---

## 2) How it works (math + tiny example)
Let activation vector be `a` (after nonlinearity). Let mask `m ~ Bernoulli(q)` applied element-wise.

Train step:
- `ã = (m ⊙ a) / q`         (inverted dropout; `⊙` = element-wise)
- Forward/backprop uses `ã`.

Test step:
- Use `a` as is (no mask, no scaling).

Expectation:
- `E[ã] = a`.  
Variance grows with `p`, so too much dropout can underfit.

**Mini numeric check (q=0.8, p=0.2):**  
If `a = [1.0, 0.5, 0.0, 2.0]`, a sample mask could be `m = [1, 0, 1, 1]`.  
Then `ã = [1/0.8, 0, 0/0.8, 2/0.8] = [1.25, 0.0, 0.0, 2.5]`.  
Average over many masks ≈ original `a`.

---

## 3) Where to use it
- **Dense (fully connected) layers:** main place; add after activation (e.g., ReLU).
- **Convolutional layers:** often lighter or use **spatial dropout** (drop whole feature maps).
- **RNNs/Transformers:** use **locked/variational dropout** (same mask across time) or built-in dropout in blocks; avoid dropping recurrent state each step unless using proper variants.
- **Input layer:** small rate can help (acts like data noise).

---

## 4) Good starting rates (rules of thumb)

| Layer / setting | Small model | Medium | Large / deep |
|---|---:|---:|---:|
| Dense hidden | 0.10–0.20 | 0.20–0.30 | 0.30–0.50 |
| CNN conv (standard) | 0.00–0.10 | 0.05–0.20 | 0.10–0.30 |
| CNN **spatial dropout** | 0.05–0.15 | 0.10–0.25 | 0.20–0.30 |
| RNN **locked** (between layers) | 0.10–0.30 | 0.20–0.40 | 0.30–0.50 |
| Input features | 0.00–0.05 | 0.00–0.10 | 0.05–0.10 |

Start low; raise if train ≪ val. If underfitting, lower `p`.

---

## 5) Variants you should know (one-liners)

- **Inverted Dropout (default):** scale by `1/q` at train; no scaling at test. Use this.
- **SpatialDropout / Dropout2D/3D:** drop entire conv channels (feature maps); keeps spatial consistency.
- **AlphaDropout (for SELU):** keeps mean/var for self-normalizing nets (SELU activations).
- **DropConnect:** drop **weights** instead of activations (stronger, slower).
- **Locked / Variational Dropout (RNN):** one mask per sequence (not per time step).
- **Stochastic Depth / DropPath:** randomly skip residual blocks/paths (very deep nets).
- **DropBlock (CNN):** drop contiguous spatial blocks (regularizes locality).

---

## 6) Placement tips

- Put dropout **after activation** (e.g., Linear → ReLU → Dropout).
- With **BatchNorm**: often **little or no dropout** is needed. If used, place **after** BN + activation: Linear → BN → ReLU → Dropout.
- In **residual blocks**: small dropout (or DropPath) between convolutions or on the residual branch; keep it light.
- Do **not** apply dropout at **test/eval**.

---

## 7) Training behavior you should expect

| Curve pattern | Meaning | What to do |
|---|---|---|
| Train loss ≪ Val loss | Overfitting | Increase `p`, add weight decay/augment, early stop |
| Train ≈ Val but both high | Underfitting | Decrease `p`, add capacity, tune LR/schedule |
| Train unstable, val noisy | Too much noise | Lower `p`, consider spatial/locked variants |

---

## 8) Small tuning recipe (fast)

1) Start **without** dropout; ensure it learns.  
2) Add **0.2** on dense head (classification) or **0.1** (regression).  
3) Watch val loss/metric 3–5 epochs.  
4) If overfit remains → raise to **0.3–0.5** gradually.  
5) For CNNs, switch to **spatial dropout** if feature maps overfit.  
6) For RNNs, use **locked dropout** between layers (e.g., 0.3).  
7) Combine with **weight decay** and **early stopping**.

---

## 9) With other regularizers (how they mix)

- **Weight decay (L2) + Dropout:** great combo; L2 smooths weights, dropout adds noise.  
- **Label smoothing + Dropout:** complementary for classification; reduces over-confidence.  
- **Data augmentation + Dropout:** recommended in vision/audio; tune `p` lower if aug is strong.  
- **BatchNorm + Dropout:** BN already stabilizes; use smaller `p` or skip.

---

## 10) Common pitfalls

- Using **classic dropout** (scale at test) instead of **inverted** → mismatch.  
- Applying dropout **before BN** → statistics get noisy. Prefer after BN+activation.  
- Setting `p` high everywhere (e.g., 0.5 in conv stack) → underfits.  
- Forgetting to **disable** dropout at evaluation/inference.  
- For sequences, changing mask **each time step** → harms memory. Use **locked** mask.

---

## 11) Short “how to implement” (pseudo-code, framework-agnostic)

Train mode:
    a = activation(linear(x))
    m = Bernoulli(q).sample_like(a)   # keep prob q = 1 - p
    a_tilde = (m * a) / q             # inverted dropout
    y = next_layers(a_tilde)

Eval mode:
    a = activation(linear(x))
    y = next_layers(a)                # no mask, no scaling

---

## 12) FAQ (quick)

- **Does dropout increase training time?** Slightly; noisy gradients may need a few more epochs.  
- **Use with residual nets?** Yes, but often **DropPath/Stochastic Depth** works better.  
- **Where not to use?** Very small datasets with tiny models can underfit; try L2 + early stop first.  
- **Calibration?** Dropout often improves calibration; label smoothing helps further.  
- **Bayesian view?** MC-Dropout approximates uncertainty by running multiple stochastic passes at test.

---

## 13) Tiny checklists

**Add dropout**
- [ ] Start on dense head (`p=0.2–0.3`).
- [ ] For CNNs, prefer **spatial dropout** (`p=0.1–0.3`).
- [ ] For RNNs, use **locked dropout** (`p=0.2–0.5`).
- [ ] Keep BN → ReLU → Dropout order.

**If still overfitting**
- [ ] Increase `p` slightly.
- [ ] Add/raise **weight decay**.
- [ ] Add **augmentation** (vision/audio).
- [ ] Turn on **early stopping** (restore best).

**If underfitting**
- [ ] Lower `p`.
- [ ] Add capacity or train longer.
- [ ] Tune learning rate/schedule.

---

## 14) One-screen summary

- **What:** Randomly drop activations at train; scale by `1/q`.  
- **Why:** Prevent co-adaptation; acts like model averaging.  
- **Where:** Dense heads (main), light in convs (spatial), locked in RNNs.  
- **How much:** 0.1–0.5 (dense), 0.05–0.3 (conv), 0.2–0.5 locked (RNN).  
- **With:** Weight decay, early stop, aug, (optionally) label smoothing.  
- **Watch for:** Underfit if `p` too high; wrong placement with BN; eval must disable dropout.