# LSTM — Long Short-Term Memory 

LSTM = RNN with two memories (long-term C_t and short-term h_t) + three gates (forget, input, output). It remembers what matters, forgets what doesn’t, and predicts step-by-step on sequences (text, audio, time-series).

⸻

## Why LSTM
Plain RNNs struggle on long sequences: gradients vanish/explode, early context is forgotten. LSTM fixes this with a cell state that can carry information untouched for many steps, controlled by gates. Result: better long-range dependencies, more stable training.

⸻

## Core mental model (easy words)
• Think of each time step t as a mini computer.  
• It reads the current input x_t and the previous short memory h_{t-1}.  
• It updates a long memory C_t (what to keep for the future).  
• It produces a short memory / output h_t (what to say right now).

**Two memories**  
• C_t (cell state) → long-term context “pipeline”.  
• h_t (hidden state) → short-term context used to make the next decision.

⸻

## The three gates (simple)
At every time step, we compute 3 filters using x_t and h_{t-1}:

1) Forget gate:  
f_t = σ(W_f [x_t, h_{t-1}] + b_f)  
Decides what fraction of old long memory to keep.  
C_{t-1} passes through f_t ⊙ C_{t-1} (⊙ = element-wise multiply).  
If f_t ≈ 1 → keep; if ≈ 0 → drop.

2) Input gate (two parts):  
• “Should we write?” i_t = σ(W_i [x_t, h_{t-1}] + b_i)  
• “What to write?” candidate g_t = tanh(W_g [x_t, h_{t-1}] + b_g)  
New info added: i_t ⊙ g_t.

3) Output gate:  
o_t = σ(W_o [x_t, h_{t-1}] + b_o)  
What portion of long memory to reveal now.

**State updates (the 5 tidy equations)**  
f_t = σ(W_f [x_t, h_{t-1}] + b_f)  
i_t = σ(W_i [x_t, h_{t-1}] + b_i)  
g_t = tanh(W_g [x_t, h_{t-1}] + b_g)  
C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t  
o_t = σ(W_o [x_t, h_{t-1}] + b_o)  
h_t = o_t ⊙ tanh(C_t)

⸻

## Forward flow (one sequence, step-by-step)
For each token/time point:  
1) Read x_t and h_{t-1}.  
2) Compute f_t, i_t, g_t, o_t.  
3) Update long memory: C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t.  
4) Emit short memory/output: h_t = o_t ⊙ tanh(C_t).  
5) Move to t+1 with (C_t, h_t).

**Shapes (typical):**  
• Input batch: (B, T, F) → batch, timesteps, features (or token ids).  
• LSTM hidden size: H.  
• Then h_t, C_t each have shape (B, H) per step.

⸻

## When to use LSTM
• NLP (sentiment, sequence labeling, simple translation), Speech/Audio (keyword spotting), Time-series (forecasting, anomaly detection).  
• Great when data size is moderate, latency is tight, or training a transformer is overkill.

⸻

## Keras quick-start (two useful templates)

1) Text Sentiment (Embedding + BiLSTM)

from tensorflow.keras.datasets import imdb  
from tensorflow.keras.preprocessing.sequence import pad_sequences  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Embedding, LSTM, Bidirectional, Dense, Dropout  

# 1) Load & prepare data  
num_words = 10000  
maxlen = 200  
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=num_words)  
X_train = pad_sequences(X_train, maxlen=maxlen, padding='post', truncating='post')  
X_test  = pad_sequences(X_test,  maxlen=maxlen, padding='post', truncating='post')  

# 2) Build model  
model = Sequential([  
    Embedding(input_dim=num_words, output_dim=128, input_length=maxlen, mask_zero=True),  
    Bidirectional(LSTM(64, return_sequences=False)),  
    Dropout(0.3),  
    Dense(1, activation='sigmoid')  
])  

# 3) Train & evaluate  
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  
model.summary()  
model.fit(X_train, y_train, validation_split=0.1, epochs=3, batch_size=128)  
model.evaluate(X_test, y_test)  

Notes:  
• mask_zero=True ignores padding tokens (nice for variable length).  
• Bidirectional often boosts accuracy in NLP.

2) Time-Series Forecast (Many-to-One)

from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import LSTM, Dense  

