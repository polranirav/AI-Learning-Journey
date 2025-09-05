# Masked Self-Attention (Decoder) — Simple, Clear, and Memorable

Masked self-attention lets the Transformer decoder look only at the past and present tokens—never the future—so we can train in parallel without cheating, and generate step-by-step at inference.

---

## Why do we need “masking”?
- In generation tasks (translation, summarization, chat), later words depend on earlier ones.  
- During training, we already know the whole target sentence. If we let the model use future words when predicting the current one, that’s data leakage (“peeking ahead”).  
- A mask blocks attention to future positions so the model can’t peek, yet we can still compute all positions in parallel.  

---

## Where does it live?
- In the decoder, the very first sublayer is **Masked Multi-Head Self-Attention**.  
- Self-attention = each output token attends over the decoder’s own (already-generated) tokens.  
- “Masked” = we forbid each position from seeing tokens to its right (future).  

---

## What is the mask?
A square matrix shaped `(T × T)` for a target sequence of length T:  
- Allowed (past & current): keep scores as is.  
- Forbidden (future): set scores to −∞ before softmax (so softmax → 0).  

Sketch (lower-triangular keep-area):

```
keep  keep  keep   0
keep  keep  keep   0
keep  keep  keep   0
keep  keep  keep  keep
```

(Real masks are numbers: 0 for keep, −∞ for block.)  

---

## The one-line recipe
We use the standard attention, but add a mask to the score matrix:

$begin:math:display$
\\text{Attention}(Q, K, V) = \\text{softmax}\\Big(\\frac{QK^T}{\\sqrt{d_k}} + \\text{mask}\\Big) \\cdot V
$end:math:display$

- Q = queries, K = keys, V = values (all from the decoder’s current token embeddings after linear projections).  
- mask = 0 where attention is allowed, −∞ where it isn’t (future positions).  
- softmax(−∞) = 0, so forbidden links vanish.  

---

## Step-by-step (mental model)
1. Embed the target tokens seen so far (during training: the whole ground-truth target; during inference: what’s generated so far).  
2. Project to Q, K, V for each token.  
3. Score = QKᵀ / √d_k (how much each token should look at each other).  
4. Mask: add −∞ above the diagonal (future).  
5. Softmax: convert scores to attention weights (future weights become 0).  
6. Weighted sum: multiply weights by V to get context-aware representations.  
7. Multi-head: do it in several heads, then concat & project.  
8. Residual + LayerNorm, then pass onward (cross-attention, FFN, etc.).  

---

## Training vs. Inference (the key idea)
- **Training (non-autoregressive compute):** We feed the entire target sequence at once (teacher forcing), apply the mask, and compute outputs for all positions in parallel. No peeking occurs because the mask blocks future tokens.  
- **Inference (autoregressive generation):** We don’t have future tokens yet, so we generate one token at a time. After each step, append the new token, recompute the masked self-attention for the extended sequence (or use caching), and continue.  

**Memory hook:** Train fast, predict step-by-step. Mask = no peeking to the right.  

---

## Tiny example (3 tokens)
Target: `["I", "am", "fine"]` (length T=3)

Mask (where X = blocked, . = allowed):

```
t=1:  .  X  X   (token 1 sees itself only)
t=2:  .  .  X   (token 2 sees tokens 1–2)
t=3:  .  .  .   (token 3 sees tokens 1–3)
```

Softmax turns those X spots into 0 attention.  

---

## Common gotchas (and quick answers)
- **“Why not just zero out future scores?”**  
  We add −∞ before softmax; that guarantees exactly 0 weight after softmax.  
- **“Do encoders use this mask?”**  
  No. The encoder uses unmasked self-attention (it can see all source tokens).  
- **“Is this the same as padding mask?”**  
  Different purpose: a padding mask hides pad tokens. Causal (look-ahead) mask hides future tokens. They’re often combined.  
- **“Why multi-head?”**  
  Different heads learn different relations (syntax, coreference, etc.), improving quality.  

---

## Pocket summary (memorize this!)
- **Purpose:** Stop future leakage; keep generation causal.  
- **Mechanism:** Add −∞ to future score entries → softmax → 0 weight.  
- **Training:** Full sequence in parallel (fast!) with mask.  
- **Inference:** One token at a time (autoregressive).  
- **Location:** First sublayer inside each decoder block.  

**Masked self-attention = causal attention: no peeking, fast training, correct generation.**