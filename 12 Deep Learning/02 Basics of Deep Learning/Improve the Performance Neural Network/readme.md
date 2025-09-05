# How to Improve a Neural Network (Simple, Practical README)

This single file gives you clear, step-by-step ways to make your neural network perform better. Keep the language simple, try these ideas in order, and note what actually helps on your dataset.

---

## 1) Start With a Clean Setup

- **Fix random seeds** (so results are repeatable).
- **Standardize inputs** (zero mean, unit variance) or **normalize** to [0,1].
- **Split data once**: train / validation / test (e.g., 70/15/15). Do not touch test until the very end.
- **Baseline first**: a small model + default optimizer + default learning rate. Record accuracy/loss.

---

## 2) Improve Your Data First (Biggest Wins)

- **Get more data** if possible.
- **Data augmentation** (images: flips, crops; text: small paraphrases; audio: noise/time-shift; tabular: careful—prefer gathering more real data).
- **Fix labels** (spot mislabeled examples).
- **Handle class imbalance** (class weights, focal loss, or balanced sampling).
- **Remove leakage** (no future info in features; no duplicates across splits).

---

## 3) Pick a Good Architecture (Depth > Width, then adjust)

- Prefer **deeper models with moderate layer sizes** over one shallow, huge layer.
- **Start small**, then grow depth/width until you begin to overfit, then dial back a bit.
- **Transfer learning** when you have limited data:
  - Load a pretrained model.
  - **Freeze early layers**, **fine-tune later layers**.
- **Activation choices**:
  - Use **ReLU/Leaky ReLU/GELU** in hidden layers (avoid pure sigmoid/tanh in deep nets).
  - Final layer depends on task:  
    - Regression → linear;  
    - Binary classification → sigmoid;  
    - Multi-class → softmax.
- **Initialization**:
  - **He/Kaiming** for ReLU-like activations.
  - **Xavier/Glorot** for tanh/linear.

---

## 4) Choose the Right Loss & Metrics

- **Binary classification** → Binary cross-entropy (BCE).  
- **Multi-class** → Categorical cross-entropy (one-hot) or sparse categorical cross-entropy (int labels).  
- **Regression** → MSE or Huber (Huber is robust to outliers).  
- Track a **task-relevant metric** (AUC/F1 for imbalance, MAE for interpretability, etc.).

---

## 5) Optimize Smartly (Learning Rate is King)

- **Optimizers to try (in order)**:
  1) **Adam** (strong default),  
  2) **RMSprop**,  
  3) **SGD + Momentum/Nesterov** (great with a well-tuned LR schedule).
- **Find a good learning rate**:
  - Use an **LR finder** (increase LR during a short warm-up run, choose the largest LR before loss blows up).
- **Use LR schedules**:
  - **Warm-up** (start small, ramp up for a few epochs).
  - **Step decay**, **Cosine decay**, or **Reduce-on-plateau** (auto-lower LR when val loss stops improving).
- **Batch size**:
  - Small (e.g., 16–64) often **generalizes better**, big batches **train faster** if you **warm up LR**.
- **Gradient tricks**:
  - **Gradient clipping** (e.g., clip norm=1.0) if gradients explode.
  - **Mixed precision** (if hardware allows) for speed and larger effective batch.

---

## 6) Regularize to Beat Overfitting

- **Early stopping** (monitor validation loss/metric; stop after patience N epochs).
- **Weight decay (L2)** (e.g., 1e-4 to 1e-2; AdamW has built-in weight decay).
- **Dropout** (e.g., 0.1–0.5; start small and place after dense/conv blocks).
- **Batch/Layer normalization** (stabilizes training and helps generalization).
- **Label smoothing** (e.g., 0.05–0.1) for classification.
- **Data augmentation** (mentioned above) is also regularization.

---

## 7) Reliable Training Workflow (Recipe)

1. **Baseline**: Small model + Adam + LR 1e-3 + batch size 32, 20–30 epochs.
2. **Watch curves**:
   - If **train ↓ & val ↓** → good, keep going.  
   - If **train ↓ & val ↑** → overfit → add regularization (dropout/L2/augmentation) or reduce capacity.  
   - If **train flat** → increase capacity, try better init/activations, raise LR a bit, or switch optimizer.
3. **Tune LR**:
   - Try 1e-4, 3e-4, 1e-3, 3e-3. Add **warm-up** and a **cosine/plateau schedule**.
4. **Tune capacity**:
   - Add layers or units until slight overfit appears, then regularize to pull back.
5. **Normalization**:
   - Add **BatchNorm/LayerNorm** between dense/conv + activation.
6. **Regularize**:
   - Add **weight decay**, **dropout**, **augmentation**, **label smoothing**.
