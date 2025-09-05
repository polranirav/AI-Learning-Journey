# Types of RNN (with tiny Keras blueprints)

> Quick guide to map your task → the right RNN wiring. Keep it simple, GitHub-friendly, and copy-paste ready.

---

## What this covers
• The 4 common RNN shapes: **One-to-One, Many-to-One, One-to-Many, Many-to-Many**  
• When to use each (typical NLP/CV tasks)  
• Keras mini-templates you can adapt fast  
• Shape cheatsheet + common gotchas  

---

## 0) One-to-One (not really RNN)
**Input:** single item (tabular row / one image) → **Output:** single item (class/score)  
Used for plain **ANN/CNN** classification/regression (no sequence).  
If your data is **not** sequential, you don’t need RNN here.

x ──> [Dense/Conv…] ──> y

---

## 1) Many-to-One
**Input:** a **sequence** → **Output:** **single** label/score  
**Examples:** Sentiment analysis (review → pos/neg), rating prediction (text → 1-5 stars).  

x1 ─┐  
x2 ─┼─> [RNN] ──> [Dense] ──> ŷ  
…  ─┤  
xt ─┘  

**Keras template (LSTM):**
from tensorflow.keras import layers, models  

vocab_size = 10000  
max_len    = 100  

model = models.Sequential([  
    layers.Embedding(vocab_size, 128, input_length=max_len, mask_zero=True),  
    layers.LSTM(128),                          # return_sequences=False (default)  
    layers.Dense(1, activation="sigmoid")      # binary sentiment  
])  
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])  

**Notes**  
• You usually read only the final RNN state → return_sequences=False.  
• Use mask_zero=True in Embedding (or Masking) if you padded sequences.  

---

## 2) One-to-Many
**Input:** single vector → **Output:** sequence  
**Examples:** Image captioning (image → text), music generation (seed → notes).  

┌────────────────────── y1  
h0 (seed) ─>│ [RNN decoder loop] ── y2  
└────────────────────── … yt  

**Keras template (image feature → caption words):**
from tensorflow.keras import layers, models  

feat_dim    = 2048     # e.g., CNN-pooled feature  
max_tgt_len = 20  
tgt_vocab   = 8000  

image_feat = layers.Input(shape=(feat_dim,))  
x = layers.Dense(256, activation="relu")(image_feat)  
x = layers.RepeatVector(max_tgt_len)(x)       # copy seed across time  
x = layers.LSTM(256, return_sequences=True)(x)  
y = layers.TimeDistributed(layers.Dense(tgt_vocab, activation="softmax"))(x)  

model = models.Model(image_feat, y)  
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")  

**Notes**  
• Teacher forcing during training (feed ground-truth tokens) improves stability.  
• Use TimeDistributed(Dense(...)) for per-time-step outputs.  

---

## 3) Many-to-Many (same length)
**Input:** sequence → **Output:** sequence (same time steps)  
**Examples:** NER (tag each word), POS tagging, per-frame event detection.  

x1 ─┐         ┌─> y1  
x2 ─┼─> [RNN] ┼─> y2  
…  ─┤         ┆   …  
xt ─┘         └─> yt  

**Keras template:**
from tensorflow.keras import layers, models  

vocab_size = 20000  
max_len    = 120  
num_tags   = 17   # e.g., BIO tag set  

inp = layers.Input(shape=(max_len,))  
x   = layers.Embedding(vocab_size, 128, mask_zero=True)(inp)  
x   = layers.Bidirectional(layers.LSTM(128, return_sequences=True))(x)  
out = layers.TimeDistributed(layers.Dense(num_tags, activation="softmax"))(x)  

model = models.Model(inp, out)  
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])  

**Notes**  
• Set return_sequences=True to emit output at every time step.  

---

## 4) Many-to-Many (variable length) — Encoder–Decoder
**Input:** sequence A → **Output:** sequence B (different length)  
**Examples:** Machine translation, abstractive summarization.  
Common layout: Encoder reads source; Decoder generates target.  

Encoder (reads x1…xt)        Decoder (writes y1…yT)  


x1 ─┐                         {s} ─┐  
x2 ─┼─> [RNN] ──> (h,c) ────>  y1  ├─> y2 … yT  
  ─┤                           ┘  
xt ─┘  



**Keras template (plain LSTM encoder–decoder):**
from tensorflow.keras import layers, models  

src_vocab, tgt_vocab = 30000, 30000  
src_len,   tgt_len   = 60, 60  
emb = 256  
hid = 512  

# Encoder  
src = layers.Input(shape=(src_len,))  
enc = layers.Embedding(src_vocab, emb, mask_zero=True)(src)  
enc_h, enc_state_h, enc_state_c = layers.LSTM(hid, return_state=True)(enc)  

# Decoder (teacher forcing)  
tgt = layers.Input(shape=(tgt_len,))  
dec = layers.Embedding(tgt_vocab, emb, mask_zero=True)(tgt)  
dec = layers.LSTM(hid, return_sequences=True)(dec, initial_state=[enc_state_h, enc_state_c])  
out = layers.TimeDistributed(layers.Dense(tgt_vocab, activation="softmax"))(dec)  

model = models.Model([src, tgt], out)  
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")  

**Notes**  
• Start/End tokens (<s>, </s>) are required to mark sequence boundaries.  
• Attention (later upgrade) lets the decoder peek at all encoder states.  

---

## Shape cheatsheet

| Pattern                | Input shape to RNN       | Output shape           | Keras knobs                                           |
|------------------------|--------------------------|------------------------|------------------------------------------------------|
| One-to-One             | – (no RNN)               | –                      | Use Dense/CNN                                        |
| Many-to-One            | (batch, time, feat)      | (batch, 1) or (batch,C)| return_sequences=False                               |
| One-to-Many            | (batch, seed_dim)        | (batch, time, C)       | RepeatVector, return_sequences=True, TimeDistributed |
| Many-to-Many (=len)    | (batch, time, feat)      | (batch, time, C)       | return_sequences=True, TimeDistributed               |
| Many-to-Many (≠len)    | [encoder_in, decoder_in] | (batch, tgt_time, C)   | Encoder–Decoder, teacher forcing                     |

---

## When to pick which
• Many-to-One: classify a whole sequence → one label (review → sentiment).  
• One-to-Many: seed → multi-step output (image → caption).  
• Many-to-Many (same): tag each element (word → tag).  
• Many-to-Many (variable): sequence transduction (en → hi translation).  

---

## Common gotchas (read this!)
• Padding & masking: if you pad with 0, use mask_zero=True (Embedding) or layers.Masking(0.0).  
• Wrong return_sequences: False for many-to-one, True when you need per-step outputs or decoders.  
• TimeDistributed mismatch: final Dense must map to the per-step classes (e.g., tags or vocab).  
• Loss choice:  
  - Binary → binary_crossentropy  
  - Multi-class label per step → sparse_categorical_crossentropy  
• Teacher forcing: for decoders, feed the shifted gold target during training.  
• Start/End tokens: needed for decoders to know when to start/stop.  

---

## Quick practice ideas
• Recreate sentiment (IMDB) with Many-to-One.  
• Do NER on CoNLL with Many-to-Many (same length).  
• Build a toy captioner (One-to-Many) using a frozen CNN feature + RNN decoder.  
• Try a tiny translator with an Encoder–Decoder LSTM (then add Attention).  