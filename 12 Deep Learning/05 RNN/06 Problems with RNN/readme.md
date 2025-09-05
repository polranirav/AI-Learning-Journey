# RNN — Problems, Why They Happen, and Quick Fixes

## 0) What this file is
A fast, GitHub-ready note on **why vanilla RNNs struggle** and **what you can do**. Plain words, memorable bullets, minimal math.

---

## 1) Tiny recap: how gradients move in an RNN
During training we use **Backpropagation Through Time (BPTT)**. Gradients flow through **all time steps** as a *product* of Jacobians:

```∂L/∂W ≈ Σ_t  (∂L/∂o_T) · (∂o_T/∂o_{T-1}) · … · (∂o_{t+1}/∂o_t) · (∂o_t/∂W)```

If those intermediate factors are mostly **< 1**, the product shrinks (vanishes). If they’re mostly **> 1**, it grows (explodes). That’s the core of both problems.

---

## 2) Problem #1 — Long-term dependency (vanishing gradients)
**What you see**
- Model uses only **recent tokens**; forgets far context.
- Next-word suggestions make sense for short phrases but fail on long sentences.
- Training loss decreases slowly or saturates early; gradients near **0**.

**Why it happens (intuition)**
- In BPTT the gradient at early time steps is a **chain of multiplications** by terms typically in `(0, 1)` (e.g., `tanh'` and recurrent weights). Over many steps that product → **0**.

**Impact**
- RNN can’t carry information over long spans → **can’t model long-term dependencies** well. This is the classic reason we move to **LSTM/GRU**.

**What helps (quick fixes)**
- **Activations**: prefer ones that don’t squash too hard (e.g., try ReLU/LeakyReLU in simple RNNs).
- **Recurrent init**: use **identity/orthogonal** init for the recurrent matrix to preserve magnitude across steps.
- **Skip/shortcut connections** across time (where feasible) to shorten gradient paths.
- **Real fix**: switch to **LSTM/GRU** (gates keep/forget information explicitly).

---

## 3) Problem #2 — Unstable training (exploding gradients)
**What you see**
- Loss **spikes**, becomes **NaN/Inf**, or training diverges.
- Weights blow up; updates are huge; metrics swing wildly.

**Why it happens (intuition)**
- The same chain rule, but now intermediate factors are **> 1** (e.g., large recurrent weights or activations with big derivatives) → the product **explodes**. Too-high **learning rate** makes it worse.

**What helps (quick fixes)**
- **Gradient clipping** (by value or by norm) to cap update size.
- **Lower learning rate**; use schedulers; try optimizers with better conditioning.
- **Safer inits** (orthogonal/identity for recurrent, small input weights) and reasonable sequence lengths (truncate BPTT).

---

## 4) Symptoms → Likely cause → First aid (at a glance)

| Symptom                                                                              | Likely cause                 | First aid                                                                       |
|--------------------------------------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------|
| Good on short text, fails on long context; gradients ~ 0 at early steps              | **Vanishing gradients**      | ReLU/LeakyReLU, orthogonal/identity recurrent init, skip links, use LSTM/GRU    |
| Loss jumps/NaN; weights explode; training diverges                                   | **Exploding gradients**      | **Gradient clipping**, reduce LR, safer inits, truncated BPTT                    |
| Training crawls; feels “stuck”                                                       | Vanishing + sub-optimal LR   | Slightly higher LR + better init; or move to gated RNN                          |
| Only recent tokens influence predictions; far tokens ignored                          | Long-term dependency limit   | Architectural: **LSTM/GRU** (preferred), or add skip connections                | 

---

## 5) Minimal mental model
- RNN training = **BPTT** = multiply a bunch of step-wise derivatives.
- **< 1** repeatedly → product → **0** (vanish) → forgets long-range info.
- **> 1** repeatedly → product → **∞** (explode) → unstable updates.
- Practical band-aids exist, but the **robust solution for long context is LSTM/GRU**.

---

## 6) Quick checklist before you give up
- [ ] Clip gradients (start: norm=1.0 or 5.0).  
- [ ] Lower LR (10× step down) and retry.  
- [ ] Orthogonal/identity **recurrent** init; small input weights.  
- [ ] Try ReLU/LeakyReLU if you used heavy squashing everywhere.  
- [ ] Shorten sequences (truncate BPTT) to stabilize early training.  
- [ ] If task truly needs long memory → **switch to LSTM/GRU**.

---

**You now know exactly why vanilla RNNs fail and the fastest ways to steady them.** Next step: LSTM/GRU — how gates preserve and control gradients over long time spans.