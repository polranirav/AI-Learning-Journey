# Positional Encoding (Transformers)


## 1) Why do we need positional encoding?
Transformers read a sentence **all at once** (in parallel). That makes them fast, but they **lose word order** by default.  
**Positional encoding (PE)** puts **order** back into token embeddings so the model can tell **“who came before/after whom.”**

**Think:**  
- “I ate *not* apples” vs “I *not* ate apples” — same words, different order → different meaning.  
- PE gives each position (0, 1, 2, …) a tiny **signal** so attention can use order.

---

## 2) Design goals (what a good PE should do)
- **Addable:** Same shape as embeddings so we can **add** them: `x_with_pos = token_embed + pos_embed`.  
- **Smooth:** Nearby positions have similar encodings → helps attention learn local patterns.  
- **Generalize:** Handle longer/shorter sequences (ideally **extrapolate** beyond train length).  
- **Parameter-light:** Preferably not huge extra weights.

---

## 3) The classic sine–cosine positional encoding
The original Transformer uses **fixed (non-learned)** sin/cos waves at different frequencies.

For model dimension `d_model`, and position `pos` (0, 1, 2, …):

- For even dimensions `2i`:  
  `PE[pos, 2i] = sin( pos / 10000^(2i / d_model) )`  
- For odd dimensions `2i+1`:  
  `PE[pos, 2i+1] = cos( pos / 10000^(2i / d_model) )`

**Intuition:**  
- Each pair `(sin, cos)` at index `i` is a **wave** with a different wavelength.  
- Stacking many waves creates a **unique fingerprint** for each position.  
- Relative shifts between fingerprints help the model reason about **relative distances**.  

**Why sin *and* cos?**  
Together they form an **orthogonal** basis; shifting position is like **rotating phase**, which attention can compare easily.

---

## 4) How do we use PE in a Transformer?
1. Get token embeddings `E ∈ R^[seq_len, d_model]`.  
2. Compute or lookup `PE ∈ R^[seq_len, d_model]`.  
3. **Add** them: `X = E + PE`.  
4. Pass `X` into the encoder/decoder blocks (self-attention, FFN, …).  

> That’s it — PE is just **added once** before the first attention layer (sometimes re-added in later layers, but the common pattern is once).

---

## 5) Fixed vs learned positional encodings

### A) Fixed (sin–cos) — what we just saw
- **Pros:** No extra parameters, works out of the box, decent **extrapolation** to slightly longer sequences.  
- **Cons:** Not task-specific; sometimes **learned** PEs perform better.

### B) Learned absolute position embeddings
- A **table of vectors** (like a vocab for positions).  
- **Pros:** Task-specific, often strong performance on train lengths.  
- **Cons:** **No natural extrapolation** beyond the maximum trained position (pos > max_pos needs special care).

> In practice: start with **sin–cos** for simplicity or use the library default. Try learned PEs if you need a performance bump and your sequence lengths are stable.

---

## 6) Mini code (NumPy/PyTorch) — fixed sin–cos PE
```python
import math
import numpy as np
import torch

def positional_encoding(seq_len: int, d_model: int, device=None):
    # seq_len x d_model
    pos = np.arange(seq_len)[:, None]                  # (L, 1)
    i   = np.arange(d_model)[None, :]                  # (1, D)
    angles = pos / np.power(10000, (2*(i//2))/d_model) # (L, D)

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angles[:, 0::2])  # even dims
    pe[:, 1::2] = np.cos(angles[:, 1::2])  # odd dims

    tensor = torch.tensor(pe, dtype=torch.float32)
    return tensor if device is None else tensor.to(device)

# Example:
L, D = 128, 512
PE = positional_encoding(L, D)  # (128, 512), add to token embeddings
```

**Shape check:** embeddings and PE must match `(seq_len, d_model)` (or `(batch, seq_len, d_model)` when batched — you’ll typically broadcast the same PE over the batch).