# Suppose X has shape (B, T, n_features) and y has shape (B, 1)  
model = Sequential([  
    LSTM(64, input_shape=(T, n_features)),  
    Dense(1)  # regression  
])  
model.compile(optimizer='adam', loss='mse')  
model.summary()  
model.fit(X, y, epochs=20, batch_size=64, validation_split=0.1)

⸻

## Many-to-One / One-to-Many / Many-to-Many (map to Keras)
• Many→One (e.g., sentiment): last output only → LSTM(..., return_sequences=False) then Dense(...).  
• Many→Many (e.g., NER, per-time-step labels): LSTM(..., return_sequences=True) then TimeDistributed(Dense(...)).  
• Encoder→Decoder (seq2seq): stack/bridge two RNNs; pass final encoder states to decoder.

⸻

## Training checklist (memorable!)
• Tokenize/Pad text → same length per batch; or mask padding.  
• Embedding > one-hot for NLP (dense, semantic).  
• return_sequences:  
  – False → one output (classification/regression).  
  – True → output at every step (sequence labeling/decoding).  
• Dropout: regularize (Dropout on outputs; recurrent_dropout inside LSTM if needed).  
• Clip grads for stability: optimizer=Adam(clipnorm=1.0) or clipvalue=1.0.  
• EarlyStopping + ReduceLROnPlateau callbacks.  
• Batch size: try 32/64/128; tune with validation.  
• Stacked LSTMs: deeper = more expressive (e.g., two layers, top return_sequences=False).  
• Bidirectional for text; Stateful LSTM for streaming time-series (advanced).  
• Scaling numeric features (time-series) helps a lot.

⸻

## Common gotchas (avoid these!)
• Forgetting to mask padding → model learns “length” instead of content.  
• Huge sequences with small LSTM → underfit; either increase H, use BiLSTM, or trim with sliding windows.  
• Exploding gradients → always consider gradient clipping.  
• Too much recurrent_dropout on GPU → slow; prefer outer Dropout first.  
• Imbalanced classes → use class weights or better sampling.

⸻

## LSTM vs GRU (quick pick)
• GRU (fewer gates) trains faster, similar accuracy on many tasks.  
• Start with GRU for speed; switch to LSTM if you need stronger long-term control or you observe performance gaps.

⸻

## Minimal math (only what you’ll remember)
• Gates are sigmoid filters: numbers between 0 and 1 that decide flow.  
• Candidate info is tanh: proposes new content.  
• Long memory update = forget old + write new.  
That’s the essence of LSTM’s stability.

⸻

## Interpreting shapes (tiny table)
• Input (B, T, F) → Embedding → (B, T, E).  
• LSTM(H, return_sequences=False) → (B, H).  
• LSTM(H, return_sequences=True)  → (B, T, H).  
• Final Dense for:  
  – Binary sentiment: Dense(1, activation='sigmoid').  
  – Multi-class per step: TimeDistributed(Dense(K, activation='softmax')).  
  – Regression: Dense(1).

⸻

## Performance tips (practical)
• Use GPU; enable mixed precision on modern GPUs for speed.  
• Keep sequences reasonably short (truncate/pad) unless necessary.  
• Pretrained embeddings (Word2Vec/GloVe/FastText) can help when data is small.  
• For speech/time-series, consider CNN→LSTM hybrids (Conv extracts local patterns, LSTM handles order).

⸻

## Tiny “from scratch” example (manual shapes)
Imagine vocab size V=10k, sequence length T=50, hidden size H=64:  
• Embedding → (B, 50, 128).  
• BiLSTM(64) → (B, 128) because forward+backward concatenate.  
• Dense(1, sigmoid) → sentiment score.

⸻

## Debugging flow (what to check if accuracy is stuck)
1) Is padding masked? (mask_zero=True or Masking() layer)  
2) Is return_sequences set correctly for your task?  
3) Try smaller model first (e.g., H=32), verify it overfits a tiny subset.  
4) Increase capacity, add dropout, tune LR.  
5) Inspect tokenization (OOV handling, vocab size).  
6) For time-series, check windowing/target alignment.

⸻

## One-page recap (yaad rakhna!)
• Two memories: C_t (long), h_t (short).  
• Three gates: forget (what to drop), input (what to add), output (what to reveal).  
• Stable training on long sequences, better context retention.  
• Use Embedding + (Bi)LSTM for text, LSTM for time-series.  
• Get the shapes and return_sequences right → half the battle won.