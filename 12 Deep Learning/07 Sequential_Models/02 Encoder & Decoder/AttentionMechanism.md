# Attention Mechanism 


## 1) Why Attention?

Vanilla Seq2Seq squeezes the whole input into **one fixed vector**. On long inputs this becomes a bottleneck.  
**Attention** fixes it: at each decoding step, the model **looks back** at all encoder states and builds a **fresh, focused context** for the current output token.  

**One-liner:** *Don’t remember everything at once — look where it matters, step by step.*

---

## 2) The core idea (in 4 steps)
For decoder step `t`:  
1. **Scores:** compare decoder’s current state `s_{t-1}` with every encoder state `h_i` → `score_{t,i}`.  
2. **Weights:** `α_{t,i} = softmax_i(score_{t,i})` (across all encoder positions `i`).  
3. **Context:** `c_t = Σ_i α_{t,i} · h_i` (weighted sum).  
4. **Predict:** combine `c_t` with decoder state to predict the next token.  

Mental picture: **spotlight over the input** that slides as the decoder generates each word.

---

## 3) Popular scoring functions (how we compute `score_{t,i}`)
- **Bahdanau (Additive):** `score = vᵀ · tanh(W_s s_{t-1} + W_h h_i)`  
  *Pros:* flexible; *Works great when dims differ.*  
- **Luong (Multiplicative):**  
  - **Dot:** `score = s_{t-1} · h_i`  
  - **General:** `score = s_{t-1}ᵀ W h_i`  
  *Pros:* fast, fewer params; *Dot* is the simplest.  

**Rule of thumb:** If you need speed → **Luong**. If you want flexibility → **Bahdanau**.

---

## 4) Shapes you can remember
- Encoder outputs: `H = [h₁, …, h_Tin]` with shape `[T_in, d_enc]`.  
- Decoder state at step `t`: `s_{t-1}` with shape `[d_dec]`.  
- Scores: `[T_in]` → softmax → attention weights `α_t` `[T_in]`.  
- Context: `c_t = α_t · H` → shape `[d_enc]`.  
- Combine: `[c_t ; s_{t-1}]` (concat) → projection → logits `[vocab_size]`.  

**Sticky note:** *Weights sum to 1; context is a smart average of encoder states.*

---

## 5) Training vs Inference
- **Training:** teacher forcing is still used. Attention weights are learned **end-to-end** by minimizing cross-entropy on target tokens.  
- **Inference:** at each step, compute scores → weights → context → predict next token (greedy or beam search).  
- **Masking:** always mask **padded** encoder positions before softmax (set their scores to `-inf`) so attention never flows to padding.

---

## 6) Global vs Local attention
- **Global:** look over **all** encoder states each step (most common).  
- **Local:** look only around a predicted window (faster; used in long inputs with mostly monotonic alignments like speech).  

Quick choice: start with **Global**; upgrade to **Local** if inputs are huge.

---

## 7) Keras-style pseudocode (readable starter)
from tensorflow.keras.layers import Input, Embedding, LSTM, AdditiveAttention, Concatenate, Dense  
from tensorflow.keras.models import Model  

# Encoder  
enc_inputs = Input(shape=(T_in,))  
x = Embedding(src_vocab, d_embed)(enc_inputs)  
enc_out, h, c = LSTM(d_model, return_sequences=True, return_state=True)(x)  

# Decoder (teacher forcing)  
dec_inputs = Input(shape=(T_out,))  # target tokens shifted right  
y = Embedding(tgt_vocab, d_embed)(dec_inputs)  
dec_lstm = LSTM(d_model, return_sequences=True, return_state=True)  

attn = AdditiveAttention()  # masks must be passed in fit()  

dec_seq, _, _ = dec_lstm(y, initial_state=[h, c])  
context = attn([dec_seq, enc_out])            # shape: [batch, T_out, d_model]  
fusion  = Concatenate()([dec_seq, context])   # combine state + context  
logits  = Dense(tgt_vocab, activation='softmax')(fusion)  

model = Model([enc_inputs, dec_inputs], logits)  
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')  

**Notes:**  
• Pass masks for encoder padding to Attention/AdditiveAttention (Keras can infer from Embedding(mask_zero=True)).  
• For Luong (dot), you can use Attention() instead of AdditiveAttention() or implement scores manually.

---

## 8) Reading attention maps
Plot α_t across i (input positions) for each output step t. You’ll see a heatmap:  
• Sharp diagonal for monotonic tasks (e.g., transliteration).  
• Jumps back/forth for reordering (machine translation).  
• Diffuse weights may indicate confusion → try better regularization or more capacity.  

**Debug mantra:** If outputs look wrong, check the heatmap first.

---

## 9) Common pitfalls & quick fixes
• Forgets long inputs: increase d_model, use multi-head or local + global attention hybrids.  
• Attends to padding: ensure masking works end-to-end.  
• Exposure bias: use scheduled sampling or better decoding (beam, length penalty).  
• Rare/unknown words: consider subword tokenization (BPE/WordPiece) or pointer-generator (copy) in seq2seq tasks.  
• Slow decoding: prune beams, switch to local attention, or move to Transformers for parallel encoder/decoder.

---

## 10) How this leads to Transformers (mental bridge)
• Seq2Seq attention is decoder → encoder (“cross-attention”).  
• Transformers add self-attention inside encoder and decoder, and make attention multi-head (multiple independent “looks”).  
• End result: fully attention-driven models that scale and parallelize better.  

**Memory hook:** RNNs + Attention → idea. Transformers → attention everywhere.

---

## 11) Checklist before shipping
• Tokenization: add <sos>/<eos> on the target side.  
• Padding + masking wired to attention.  
• Teacher forcing on; save tokenizers with the model.  
• Start greedy; add beam search when stable.  
• Visualize attention heatmaps for sanity checks.

---

Attention lets the decoder focus on relevant encoder states every step, replacing the single-vector bottleneck with a dynamic context. Compute scores → softmax → weighted sum → predict. Easy idea, huge impact.