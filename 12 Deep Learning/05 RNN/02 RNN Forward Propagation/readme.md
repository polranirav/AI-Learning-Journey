# RNN Forward Propagation (Step-by-Step, Shapes & Intuition)

---

## 1) What changes vs a normal (feed-forward) net
- Step by step: RNN reads the sequence one time step at a time: t = 1, 2, …, T.  
- Memory (hidden state): it carries a small memory h_t from the previous step to the next step.  
- Shared weights: the same parameters are reused at every time step (weight sharing).  
- Result: order matters; the model can use context from the past to predict the present.  

---

## 2) Data layout (shapes you actually use)
- Per batch: (batch, T, features)  
- T: number of time steps (e.g., words per sentence after padding)  
- features: input vector size per step (e.g., one-hot size or embedding size)  
- Text example: tokenize → either one-hot (features = |vocab|) or Embedding (features = d_embed)  
- Time series example: each step = a feature vector (e.g., [open, high, low, close] → features = 4)  
- Padding + masking: pad to a common T_max, and mask padded positions so the model ignores them.  

---

## 3) The simple RNN cell (forward equations)
For each step t:  
- State update: h_t = act(W_xh · x_t + W_hh · h_{t-1} + b_h)  
- Output (optional at each step): ŷ_t = out(W_hy · h_t + b_y)  
- Initial state: h_0 = 0 (or learn / pass a custom state)  
- Typical activations: act = tanh (RNN state), out = sigmoid/softmax/linear (depends on task)  

**Shapes (common pick):**  
- x_t → (features,)  
- h_t → (hidden,)  
- W_xh → (features, hidden)  
- W_hh → (hidden, hidden)  
- W_hy → (hidden, output_dim)  

---

## 4) Unrolling through time (what “forward pass” means)
Imagine the same cell copied T times:  
1. t = 1: use x_1 and h_0 → compute h_1 (and maybe ŷ_1)  
2. t = 2: use x_2 and carry h_1 → compute h_2 (and maybe ŷ_2)  
3. …  
4. t = T: use x_T and h_{T-1} → compute h_T (and maybe ŷ_T)  

All steps reuse the same W_xh, W_hh, W_hy. That’s how RNNs remember context.  

---

## 5) Output patterns (which ŷ do you use?)
| Pattern             | What you return               | Typical use                          |
|---------------------|--------------------------------|---------------------------------------|
| Many→One            | last state/output (h_T → ŷ)   | sentence sentiment, series classification |
| Many→Many (aligned) | every step’s output (ŷ_1…ŷ_T) | POS tagging, per-step anomaly flag   |
| Seq2Seq             | encoder state(s) → decoder outputs | translation, captioning (uses decoder RNN) |

**In Keras:** `return_sequences=False` for Many→One; `True` for Many→Many.  

---

## 6) A tiny worked example (shapes + parameter count)
- Toy text: vocab size V = 5 (one-hot), sequence length T = 4, hidden size H = 3, output = binary (1 unit).  
- Shapes:  
  - x_t: (5,) one-hot  
  - W_xh: (5, 3) → 15 params  
  - W_hh: (3, 3) → 9 params  
  - b_h: (3,) → 3 params  
  - W_hy: (3, 1) → 3 params  
  - b_y: (1,) → 1 param  
  - Total params: 15 + 9 + 3 + 3 + 1 = 31 (reused at each step)  

**Forward pass over T=4:**  
1. h_1 = tanh(W_xh x_1 + W_hh h_0 + b_h); ŷ_1 = σ(W_hy h_1 + b_y) (if needed)  
2. h_2 = tanh(W_xh x_2 + W_hh h_1 + b_h); ŷ_2 = σ(…)  
3. h_3 = tanh(W_xh x_3 + W_hh h_2 + b_h); ŷ_3 = σ(…)  
4. h_4 = tanh(W_xh x_4 + W_hh h_3 + b_h); ŷ_4 = σ(…)  

For Many→One, keep only ŷ_last (or map from h_last).  

---

## 7) Practical choices that affect forward behavior
- Embedding > one-hot for text: smaller features, smoother learning.  
- Hidden size (H): bigger = more capacity, but slower; start small, grow as needed.  
- Masking: must be on if you pad sequences, so forward pass ignores pads.  
- Bidirectional (for offline tasks): forward + backward passes over time improve context.  
- Return sequences: on/off to match your desired output pattern.  

---

## 8) Where people trip up (forward-pass gotchas)
- Mismatched shapes: (batch, T, features) is the norm; don’t forget batch axis.  
- Forgetting initial state: default is zeros; pass a state only if you mean to.  
- Using the wrong output step: Many→One tasks should read last state/output, not all steps.  
- Padding leakage: without masks, the model “reads” padded zeros as real data.  

---

## 9) Minimal mental recipe (how to “run” an RNN)
1. Prepare (batch, T, features) (pad + mask if needed).  
2. For t = 1..T: feed x_t and previous h_{t-1} → get h_t (and maybe ŷ_t).  
3. Choose the right output pattern (last step or all steps).  
4. Map h to prediction with a small output layer and the right activation.  

---

## 10) Memory hooks (quick recall)
- Core update: h_t = act(W_xh x_t + W_hh h_{t-1} + b_h)  
- Carry context: h_t depends on current input and previous state.  
- Same weights at every step.  
- Shapes: (batch, T, features) → hidden (H) → output.  
- Pick output pattern (Many→One vs Many→Many) to match your task.  

---