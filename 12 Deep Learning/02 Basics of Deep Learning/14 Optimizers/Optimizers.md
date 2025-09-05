# Optimizers 


- [0. Quick view](#0-quick-view)
- [1. Basics](#1-basics)
- [2. Optimizers (rules)](#2-optimizers-rules)
- [3. Side-by-side table](#3-side-by-side-table)
- [4. Good defaults](#4-good-defaults)
- [5. Learning-rate schedules](#5-learning-rate-schedules)
- [6. Batch size tips](#6-batch-size-tips)
- [7. Weight decay vs L2](#7-weight-decay-vs-l2)
- [8. Gradient clipping](#8-gradient-clipping)
- [9. Tuning steps](#9-tuning-steps)
- [10. Fix guide](#10-fix-guide)
- [11. Code (short)](#11-code-short)
- [12. FAQ](#12-faq)

---

## 0. Quick view
- Goal: lower the loss by moving weights.
- Need: gradients from backprop.
- Work unit: step on a mini-batch (e.g., 32/64/128).

---

## 1. Basics
- Symbols: `w` weight, `g` grad, `η` lr (learning rate), `ε` tiny, `μ` momentum, `β1/β2` Adam terms.
- Plain SGD idea: go **against** the gradient: `w ← w − η·g`.

---

## 2. Optimizers (rules)

> All updates are element-wise.

**SGD**
- Rule: `w ← w − η·g`
- Simple, needs a schedule.

**SGD + Momentum**
- Keep velocity: `v ← μ·v + g`
- Update: `w ← w − η·v`

**Nesterov (NAG)**
- Look ahead:
  - `v_prev ← v`
  - `v ← μ·v − η·g(w − μ·v_prev)`
  - `w ← w + v`

**Adagrad**
- Per-param rate shrinks:
  - `s ← s + g²`
  - `w ← w − η·g/(√s + ε)`

**RMSProp**
- Moving avg of `g²`:
  - `s ← ρ·s + (1−ρ)·g²`
  - `w ← w − η·g/(√s + ε)`

**Adadelta**
- Unit-free step:
  - `s ← ρ·s + (1−ρ)·g²`
  - `Δ ← − √(u+ε)/√(s+ε) · g`
  - `u ← ρ·u + (1−ρ)·Δ²`
  - `w ← w + Δ`

**Adam**
- Momentum + RMSProp + bias fix:
  - `m ← β1·m + (1−β1)·g`
  - `v ← β2·v + (1−β2)·g²`
  - `m̂ = m/(1−β1ᵗ)`, `v̂ = v/(1−β2ᵗ)`
  - `w ← w − η·m̂/(√v̂ + ε)`

**AdamW (Adam + decoupled decay)**
- Do Adam step, then decay:
  - `w ← w − η·λ·w` (after the Adam part)

**Nadam**
- Adam with Nesterov-style look ahead.

**AMSGrad**
- Adam with non-decreasing `v̂`:
  - `v̂_max ← max(v̂_max, v̂)`
  - use `v̂_max` in the Adam step.

**RAdam**
- Adam with safer early steps (rectified).

**Yogi**
- Tighter control of `v` (sign-aware); like Adam but steadier on noise.

**AdaBelief**
- Track `(g − m)²` instead of `g²`; can help generalization.

**Lion**
- Sign of momentum:
  - `m ← β1·m + (1−β1)·g`
  - `w ← w − η·sign(m)`

**LARS**
- For very large batches (per-layer scale):
  - `trust = ||w||/(||g|| + ε)`
  - `Δw = −η·trust·g`

**LAMB**
- AdamW + per-layer trust:
  - do AdamW → get `Δ`
  - `trust = ||w||/(||Δ|| + ε)`
  - `w ← w − trust·Δ`

---

## 3. Side-by-side table
| Optimizer | Momentum | Per-param adaptive LR | Typical Base LR | Good For | Watch-outs |
|---|---:|---:|---:|---|---|
| SGD | – | – | 0.1–1.0 (with schedule) | Strong baselines; great generalization with LR schedule | Needs careful LR; noisy steps |
| SGD + Momentum | ✔ | – | 0.03–0.3 | Vision CNNs; stable training | Tune μ≈0.8–0.95 |
| Nesterov (NAG) | ✔ (look-ahead) | – | 0.03–0.3 | Slightly faster than plain momentum | Slightly more tuning |
| Adagrad | – | ✔ | 0.01–0.1 | Sparse features (NLP/classic ML) | LR decays too much over time |
| RMSProp | – | ✔ | 1e-3–1e-2 | RNNs; drifting losses | Tune ρ≈0.9; sometimes add momentum |
| Adadelta | – | ✔ | ~1.0 | When LR is hard to pick | Can be slow |
| Adam | ✔ | ✔ | 5e-4–3e-3 | Strong default across domains | Classic L2 ≠ weight decay |
| AdamW | ✔ | ✔ | 5e-4–3e-3 | Transformers; modern CV/NLP | Prefer `weight_decay` (decoupled) |
| Nadam | ✔ | ✔ | 5e-4–3e-3 | Occasionally faster than Adam | Small gains; extra knobs |
| AMSGrad | ✔ | ✔ | 3e-4–2e-3 | When Adam unstable | May slow convergence |
| RAdam | ✔ | ✔ | 5e-4–3e-3 | More stable warmup-free starts | Similar to AdamW + warmup |
| Yogi | ✔ | ✔ | 5e-4–3e-3 | Noisy objectives | Not in all libs |
| AdaBelief | ✔ | ✔ | 1e-3–3e-3 | Better gen in some tasks | Less standard |
| Lion | ✔ (sign) | – (simple) | 3e-4–3e-3 | Large models, speed | Newer; tune carefully |
| LARS | ✔ | Layer-scale | 0.1–10 (scaled) | Very large batch CNNs | Requires correct scaling |
| LAMB | ✔ | Layer-scale + Adam | 1e-3–1e-2 | Very large batch Transformers | Mostly for huge models |

---

## 4. Good defaults

| Item | Default | Try range | Tip |
|---|---|---|---|
| LR (Adam/AdamW) | 5e-4 | 1e-4…3e-3 | Do LR-range test |
| LR (SGD+Mom) | 0.1 | 0.03…0.3 | Needs schedule |
| Momentum `μ` | 0.9 | 0.8…0.95 | Smoother steps |
| `β1` (Adam) | 0.9 | 0.8…0.95 | First moment |
| `β2` (Adam) | 0.999 | 0.98…0.9999 | Second moment |
| `ε` | 1e-8 | 1e-8…1e-6 | Stability |
| Weight decay | 0.01 | 0.001…0.1 | Use AdamW/LAMB |
| `ρ` (RMSProp) | 0.9 | 0.9…0.99 | Avg of `g²` |
| Batch size | 64 | 32…512 | Fit memory |
| Grad clip (global) | off | 0.5…1.0 | Use if spikes |

---

## 5. Learning-rate schedules

| Schedule | When | How it moves |
|---|---|---|
| Warmup | Deep nets, large batch | Start small → ramp up early |
| Step decay | Classic CNNs | Drop ×0.1 at set epochs |
| Cosine | Smooth finish | Fall to near 0 smoothly |
| One-Cycle | Fast + regularize | LR up then down; momentum down then up |
| Cyclic | LR search/small data | Bounce between min/max |

---

## 6. Batch size tips
- Start 64–256.
- Double batch ⇒ try double LR (then retune).
- For huge batch (≥4096): use **LARS** (CNN) or **LAMB/AdamW + warmup** (NLP).

---

## 7. Weight decay vs L2
- **L2 penalty**: add `λ·||w||²` to the **loss** (mixes with optimizer math).
- **Weight decay (decoupled)**: after the step do `w ← w − η·λ·w`.  
  Prefer this with Adam-style methods (**AdamW**, **LAMB**).

---

## 8. Gradient clipping
- Use if loss explodes or for long sequences.
- Best pick: **global-norm clip** to 0.5–1.0.

---

## 9. Tuning steps
1. Start: **AdamW**, batch 64–256, `lr=5e-4`, `weight_decay=0.01`.
2. Add **warmup + cosine**.
3. Run **LR-range test**, pick LR just before it blows up.
4. If spikes/NaN: enable **grad clip 1.0**.
5. If plateaus: try **One-Cycle** or Step drops.
6. If very large batch: use **LAMB/LARS** with warmup.
7. If underfit: raise LR a bit, reduce decay, or grow model.
8. If overfit: raise decay, add dropout/aug, early stop.

---

## 10. Fix guide

| Problem | Likely cause | Quick fix |
|---|---|---|
| Loss flat | LR too small | Raise LR; use AdamW; warmup+cosine |
| Loss explodes/NaN | LR too big; bad grads | Lower LR; grad clip; check data/normalization |
| Train↑, Val↓ | Overfit | More decay; dropout; augmentation; early stop |
| Slow train | No schedule; tiny batch | Add schedule; larger batch; mixed precision |
| Large-batch stalls | No warmup; wrong scaling | Warmup 5–10%; LARS/LAMB; tune LR |

---

## 11. Code (short)
(Indented code blocks keep this file one-piece.)

PyTorch — AdamW + Warmup + Cosine (+ optional clip)

    import torch
    from torch.optim import AdamW
    from torch.optim.lr_scheduler import SequentialLR, LinearLR, CosineAnnealingLR

    model = ...
    loader = ...
    EPOCHS = 10
    total_steps = len(loader) * EPOCHS

    opt = AdamW(model.parameters(), lr=5e-4, betas=(0.9, 0.999), eps=1e-8, weight_decay=0.01)

    warmup_steps = int(0.05 * total_steps)
    sch1 = LinearLR(opt, start_factor=0.1, end_factor=1.0, total_iters=warmup_steps)
    sch2 = CosineAnnealingLR(opt, T_max=total_steps - warmup_steps)
    sched = SequentialLR(opt, [sch1, sch2], milestones=[warmup_steps])

    for epoch in range(EPOCHS):
        for batch in loader:
            opt.zero_grad()
            loss = model(**batch)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)  # optional
            opt.step()
            sched.step()

Keras — SGD+Nesterov with step decay

    import tensorflow as tf

    EPOCHS = 20
    opt = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9, nesterov=True)

    def step_decay(epoch, lr):
        if epoch in [int(0.6*EPOCHS), int(0.8*EPOCHS)]:
            return lr * 0.1
        return lr

    model.compile(optimizer=opt, loss=..., metrics=[...])
    cb = tf.keras.callbacks.LearningRateScheduler(step_decay)
    model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=[cb])

One-Cycle (PyTorch idea)

    # 1) Run LR-range test quickly to find max_lr (where loss starts to blow up).
    # 2) Use torch.optim.lr_scheduler.OneCycleLR with max_lr and total_steps.
    #    Keep momentum high when LR low, and vice versa.

## 12) FAQ
- **What should I try first?** AdamW (lr≈5e-4) + warmup + cosine, batch 64–256, weight_decay≈0.01.
- **When prefer SGD?** Often for CNNs/vision when you want strongest generalization: SGD+Nesterov with step/cosine schedule.
- **Very large batch?** Use LARS (CNNs) or LAMB (Transformers). Always add warmup.
- **My validation is worse than train.** Increase weight decay, use dropout/augment, and add early stopping.
- **How to pick LR fast?** LR-range test: sweep LR exponentially for 1–3 epochs, plot loss vs LR, pick a value just before divergence.

---