---

## 7) Practical tips & gotchas
- **Scaling:** Some implementations scale token embeddings by √d_model before adding PE: `X = √d_model * E + PE`. This keeps magnitudes balanced.  
- **Masking:** PE doesn’t replace padding masks. Still mask pad tokens in attention.  
- **Very long sequences:** Fixed sin–cos can oscillate; for very long context you might explore relative or rotary variants (below).  
- **Extrapolation:** Fixed PEs can go past train length; learned absolute PEs usually can’t (without tricks).

---

## 8) Variants you’ll hear about (one-liners)
Keep it simple on first pass; these are nice to know:  
- **Relative position bias/encodings:** Model uses distance between tokens (i−j) rather than absolute index. Helps generalize to different lengths and long-range patterns.  
- **RoPE (Rotary Positional Embeddings):** Injects position as a rotation in query/key space. Plays nicely with dot-product attention and often helps long-context performance.  
- **ALiBi (Attention with Linear Biases):** Adds a simple distance-based bias to attention scores; very cheap and good for long sequences.

---

## 9) FAQ (quick answers)
**Q1: Why add, not concatenate?**  
Adding keeps the dimension fixed and lets PE act like a gentle “position flavor” on each feature. Concatenation doubles dims and changes parameter counts everywhere.  

**Q2: Do we add PE at every layer?**  
Common default: add once at the input of the first layer. Some models re-inject position info each layer (design choice).  

**Q3: Does PE go to decoder too?**  
Yes. Both encoder inputs and decoder inputs need positions.  

**Q4: What about CNN/RNN?**  
They carry order inherently (conv/recurrent structure). Transformers need explicit positional info.

---

## 10) Quick checklist (memory hooks)
- Transformer is order-blind → we must add position.  
- Sin–cos PE: fixed, parameter-free, adds smoothly varying waves.  
- Formula: `sin/cos(pos / 10000^(2i/d_model))`.  
- Add to embeddings (shapes must match).  
- For long contexts: consider relative/RoPE/ALiBi.  
- Mask pads as usual; PE ≠ padding mask.  
- Start simple, switch to learned/relative if needed.

---

## 11) Tiny Keras/PyTorch snippets (how to plug in)

**Keras (conceptual):**
```python
import tensorflow as tf

class SineCosPE(tf.keras.layers.Layer):
    def __init__(self, max_len, d_model):
        super().__init__()
        pe = positional_encoding(max_len, d_model).numpy()
        self.pe = tf.constant(pe[None, ...])  # (1, L, D)

    def call(self, x):
        # x: (batch, seq_len, d_model)
        return x + self.pe[:, :tf.shape(x)[1], :]
```

Usage in a model:
```python
inp = tf.keras.Input(shape=(None,), dtype=tf.int32)
emb = tf.keras.layers.Embedding(input_dim=vocab, output_dim=d_model)(inp)
x   = SineCosPE(max_len=2048, d_model=d_model)(emb)
# ... transformer blocks ...
```

**PyTorch (conceptual):**
```python
import torch.nn as nn

class SineCosPE(nn.Module):
    def __init__(self, max_len, d_model, device=None):
        super().__init__()
        pe = positional_encoding(max_len, d_model, device=device)  # (L, D)
        self.register_buffer("pe", pe.unsqueeze(0))                # (1, L, D)

    def forward(self, x):
        # x: (batch, seq_len, d_model)
        return x + self.pe[:, :x.size(1), :]
```

Usage:
```python
# x = token_embeds(x_ids)  # (B, L, D)
# x = SineCosPE(2048, d_model)(x)
# x = transformer_blocks(x)
```

---

- Transformers need positional info to understand order.  
- Sin–cos PE is the classic, simple, parameter-free way.  
- Add PE to token embeddings; then run attention.  
- For longer contexts or special tasks, explore learned, relative, RoPE, or ALiBi.