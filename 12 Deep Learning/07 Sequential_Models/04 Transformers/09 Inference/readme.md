# Transformer Inference (Decoding) — simple guide

**Goal:** How a trained Transformer turns an input sentence into an output sentence at prediction time (inference).

---

## Big picture (30-second view)
- **Encoder**: same in training & inference. It reads the source sentence and produces context vectors.  
- **Decoder**: **different** behavior.  
  - **Training:** sees the whole target sentence at once (teacher forcing).  
  - **Inference:** **auto-regressive** — generates **one token at a time**, feeds it back, repeats.  

---

## Setup (tiny example)
- Task: English → Hindi translation  
- Input: “**We are friends**”  
- Output: model should generate Hindi one token at a time.  

---

## Step-by-step decoding loop
1. **Encode the source**  
   Tokenize → embeddings → + positional encoding → N×(Multi-Head Self-Attention → FFN with Add&Norm).  
   Result: contextual vectors for each source token (the “memory” for the decoder).  

2. **Start the decoder**  
   Begin with a special token: `<SOS>` (start of sentence).  
   Decoder input so far: `["<SOS>"]`.  

3. **Masked self-attention (inside decoder)**  
   - Compute Q, K, V from current target tokens.  
   - Apply **causal mask** (upper-triangle mask) so each position can only “see” **past & current** tokens, not the future.  
   - Output: target-side context.  

4. **Cross-attention (decoder → encoder)**  
   - Queries come from decoder; Keys/Values come from **encoder outputs**.  
   - Learns **which source words** matter for **this** target step.  

5. **Feed-Forward network (FFN)**  
   - Non-linear transform to mix and refine features.  
   - Add&Norm around each sub-layer as usual.  

6. **Vocab projection + Softmax**  
   - Project to vocab size → softmax to get **next-token probabilities**.  

7. **Choose next token**  
   Common strategies:  
   - **Greedy:** argmax (simple, fast).  
   - **Beam search:** keep top-B candidates (better quality).  
   - **Top-k / Top-p (nucleus) sampling:** add diversity.  
   - **Temperature τ:** >1 = more random, <1 = more focused.  

8. **Append & repeat**  
   - Append chosen token to decoder input (now `["<SOS>", token₁]`).  
   - Go back to Step 3.  
   - Stop when `<EOS>` (end of sentence) appears or **max length** is reached.  

---

## What stays the same as training
- Encoder stack, projections (Q/K/V), Add&Norm, FFNs — **identical math**.  
- **Masked** self-attention in the decoder is **still used** at inference (we must match training behavior).  

---

## Speed tips (what real systems do)
- **KV cache:** Save decoder’s K/V from previous steps so you don’t recompute them every time. Per new token you only compute **one more column** of K/V — big speedup.  
- **Batching:** You can decode multiple sentences in parallel (especially easy with greedy/beam).  

---

## Practical knobs
- **Max length:** hard cap to avoid endless generation.  
- **Length penalty (beam):** avoids too-short outputs.  
- **Repetition penalty / no-repeat n-grams:** reduces loops like “very very very…”.  
- **Special tokens:** `<SOS>`, `<EOS>`, `<PAD>`, `<UNK>` — make sure your tokenizer agrees with the model.  

---

## Minimal pseudocode (greedy)
```python
# Given: tokenizer, model, source_text
src_ids = tokenize(source_text)
enc_out = model.encode(src_ids)          # Encoder once

tgt_ids = [SOS_ID]
for t in range(MAX_LEN):
    # Decoder takes previous outputs
    logits = model.decode(enc_out, tgt_ids)   # masked self-attn + cross-attn + FFN
    next_id = argmax(softmax(logits[-1]))     # last step's distribution
    if next_id == EOS_ID:
        break
    tgt_ids.append(next_id)

result = detokenize(tgt_ids[1:])  # drop <SOS>
```
(Beam/top-k/top-p differ only in how next_id (or next hypotheses) are chosen.)  

---

## Shapes at a glance (single example)
- **Encoder input:** `[S, d_model]`  → encoder output: `[S, d_model]`  
- **Decoder running step t input:** `[t, d_model]`  
- **Masked self-attention:** attends over t tokens (causal mask)  
- **Cross-attention:** Q from `[t, d_model]`, K/V from encoder `[S, d_model]`  
- **Output logits at step t:** `[Vocab]`  

---

## Common mistakes (and quick fixes)
- **Forgetting the mask** → future leakage → nonsense.  
  Fix: upper-triangular causal mask in decoder self-attention.  
- **No KV cache** → slow decoding.  
  Fix: cache & reuse past K/V for each head.  
- **Short/stopped sentences with beam.**  
  Fix: add length penalty; tune beam size.  
- **Repetition & loops.**  
  Fix: repetition penalty, no-repeat n-gram, top-p/top-k sampling.  

---

## Quick memory hooks
- Encoder same, Decoder changes.  
- Auto-regressive: one token at a time, feed back in.  
- Mask in decoder self-attention — always.  
- Cross-attention reads from encoder “memory”.  
- KV cache = fast inference.  
- Stop at `<EOS>` or max length.  