# Sentiment Analysis with RNNs (Keras) — README

Build a small, end-to-end sentiment classifier for movie reviews using Recurrent Neural Networks. Plain words, clear shapes, and working Keras code.

⸻

## 1) What you’ll build (and why RNN?)
	•	We’ll train a model that reads a sequence of tokens (a review) and predicts positive (1) / negative (0).
	•	RNNs read text step-by-step and carry a small memory (hidden state) so order matters.
	•	Two encodings you’ll see:
	•	Integer / one-hot (simple but heavy/limited)
	•	Embedding (dense vectors that capture meaning — recommended)

⸻

## 2) Data to numbers (the essential pipeline)
	1.	Tokenize text → build a vocabulary and map each word to an integer id.
	2.	Pad sequences to a fixed length T (e.g., 50 or 200) so batches are rectangular.
	3.	(Option A) One-hot each token to size V (vocab) → big feature size.
		(Option B) Feed integer ids into an Embedding layer → compact feature size d.
	4.	Feed shape to the model as (batch, T, features); with Embedding, features = d.

**Good practices**
	•	Use an OOV (out-of-vocabulary) token for unknown words.
	•	Use masking so padded 0’s are ignored by the model.
	•	Keep a train/val split to watch overfitting.

⸻

## 3) RNN forward pass (tiny math you should remember)
For time steps t = 1..T:
	•	State update: h_t = tanh(W_xh x_t + W_hh h_{t-1} + b_h)
	•	Output: ŷ_t = σ(W_hy h_t + b_y) (sigmoid for binary; softmax for multi-class)
	•	Initial state: h_0 = 0 (or learned/passed state)
	•	Parameter count (SimpleRNN): if input feature size is F and hidden size is H,
	params = F·H + H·H + H (input→hidden + hidden→hidden + bias).
	Example: F=32, H=64 → 32*64 + 64*64 + 64 = 2048 + 4096 + 64 = 6208.

⸻

## 4) Output patterns (pick one that fits your task)

| Pattern                         | Keras setting              | When to use                                  |
|---------------------------------|----------------------------|----------------------------------------------|
| Many→One (use last step only)   | `return_sequences=False`   | Review sentiment, sequence classification    |
| Many→Many (output every step)   | `return_sequences=True`    | Tagging per token, step-wise flags           |
| Seq2Seq (encoder→decoder)       | separate encoder/decoder   | Translation, captioning                      |

⸻

## 5) Option A (educational baseline): integer ids → SimpleRNN (no Embedding)

⚠️ Not recommended for real projects (ids have no numeric meaning). Kept here to mirror the simple approach and show shapes.

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Masking

# 1) Load IMDB (pre-tokenized to integer ids)
num_words = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# 2) Pad/truncate to fixed T
T = 50  # try 200 on a stronger machine
x_train = pad_sequences(x_train, maxlen=T, padding="post", truncating="post")
x_test  = pad_sequences(x_test,  maxlen=T, padding="post", truncating="post")

# 3) (Hack) Treat each id as a 1-d feature at each time-step
x_train = x_train[..., None].astype("float32")  # (batch, T, 1)
x_test  = x_test[..., None].astype("float32")

