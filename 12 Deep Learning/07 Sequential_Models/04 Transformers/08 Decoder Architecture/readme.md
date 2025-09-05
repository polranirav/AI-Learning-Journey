# Transformer Decoder — README

> **Goal:** Turn encoder outputs + partial target sentence into the next target tokens.  
> **Use-cases:** translation, captioning, code generation, summarization.

---

## 1) Big Picture (in plain words)
- A Transformer = **Encoder stack** + **Decoder stack**.  
- The **Decoder** reads two things:  
  1) **What we’ve generated so far** (target sentence, shifted right).  
  2) **Encoder memory** (the encoded input).  
- Each decoder layer does **three steps**:  
  1) **Masked self-attention** (look only at past tokens).  
  2) **Cross-attention** (look into encoder outputs).  
  3) **Feed-forward** (mix features non-linearly).  
- After N layers (usually 6), a **linear layer + softmax** picks the next word.  

---

## 2) Input to the Decoder (training time)
1. **Shift-right** the target: add a special `<START>` at the front and drop the last token.  
   This enforces “predict token *t* from tokens `<START> ... t-1`”.  
2. **Tokenize** target sentence into ids.  
3. **Embedding**: map ids → vectors of size `d_model` (e.g., 512).  
4. **Positional encoding**: add position info so order matters.  
5. Send the result to **decoder layer 1**.  

> Tip: At training we use **teacher forcing** (we always feed ground-truth previous tokens).  
> At inference we **auto-regress** (feed our own last prediction).  

---

## 3) One Decoder Layer (the heart)
Each layer repeats this trio with **residual skip** and **LayerNorm** after each sub-block:

### A) Masked Self-Attention
- **Why masked?** The model must not peek at future words.  
- **What it does:** For every position *t*, build attention over positions `≤ t` in the **decoder input**.  
- **Math sketch:**  
  `Attention(Q, K, V) = softmax((Q Kᵀ) / √d_k + mask) V`  
  Here, `Q=K=V` come from the decoder’s current states (multi-head version in practice).  

### B) Cross-Attention (a.k.a. Encoder–Decoder Attention)
- **Why:** Let the decoder consult the **encoder memory** (the input meaning).  
- **What it does:**  
  - `Q` from **decoder stream** (output of masked self-attn).  
  - `K, V` from **encoder outputs** (the “memory”).  
  - Same attention formula (no look-ahead mask here).  

### C) Feed-Forward Network (FFN)
- Two linear layers with a nonlinearity (e.g., ReLU or GELU):  
  - `Linear(d_model → d_ff)` → `ReLU/GELU` → `Linear(d_ff → d_model)`.  
- Acts **position-wise** (applied to each token vector independently).  

**After each sub-block:**  
`y = LayerNorm(x + SubBlock(x))`  (residual + normalize)  

---

## 4) Stack of Layers
- Repeat the layer above **N times** (e.g., 6).  
- All layers share the **same design** but **different learned weights**.  

---

## 5) Output Head
- Take the final decoder states `[B, T, d_model]`.  
- Apply **Linear(d_model → VocabSize)** to get **logits** `[B, T, V]`.  
- Apply **softmax** over `V` to get probabilities for each next token.  
- **Loss:** token-wise cross-entropy vs the **true** target tokens.  

---

## 6) Training vs. Inference (one-line view)
- **Training:** feed **shifted ground truth** (teacher forcing). All time steps run in parallel.  
- **Inference:** start with `<START>`, **loop**: predict → append → predict next (auto-regressive).  

---

## 7) Shapes at a Glance (common defaults)

| Object                   | Shape             |
|--------------------------|-------------------|
| Encoder memory           | `[B, S, d_model]` |
| Decoder input (embedded) | `[B, T, d_model]` |
| After any decoder layer  | `[B, T, d_model]` |
| Output logits            | `[B, T, V]`       |

`B`: batch, `S`: source length, `T`: target length, `V`: target vocab size, `d_model`: model width.  

---

## 8) Mental Model (sticky ideas)
- **Masked self-attn = “talk to your past self only.”**  
- **Cross-attn = “ask the encoder for help.”**  
- **FFN = “non-linear polish per token.”**  
- **Residual + LayerNorm = “keep signals stable and trainable.”**  
- **Shift-right = “predict next from previous.”**  

---

## 9) Minimal Pseudocode (framework-agnostic)
```python
# x_mem: encoder outputs [B,S,d_model]
# y_in:  shifted target embeddings + positions [B,T,d_model]

h = y_in
for _ in range(N_layers):
    # Masked self-attn (causal)
    h = LayerNorm(h + MultiHeadSelfAttn(h, h, h, mask="causal"))
    # Cross-attn (Q from h, K/V from encoder memory)
    h = LayerNorm(h + MultiHeadCrossAttn(q=h, k=x_mem, v=x_mem))
    # Feed-forward
    h = LayerNorm(h + FFN(h))

logits = LinearToVocab(h)     # [B,T,V]
loss = CrossEntropy(logits, y_true)  # training
```

---

## 10) Frequent Gotchas (and fixes)
- Forgetting the causal mask → leakage of future info.  
- Missing shift-right → the model can’t learn “next token” prediction.  
- Wrong vocab between embed and head → mismatch; keep target vocab consistent.  
- Too small d_ff in FFN → weak capacity; start with d_ff ≈ 4× d_model.  
- No dropout → overfitting; add dropout in attn/ffn sub-blocks (during training).  

---

## 11) Quick Checklist (before you run)
- Target tokens are shifted right (have `<START>` at index 0).  
- Causal mask on decoder self-attention.  
- Cross-attention gets K,V from encoder outputs.  
- Residual + LayerNorm after each sub-block.  
- Output head uses target vocab and cross-entropy on true targets.  
- Batch shapes match the table above.  
- Train with teacher forcing; infer auto-regressively.  

---
The decoder is a stack of identical layers. Each layer first looks back (masked self-attention), then looks across to the encoder (cross-attention), then polishes with an FFN. Residuals + LayerNorm keep training stable. A linear + softmax head turns the final states into words.  