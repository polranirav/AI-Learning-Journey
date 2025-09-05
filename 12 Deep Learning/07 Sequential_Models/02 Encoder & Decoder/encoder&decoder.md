# Encoder–Decoder (Seq2Seq)

## 1) Why Seq2Seq?

Some problems have a sequence in → sequence out shape. Example: English → Hindi translation, text summarization, code generation. The tricky parts:  
• Variable-length input (2 words or 200?).  
• Variable-length output (not 1:1 with input).  
• We must remember order & context across many tokens.  

Seq2Seq handles this by splitting the job in two: an Encoder that reads and compresses the input, and a Decoder that expands that summary into the output sequence.  

⸻

## 2) The one-minute mental model
• Encoder (usually an LSTM/GRU): reads tokens one by one and produces a final hidden state — a compact context vector (a “summary” of the whole input).  
• Decoder (another LSTM/GRU): starts from that context and generates tokens step-by-step until it emits a special `<eos>` (end-of-sequence) token.  
• During training we feed the decoder the gold previous token (teacher forcing) so it learns faster and more stably.  

[Input tokens] → ENCODER → [context vector] → DECODER → [Output tokens]  

**Memorable line:** Encoder packs. Decoder unpacks.  

⸻

## 3) What flows where (shapes you can remember)
Let T_in = input length, T_out = output length, d_model = hidden size.  
• Encoder input: [T_in, d_embed] → LSTM/GRU → final (h_T, c_T) or just h_T.  
• Context passed to decoder init: h0_dec = h_T (and c0_dec = c_T for LSTM).  
• Decoder input at step t: previous target token embedding (training) or previous predicted token (inference) + its recurrent state.  
• Decoder output at step t: logits [vocab_size] → softmax → next token.  

Quick mantra: embed → encode → (h,c) → decode → softmax → token.  

⸻

## 4) Tiny walk-through (English → Hindi)
Say input is “Nice to meet you”.  
Encoder reads: Nice → to → meet → you and ends with a strong state (h_T, c_T) that “remembers” the sentence.  
Decoder starts from that state and prints tokens one by one: आपसे → मिलकर → अच्छा → लगा → `<eos>`.  

At each step we compute a probability over the target vocabulary and pick (or train against) the correct next token.  

⸻

## 5) Training loop (teacher forcing)
For each pair (source_seq, target_seq):  
1. Tokenize & encode both sides (add special tokens: `<sos>`, `<eos>`).  
2. Encode the full source to get context.  
3. Decode target using teacher forcing: feed the gold previous token at every step.  
4. Minimize cross-entropy between predicted distribution and the gold next token.  
5. Repeat across batches/epochs.  

**Rule of thumb:** teacher forcing early, schedule down later if you see exposure bias issues.  

⸻

## 6) Inference (test-time decoding)
• No gold tokens now. Start with `<sos>`, then greedy pick argmax each step, or use beam search for better sequences.  
• Stop at `<eos>` or when you hit a max length.  

**Sticky note:** Training feeds truth; inference feeds itself.  

⸻

## 7) Where vanilla Seq2Seq struggles
• A single fixed context vector can be a bottleneck on long sentences: the encoder must cram everything into one vector, and the decoder must recover the entire meaning from it. That’s hard and leads to drops on long inputs.  
• The decoder would love to peek at specific parts of the input while generating each token, not just one static summary.  

This is exactly why the Attention mechanism was introduced — to let the decoder build a dynamic context per step by softly focusing on relevant encoder states. (We’ll build that in the next file.)  

⸻

## 8) Quick implementation sketch (Keras-style pseudocode)
• Encoder: Embedding → LSTM(return_state=True) → get (h_T, c_T).  
• Decoder: Embedding → LSTM(initial_state=[h_T, c_T]) → Dense(vocab_tgt, softmax).  
• Train with teacher forcing: inputs are (source_seq, target_seq[:-1]), labels are target_seq[1:].  

**Mnemonic:** shift target right for decoder input; predict the next.  

⸻

## 9) Checklist before you code
• Add `<sos>` and `<eos>` on target side.  
• Pad sequences; mask padding in loss.  
• Tie/untie embeddings: your call, but keep dimensions consistent.  
• Save tokenizers with the model: decoding depends on the exact vocab.  
• Start with greedy decoding; add beam search later.  

⸻

## 10) Summary in one breath
Seq2Seq = Encoder (packs input into a context) + Decoder (unpacks into output, token by token). It trains with teacher forcing and predicts with auto-regressive decoding. Classic, clean, and the foundation for attention and transformers you’ll meet next.