# 4) Build a minimal RNN classifier (many→one)
model = Sequential([
    Masking(mask_value=0.0, input_shape=(T, 1)),  # ignore padded zeros
    SimpleRNN(32, return_sequences=False),         # hidden size 32
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(x_train, y_train, epochs=3, batch_size=128,
                    validation_split=0.2, verbose=1)

print("Test accuracy:", model.evaluate(x_test, y_test, verbose=0)[1])
```

**What to expect**
	•	Trains fast, but accuracy is limited (ids carry arbitrary magnitudes).
	•	Use this only to understand the forward flow and shapes: (batch, T, 1).

⸻

## 6) Option B (recommended): Embedding → SimpleRNN (or LSTM/GRU)

Better results with a small dense vector per word. This is the standard recipe.

```python
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, GRU, Dense

# 1) Load IMDB, keep top-k words
num_words = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# 2) Pad to fixed length
T = 200  # longer context generally helps
x_train = pad_sequences(x_train, maxlen=T, padding="post", truncating="post")
x_test  = pad_sequences(x_test,  maxlen=T, padding="post", truncating="post")

# 3) Build model: Embedding -> (choose ONE RNN) -> Dense
embed_dim = 64   # try 16/32/64; higher = richer features
hidden    = 64   # try 32/64/128

model = Sequential([
    Embedding(input_dim=num_words, output_dim=embed_dim, input_length=T, mask_zero=True),
    # Choose ONE of the following:
    SimpleRNN(hidden, return_sequences=False),
    # GRU(hidden, return_sequences=False),
    # LSTM(hidden, return_sequences=False),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(x_train, y_train, epochs=3, batch_size=128,
                    validation_split=0.2, verbose=1)

print("Test accuracy:", model.evaluate(x_test, y_test, verbose=0)[1])
```

**Why this works better**
	•	Dense vectors (embeddings) → smaller, meaningful features.
	•	Model sees context via RNN and semantics via embeddings.
	•	With LSTM/GRU you usually get higher accuracy and more stable training.

⸻

## 7) Understanding return_sequences (quick clarity)
	•	False (default): you get only the last output → suitable for review sentiment.
	•	True: you get all time steps → use for token tagging or feeding a decoder.

⸻

## 8) Common pitfalls (save your time)
	•	Forgetting masks: set mask_zero=True in Embedding (and use Masking for manual inputs) so pads don’t pollute learning.
	•	Tiny T: trimming to very short sequences (e.g., T=50) is fast but may hurt accuracy; start small, then grow.
	•	No validation: always keep validation_split or a separate val set to watch overfitting.
	•	Ignoring class balance: IMDB is balanced, but other datasets may not be — watch metrics beyond accuracy.
	•	Feeding ids as numbers (Option A) in production: avoid; use Embedding (Option B).

⸻

## 9) Useful knobs (tune these first)
	•	embed_dim (e.g., 32 → 128): richer word meaning.
	•	hidden size (e.g., 32 → 128): more capacity; slower.
	•	T (sequence length): keep what covers most reviews (e.g., 200).
	•	Cell type: SimpleRNN < GRU < LSTM (usually).
	•	Regularization: add Dropout/recurrent_dropout in the RNN; SpatialDropout1D after Embedding.
	•	Optimizer: start with Adam; reduce lr if training is noisy.

⸻

## 10) Shape cheat-sheet

| Stage                            | Shape                   |
|----------------------------------|-------------------------|
| Padded tokens                    | (batch, T)              |
| After Embedding                  | (batch, T, embed_dim)   |
| RNN (return_sequences=False)     | (batch, hidden)         |
| RNN (return_sequences=True)      | (batch, T, hidden)      |
| Final Dense (binary)             | (batch, 1)              |

⸻

## 11) Quick upgrade paths
	•	Swap SimpleRNN → LSTM/GRU for longer context handling.
	•	Make it Bidirectional: `tf.keras.layers.Bidirectional(LSTM(...))` for offline tasks.
	•	Try pretrained embeddings (GloVe/word2vec) or SentencePiece/BPE tokenization.
	•	Add EarlyStopping and ReduceLROnPlateau callbacks to train cleanly.

⸻

## 12) Memory hooks (remember these 5 lines)
	•	RNN update: h_t = tanh(W_xh x_t + W_hh h_{t-1} + b_h)
	•	Binary head: ŷ = σ(W_hy h_T + b_y) (use last step)
	•	Params (SimpleRNN): F·H + H·H + H
	•	Mask pads: Embedding(..., mask_zero=True) or Masking(mask_value=0)
	•	Use Embedding: integer ids → dense, meaningful vectors → better results

⸻

	•	Tokenize → Pad → Embedding → (LSTM/GRU) → Dense(sigmoid).
	•	Start simple, watch shapes, and let the model learn the meaning from data.