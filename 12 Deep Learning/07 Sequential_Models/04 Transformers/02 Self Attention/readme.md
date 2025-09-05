# Self-Attention

 Self-attention is a way for each token (word, subword, etc.) in a sequence to look at the other tokens and decide **how much to focus on each of them** before making its next representation. It turns **static** embeddings into **context-aware** embeddings and is the core of Transformers.

---

## Why do we need it?
- The word **“bank”** means different things in “river bank” vs “money bank”. Plain word embeddings can’t change with context.  
- Self-attention **recalculates** a token’s vector by mixing in information from **relevant** tokens in the same sentence/paragraph.

---

## The idea in one sentence
For each token, compute **how similar** it is to every other token, turn those similarities into **weights**, and take a **weighted sum** of everyone’s information.

---

## The 5 steps (forward pass)
Assume you have a sequence of `n` tokens and each token has an embedding of size `d_model`.

1. **Start with embeddings**  
   Matrix `X` of shape `(n, d_model)` — one row per token.

2. **Make Q, K, V (learned projections)**  
Q = X · Wq    (n × d_k)  
K = X · Wk    (n × d_k)  
V = X · Wv    (n × d_v)  

`Wq, Wk, Wv` are trainable matrices.  

Intuition:  
• **Q (Query):** what this token is looking for.  
• **K (Key):** what this token offers.  
• **V (Value):** the actual information carried.  

3. **Similarity scores (who should I attend to?)**  
Scores = Q · Kᵀ   (n × n)  
Each row i compares token i’s query to everyone’s key.

4. **Scale & normalize**  
• **Scale:** divide by `√d_k` to keep numbers stable: `Scores / √d_k`  
• (Optional) **Mask:**  
  – **Padding mask:** ignore padded tokens.  
  – **Causal mask (decoder):** block “future” tokens.  
• **Softmax (row-wise):** turn each row into probabilities:  
Weights = softmax(Scores_scaled)   (n × n)

5. **Mix values**  
Y = Weights · V   (n × d_v)  
Row i in `Y` is token i’s **context-aware** vector: a blend of the values it decided to attend to.  

That’s it: **self-attention output = context-aware embeddings**.

---

## A tiny example (intuition, not exact math)
Sentence: *“Cats chase mice.”*  
• The token **“chase”** will likely put high weight on “Cats” (subject) and “mice” (object).  
• The token **“mice”** may attend more to “chase” (what’s happening to it).  
These weights come from `softmax(QKᵀ/√d_k)`, so each token learns *who matters most*.

---

## Multi-Head Self-Attention (MHSA)
One attention may miss some relations. So we use **h heads**:  
1. Split the model dimension into `h` parts (e.g., `d_model=512`, `h=8`, each head sees `d_k=d_v=64`).  
2. Run the 5-step attention **in parallel per head** (each with its own `Wq, Wk, Wv`).  
3. **Concat** head outputs `(n × (h·d_v))`.  
4. Project back with `Wo` to `(n × d_model)`.  

**Benefit:** different heads can learn different patterns (syntax, long-range links, names, etc.).

---

## Shapes cheat-sheet
• `X`: `(n, d_model)`  
• `Wq, Wk`: `(d_model, d_k)`, `Wv`: `(d_model, d_v)`  
• `Q, K`: `(n, d_k)`, `V`: `(n, d_v)`  
• `Scores = QKᵀ`: `(n, n)`  
• `Weights = softmax(Scores/√d_k)`: `(n, n)`  
• `Y = Weights·V`: `(n, d_v)`  
• MHSA concat: `(n, h·d_v)` → `Wo` → `(n, d_model)`

---

## Positional information (important!)
Self-attention itself doesn’t know order.  
Transformers **add positions** (positional encodings/embeddings) to `X` so the model can tell “who came first”.

---

## Masks (quick guide)
• **Padding mask:** zero out attention to `[PAD]` tokens.  
• **Causal (look-ahead) mask:** in decoders, prevent token *t* from looking at tokens *t+1…n* (so generation is left-to-right).

---

## Complexity & common trade-offs
• **Time/Memory:** attention uses an `(n × n)` matrix → grows quadratically with sequence length.  
• Long texts can be heavy; practical tricks include smaller `d_model`, fewer heads, chunking, or specialized “efficient attention” variants.

---

## Tips & gotchas
• Pick `d_k` so that scaling by `√d_k` keeps logits in a good range for softmax.  
• Always apply the **right mask** (padding/causal), or you’ll leak information.  
• Don’t forget **positional encodings**; without them, the model can’t learn order.  
• Multi-head helps; too many heads without capacity can hurt or overfit.

---

## Mini-glossary
• **Query (Q):** what a token asks about.  
• **Key (K):** what a token can match on.  
• **Value (V):** the info shared if matched.  
• **Head:** one attention unit; multiple heads = multiple views.  
• **`d_k` / `d_v` / `d_model`:** feature sizes for K/Q, V, and model.

---

## One-line summary (formula)
Attention(Q, K, V) = softmax( (Q Kᵀ) / √d_k  [+ mask] ) · V  

With multi-head and positions, this block is the heart of the Transformer.