# What is an RNN? (Recurrent Neural Network)

---

## 1) The idea in one line
An RNN is a neural network for sequences. It reads inputs step by step (time 1, time 2, …), keeps a small memory (hidden state), and uses that memory to make better predictions.

---

## 2) Where sequences show up
- **Text & NLP**: sentences, chat, subtitles, code tokens  
- **Time series**: sales, traffic, sensors, stock prices  
- **Audio & speech**: waveforms, MFCC frames  
- **Biology**: DNA/RNA bases (A,C,G,T)  
Any data where order matters is a sequence.

---

## 3) Why not just ANN or CNN?
- **Variable length**: sentences can be 3 words or 300; dense nets want fixed size.  
- **Order matters**: flattening destroys position information.  
- **Zero-padding hack = waste**: lots of useless zeros → many weights, slow training.  
- **No memory**: plain ANN/CNN (without tricks) doesn’t remember what came before.  

**RNN fix:** read tokens in order and carry context forward as a hidden state.

---

## 4) How an RNN runs (mental model)
At each step *t*, the RNN takes the current input \(x_t\) and the previous hidden state \(h_{t-1}\), then produces a new state \(h_t\) and (optionally) an output \(y_t\).
- **State update (concept)**: \(h_t = f(W_{xh}\, x_t + W_{hh}\, h_{t-1} + b_h)\)  
- **Output (optional)**: \(y_t = g(W_{hy}\, h_t + b_y)\)  
- **Unrolling**: imagine copying the same cell across time steps 1..T (shared weights).  
- **What it learns**: how much of the past to carry and how much of the new input to use.

---

## 5) Common input↔output patterns
| Pattern                 | Example task                         | Shape hint                                 |
|-------------------------|--------------------------------------|---------------------------------------------|
| Many→One                | Sentiment of a review                | inputs: (T, features) → one label           |
| Many→Many (aligned)     | POS tagging (one tag per token)      | inputs: (T, features) → (T, classes)        |
| Many→Many (seq2seq)     | Translation (src→tgt)                | encoder (T_src, feat) → decoder (T_tgt, classes) |
| One→Many                | Music generation from a prompt       | one start token → a sequence                |

**Tip:** In Keras, batch adds one more axis, so you often see **(batch, T, features)**.

---

## 6) Shapes & data prep (quick guide)
- **Batch major**: (batch, T, features) is the standard.  
- **Text**: tokenize → integer ids → **Embedding** layer (maps ids to vectors).  
- **Padding**: pad shorter sequences to a max T; use **masking** so the model ignores pads.  
- **Scaling**: for numeric time series, normalize features (e.g., z-score or min–max).

---

## 7) Training RNNs (the short story)
- **BPTT (Backprop Through Time)**: gradients flow across steps.  
- **Truncated BPTT**: for long sequences, backprop only *k* steps to save memory/time.  
- **Gradient clipping**: cap gradients (by value or norm) to control exploding updates.  
- **Teacher forcing (seq2seq)**: during training, feed the true previous token to the decoder.

---

## 8) Strengths and limits
**Strengths**
- Respects order and context  
- Works well on moderate-length sequences  
- Simple to prototype (Keras SimpleRNN, LSTM, GRU)  

**Limits**
- Vanishing/exploding gradients on long sequences  
- Hard to model very long dependencies  
- Usually slower than CNN/Transformer for long texts  

**Practical fix:** prefer **LSTM** or **GRU** over vanilla RNN; add clipping, good init, dropout. For very long text, look at **Transformers**.

---

## 9) RNN family (when to use what)
- **SimpleRNN**: teaching & tiny problems; short contexts.  
- **LSTM**: adds gates + cell state → better long-memory. Default safe choice.  
- **GRU**: like LSTM but fewer parameters; often as good, faster.  
- **Bidirectional**: read left→right and right→left; great for tagging/classification (not for streaming).  
- **Stacked (deep)**: multiple layers for richer features—watch overfitting.

---

## 10) Mini glossary (plain words)
- **Step / time step (t)**: the current token/frame in the sequence.  
- **Hidden state (h_t)**: the RNN’s memory at step t.  
- **Masking**: tells the model which positions are padding (ignore them).  
- **Teacher forcing**: training trick for decoders to converge faster.  
- **Truncated BPTT**: backprop only a fixed number of steps for efficiency.

---

## 11) One-minute example (mentally simulate)
**Sentiment (movie review):**  
You feed word embeddings one by one: “movie → was → surprisingly → good”.  
At each step, the state updates; by the end, the state encodes the overall feel.  
Final dense layer maps that state to **Positive / Negative**.

---

## 12) Memory hooks (recall fast)
- **RNN = step-by-step + memory (h_t)**.  
- Use for ordered data (text, time series, audio).  
- **Shapes**: (batch, T, features); **pad + mask**.  
- Train with **BPTT**; add **clipping**; prefer **LSTM/GRU** for longer context.  
- Pick IO pattern: **many→one** (classify), **many→many** (tag), **seq2seq** (translate).

---