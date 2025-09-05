# Transformer Encoder — a super-simple, memory-friendly guide

Why it exists: The encoder turns a batch of tokens into rich, context-aware vectors the decoder (or a classifier) can use. Think of it as: Tokens → Understanding.

---

## (one screen)
- A Transformer has two big parts: Encoder and Decoder. The encoder is a stack of identical blocks (often 6). Each block has just two brains: Multi-Head Self-Attention and a Feed-Forward Network (FFN), with residual (skip) connections and LayerNorm around each.  
- Shapes you’ll see a lot: d_model = 512, FFN hidden = 2048. Outputs keep the same length × 512 shape through the whole encoder.  
- Input prep is crucial: Tokenize → Embed → Add Positional Encoding → go into block 1 → … → block N.  

---

## The mental picture (carry this in your head)

```
Input tokens
   │  (tokenize → embed → + position)
   ▼
[ Encoder Block ] × N   (N ≈ 6)
   ├─ Multi-Head Self-Attention
   │    + residual → LayerNorm
   └─ Feed-Forward (512 → 2048 → 512)
        + residual → LayerNorm
   ▼
Same length of vectors, each still 512-dim, but now context-aware
```

Each block is architecturally identical (copy-paste structure), but has its own learned weights. If you understand one block, you understand them all.  

---

## What goes in (and why)
1. **Tokenization** → split text into tokens (e.g., words/subwords).  
2. **Embedding** → map each token to a dense 512-dim vector.  
3. **Positional Encoding** → add a same-size vector that says “I’m the 1st/2nd/… token”, because attention itself doesn’t know order.  

Now you have a sequence like: X ∈ (length × 512). This is fed to encoder block 1.  

---

## Inside one encoder block (the 2-step dance)

**1) Multi-Head Self-Attention → Add → LayerNorm**  
- Goal: Make each token’s vector “look around” at other tokens to become context-aware.  
- Multi-Head = several attention views in parallel (different subspaces), then concat and re-project to 512.  
- Residual (skip) add: X + Attention(X) keeps gradients healthy and preserves original info.  
- LayerNorm after the add stabilizes training.  
- Result shape is still length × 512.  

**2) Feed-Forward (FFN) → Add → LayerNorm**  
- Small MLP applied to each position independently:  
  - Linear 512 → 2048, ReLU  
  - Linear 2048 → 512  
- Again residual add and LayerNorm.  
- Result shape stays length × 512. This adds non-linearity/capacity beyond attention’s linear ops.  

Stack N of these blocks (commonly 6) so the model can build deep, expressive representations of language. Output goes to the decoder (for seq2seq) or straight to a head (for classification).  

---

## Shapes at a glance (defaults you’ll recognize)
- d_model: 512 throughout the encoder (inputs, attention outputs, FFN output).  
- FFN hidden: 2048 (middle layer).  
- Length (time steps): unchanged from input to output.  

So you can mentally track: (L × 512) → (L × 512) → … (L × 512) across all encoder blocks.  

---

## Tiny FAQ (the “why”s)
- **Why residual connections?**  
  They provide an alternative gradient path (easier training, less vanishing) and let the model fall back to raw features if a sub-module hurts rather than helps.  

- **Why the FFN after attention?**  
  Attention mixes information; the FFN adds non-linear transformation power per position (512→2048→512) to shape richer features.  

- **Why multiple blocks (e.g., 6)?**  
  Language is complex; stacking blocks increases representational depth. “6” is a commonly used, empirically strong choice.  

---

## One-minute walk-through (“How are you?”)
1. Tokens: “How”, “are”, “you”.  
2. Embeds: 3 vectors ∈ ℝ⁵¹².  
3. Add positions: still 3×512.  
4. Block 1: attention makes each token context-aware → add+norm → FFN → add+norm (still 3×512).  
5. Repeat for blocks 2…6: always 3×512, but features get sharper.  
6. Done: pass to decoder (for translation/summarization) or a head (for classification).  

---

## Wrap-up
The encoder is just **“Attention + FFN”**, repeated with skips and norms, keeping shapes constant while making every token smart about its neighbors.