7. **Batch size**:
   - If GPU RAM allows, try **larger batch + LR warm-up** for speed; otherwise keep 32–64.
8. **Callbacks**:
   - **EarlyStopping** (patience 5–10), **ModelCheckpoint** (best val metric), **ReduceLROnPlateau**.
9. **Diagnose vanishing/exploding gradients**:
   - Use ReLU-family activations; **He init**; **BatchNorm**; **clip grads** if needed.
10. **Final model**:
   - Retrain on **train+val** with best settings, then evaluate once on **test**.

---

## 8) Quick Checklists

### Underfitting (model too simple / learning too slowly)
- Increase model **depth/width**.
- **Increase LR** a bit or switch optimizer.
- Train **longer** (with early stopping).
- **Reduce** regularization (dropout/L2).

### Overfitting (great on train, poor on val/test)
- Add/strengthen **dropout**, **L2/weight decay**, **augmentation**, **label smoothing**.
- Use **early stopping**.
- **Reduce** model size slightly.

### Unstable/Noisy training
- Lower **LR**; add **warm-up**; try **Adam**.
- Add **BatchNorm/LayerNorm**.
- **Clip gradients** (e.g., norm 1.0).

### Slow training
- Use **mixed precision**, **bigger batch + LR warm-up**, **lighter architecture**, **caching/num_workers** in dataloaders.

---

## 9) Common Pitfalls to Avoid

- **Data leakage** (accidentally giving future or label info).
- **Shuffling** off for training (should be on).
- **Metric mismatch** (optimize loss that doesn’t match your business metric—choose/track the right metric).
- **Unbalanced splits** (stratify classification splits).
- **Forgetting to standardize/normalize inputs**.

---

## 10) When You Have Little Data

- **Transfer learning** (use pretrained backbones).
- **Freeze most layers**, train only the head; then **unfreeze and fine-tune** with a small LR.
- **Heavy augmentation** + **strong regularization**.
- **Cross-validation** for reliable estimates.

---

## 11) Small, Sensible Default Hyperparameters

- Optimizer: **Adam** (β1=0.9, β2=0.999, eps=1e-8), **LR=1e-3** (then tune).
- LR schedule: **Warm-up 3–5 epochs**, then **cosine decay** or **reduce-on-plateau**.
- Batch size: **32 or 64** (try larger if GPU allows and use LR warm-up).
- Regularization: **Weight decay 1e-4**, **Dropout 0.1–0.3**, **Label smoothing 0.05** (classification).
- Init: **He/Kaiming** for ReLU-family.
- Activations: **ReLU/Leaky ReLU/GELU** hidden; **sigmoid/softmax/linear** output per task.
- Callbacks: **EarlyStopping**, **ModelCheckpoint**, **TensorBoard** logging.

---

## 12) Minimal Tuning Plan (Fast Path)

1) Run baseline; save metrics.  
2) Tune **LR** (+ schedule).  
3) Add **Batch/LayerNorm**.  
4) Increase **depth/units** until slight overfit appears.  
5) Add **weight decay, dropout, augmentation, label smoothing** to fix overfit.  
6) Try **Adam ↔ SGD+Momentum**; pick the best.  
7) If data is small → **transfer learning**.  
8) Lock settings; **retrain** on train+val; evaluate on **test** once.

---

## 13) Glossary (one-liners)

- **Early stopping**: Stop training when validation metric stops improving.  
- **Weight decay (L2)**: Penalizes large weights to reduce overfitting (AdamW implements this well).  
- **BatchNorm/LayerNorm**: Normalize activations to stabilize training.  
- **Gradient clipping**: Limit gradient size to prevent exploding updates.  
- **Label smoothing**: Soften targets slightly to improve calibration/generalization.  
- **Warm-up**: Start with a low LR, ramp up to target LR over a few epochs.  
- **Cosine decay**: Smooth LR decrease that often gives strong results.  
- **Transfer learning**: Start from a pretrained model; fine-tune for your task.

---

## 14) Troubleshooting by Symptoms

- **Training loss not decreasing at all** → LR too low/high, wrong loss, bug in labels, missing normalization.
- **Val loss much higher than train loss** → overfitting → add regularization/augmentation, reduce capacity.
- **Sudden loss spikes** → LR too high, exploding gradients → lower LR, add clipping, check batch norm.
- **Stuck accuracy around chance** → wrong labels, shuffled labels/features mismatch, output layer/loss mismatch.

---

## 15) Final Notes

- Change **one thing at a time** and log the result.  
- Keep runs organized (config file or experiment tracker).  
- The best recipe depends on **your data**: always validate with a proper split.