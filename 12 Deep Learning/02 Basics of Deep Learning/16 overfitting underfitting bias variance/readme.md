# overfitting_underfitting_bias_variance

## 1) Quick meanings
- **Overfitting**: model learns training data too closely; fails on new data.
- **Underfitting**: model too simple or trained poorly; fails on both train and test.
- **High bias**: wrong assumptions / too simple; error stays high.
- **High variance**: model too flexible; results change a lot across samples.

---

## 2) How to spot (using train/validation curves)
| Pattern (loss ↓ is good) | Train loss | Val loss | Val metric | Name | What it means |
|---|---:|---:|---:|---|---|
| Both high, both flat | high | high | poor | Underfit (high bias) | Model too simple or learning too slow |
| Train ↓ low, Val stays high | low | high | poor | Overfit (high variance) | Memorizing, not generalizing |
| Train ↓ and Val ↓ then Val ↑ | low | first ↓ then ↑ | peak then drop | Overfit starting | Stop early or regularize |
| Both ↓ and close | low | low | good | Good fit | Keep going or stop early |
| Very noisy Val curve | low | zig-zag | unstable | High variance / LR too high | Reduce LR, add regularization |

---

## 3) Fast fixes (pick from top of each column first)
| Problem | Fast fixes | Next fixes | Last resort |
|---|---|---|---|
| Underfitting (high bias) | Increase model capacity (more layers/units); train longer; raise LR a bit | Better features; reduce regularization (smaller weight decay/dropout) | Change architecture |
| Overfitting (high variance) | More data or stronger augmentation; more regularization (weight decay, dropout); early stopping | Lower model capacity; label smoothing; mixup/cutmix (vision) | Gather more labeled data |
| Noisy / unstable training | Lower LR; add warmup; gradient clipping | Normalize features; smaller batch; check preprocessing | Rethink loss/architecture |

---

## 4) Bias–variance in one line
- Expected squared error: `E[(y − ŷ)^2] = Bias^2 + Variance + irreducible noise`.
- **Bias** comes from a model too simple.  
- **Variance** comes from a model too flexible or data too small.  
- Goal: **low total**, not zero of each. Use enough capacity + regularization + data.

---

## 5) Checklist (debug in this order)
- [ ] **Data sanity**: correct labels, no leakage, splits truly separate, same preprocessing for train/val/test.
- [ ] **Scale/normalize features** (tabular) or use proper input pipelines (vision/audio/NLP).
- [ ] **Loss/activation match** (e.g., sigmoid+BCE, softmax+CE, linear+MSE).
- [ ] **Learning rate** picked by LR range test; warmup if needed.
- [ ] **Batch size** reasonable (32–256); try smaller if unstable.
- [ ] **Regularization** set (weight decay, dropout, data aug, early stop).
- [ ] **Monitor curves** (train vs val loss/metric) every epoch.
- [ ] **Seed and logs** saved for repeat runs.

---

## 6) Regularization toolbox (what, knob, quick default)
| Method | What it does | Knob(s) | Quick default |
|---|---|---|---|
| Weight decay (L2) | Shrinks weights | `wd` | 1e-4 (vision SGD), 0.01 (AdamW Transformers) |
| Dropout | Randomly zero activations | `p` | 0.1–0.5 (start 0.2–0.3) |
| Data augmentation | More variety from images/audio/text | aug strength | Start light, grow until val drops |
| Early stopping | Stop when val stops improving | patience | 5–10 epochs (or steps window) |
| Label smoothing | Softer targets | ε | 0.05–0.1 (classification) |
| Mixup/CutMix (vision) | Blend samples/labels | α | 0.2 (mixup), 1.0 (CutMix) |
| Noise injection | Add noise to inputs/weights | σ | small (e.g., 0.01) |
| DropPath/StochasticDepth | Randomly skip blocks | rate | 0–0.2 (modern vision nets) |

---

## 7) Data issues to watch
- **Leakage**: test info in train path (features, time, IDs). Fix splits and pipelines.
- **Bad labels**: high train loss floor; check with small training subset (below).
- **Class imbalance**: use class weights, focal loss, or balanced sampling.
- **Shift**: train and test distributions differ; align preprocessing or adapt.

---

## 8) Two quick tests (cheap and strong)
1) **Overfit a tiny subset** (e.g., 100 samples). If it cannot hit near-zero train loss, the model/optimizer/loss pipeline is wrong.  
2) **Shuffle labels** and train. If accuracy stays high, leakage or bug.

---

## 9) Learning curves (what to change)
| Observation | Likely cause | Try |
|---|---|---|
| Train↑ Val↑ both poor | Bias | Bigger model, train longer, raise LR slightly |
| Train↑ good, Val bad | Variance | More regularization, more data/aug, earlier stop |
| Train good, Val noisy | Variance / LR high | Lower LR, grad clip, larger batch or EMA |
| Val best early | Overfit | Early stopping, stronger reg |
| Both plateau early | Too small LR or vanishing grads | LR range test, use warmup+cosine, check init/normalization |

---

## 10) Domain hints
- **Vision**: augment (flips, crops, color jitter), weight decay, label smoothing, mixup/CutMix, cosine LR; watch for over-aug hurting val.
- **NLP**: small LR with warmup, weight decay (AdamW), dropout in attention/MLP, layer-wise LR decay; check tokenization and sequence lengths.
- **Tabular**: feature scaling, target transform if skewed, strong regularization, early stop; try tree models as baseline.

---

## 11) Model capacity guide (simple rule)
- Start with a model a bit **bigger** than you think. If it overfits: add regularization or shrink. If it underfits even with near-zero reg: grow.

---

## 12) Early stopping recipe
- Track **val loss** (or metric).  
- Keep the best weights.  
- Stop if no improvement for `patience` epochs (e.g., 10).  
- Combine with LR decay after plateau.

---

## 13) Small math (loss + penalties)
- Total objective: `L_total = L_data + λ2 * ½||W||² + λ1 * ||W||₁`.  
- L2 (weight decay) reduces variance; L1 promotes sparsity.

---

## 14) Simple workflows
**If underfitting**: check data/activations → increase LR a bit → train longer → bigger model → reduce reg.  
**If overfitting**: add/strengthen reg (wd, dropout, aug, smoothing) → earlier stop → maybe smaller model → more data.  
**If unstable**: lower LR, add warmup and grad clipping, check normalization and initialization.

---

## 15) One-page memory
- Underfit = both poor → add capacity or LR/time.  
- Overfit = train good, val bad → more regularization/data/early stop.  
- Balance bias and variance; aim for lowest **val** loss.  
- Always sanity-check data and try to overfit a tiny subset.