# Cross-Attention (Decoder): A Super-Simple Guide

**One-liner:** Cross-attention lets the decoder look at the encoder’s outputs while generating each target token. Queries come from the decoder; Keys/Values come from the encoder.

---

## Why do we need it?
- Self-attention (inside encoder/decoder) looks within the same sequence.  
- Cross-attention lets the decoder look **across** to the encoder, so every output token can focus on the most relevant input tokens (e.g., the right word(s) in the source sentence).  

**Think:** “I’m writing the translation word-by-word. Before picking the next word, let me glance at the whole source sentence and highlight what matters.”

---

## What is flowing where?
- **Q (queries):** current decoder representations (what the decoder needs).  
- **K (keys) & V (values):** encoder outputs (what the encoder provides).  
- **Output:** updated decoder representations that are now context-aware (aware of the source sequence).  

---

## Cross-Attention vs Self-Attention (at a glance)

| Topic            | Self-Attention                        | Cross-Attention                     |
|------------------|---------------------------------------|--------------------------------------|
| Where do Q,K,V come from? | All from the same sequence         | Q from decoder, K,V from encoder    |
| Purpose          | Build context inside a sequence       | Pull relevant info from the other sequence |
| Masking          | Encoder: none; Decoder: causal mask   | Usually no mask (just pad mask)      |
| When used        | Encoder & decoder blocks              | Decoder block (between masked self-attn and FFN) |

---

## The step-by-step picture
For one decoder layer (ignoring residuals/norms for the moment):  
1. Decoder does masked self-attention over already-generated tokens → `H_dec`.  
2. Cross-attention:  
   - Make Q from `H_dec`.  
   - Make K,V from encoder outputs `H_enc`.  
   - Compute attention weights with `softmax(QKᵀ / √d_k)`.  
   - Mix values: `Context = Weights · V`.  
3. Feed Context to the feed-forward network → updated decoder states.  

Repeat across layers; the final decoder head produces logits for the next token.  

---

## Shapes cheat-sheet (batch size B)
- Encoder outputs: `H_enc → [B, T_enc, d_model]`  
- Decoder states so far: `H_dec → [B, T_dec, d_model]`  
- After projections:  
  - Q: `[B, T_dec, d_k]`  
  - K: `[B, T_enc, d_k]`  
  - V: `[B, T_enc, d_v]`  
- Weights: `softmax(QKᵀ/√d_k)` → `[B, T_dec, T_enc]`  
- Context: `[B, T_dec, d_v]` → projected back to `d_model`  

**Complexity:** O(T_dec · T_enc · d_k) — scales with both lengths.  

---

## A tiny mental model
- **Queries (Q):** questions from the decoder: “What do I need right now?”  
- **Keys (K):** labels on encoder tokens: “Here’s what I contain.”  
- **Values (V):** the actual content you’ll take if you pick that token.  
- **Attention:** match Q with K, then take a weighted mix of V.  

---

## Masking rules you’ll actually use
- No causal mask here (future target tokens aren’t part of K/V).  
- Pad mask for the encoder: ignore padded positions in `H_enc`.  
- Keep the causal mask only in the decoder’s self-attention (previous sublayer).  

---

## Minimal PyTorch-like sketch (one head, no boilerplate)
```python
# H_dec: [B, T_dec, d_model], H_enc: [B, T_enc, d_model]
Q = H_dec @ W_Q            # [B, T_dec, d_k]
K = H_enc @ W_K            # [B, T_enc, d_k]
V = H_enc @ W_V            # [B, T_enc, d_v]

scores = (Q @ K.transpose(-2, -1)) / (d_k ** 0.5)  # [B, T_dec, T_enc]
scores += enc_pad_mask     # 0 or -inf at encoder pad spots
weights = scores.softmax(dim=-1)                    # [B, T_dec, T_enc]

context = weights @ V      # [B, T_dec, d_v]
out = context @ W_O        # [B, T_dec, d_model]
```
For multi-head, do this in parallel for multiple heads, then concat heads and project with `W_O`.  

---

## When does cross-attention shine?
- **Machine translation / summarization / dialogue:** decoder pulls the most relevant source tokens at each step.  
- **Vision-language models:** text queries attend to image features.  
- **Retrieval-augmented generation:** decoder queries external memory/encoder outputs.  

---

## Gotchas & tips
- Length mismatch is normal: T_dec and T_enc can differ (often do).  
- Memory use: T_dec × T_enc attention map can be big; watch GPU.  
- Padding: always supply an encoder pad mask to avoid attending garbage.  
- Ordering: Decoder layer = Masked Self-Attn → Cross-Attn → FFN (each with Add & Norm).  

---

## (stick this on your wall)
- Q from decoder, K/V from encoder.  
- Weights = `softmax(QKᵀ/√d_k)` → mix V → context for each target step.  
- No causal mask here (use pad mask only).  
- This is how the decoder looks at the source to pick the right next token.  