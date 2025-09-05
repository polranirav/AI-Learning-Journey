# Transformers — a friendly, one-file intro

>  Transformers are a neural-network design built to turn one sequence into another (think: translate, summarize, answer, generate). They dropped RNNs/LSTMs in favor of **self-attention**, which lets models read many tokens **in parallel** and focus on the most relevant parts. That single idea unlocked today’s AI wave—chatbots, code assistants, image/video generation, and more.  

---

## Why did we need Transformers?
- **Seq2Seq with LSTMs worked… until it didn’t.** Long sentences squeezed into one “context vector” lost details; training was slow because inputs were processed **step-by-step**.  
- **Attention fixed most of it.** Instead of one context, the decoder **looks back** to the encoder states with **weights** (attention) at each step.  
- **Final leap (2017):** *Attention Is All You Need* removed RNNs entirely. Pure attention ⇒ **parallel training** ⇒ scale to massive data ⇒ pretrain once, **fine-tune everywhere**.   


## The big idea (in plain words)
A Transformer has two Lego stacks:

1) **Encoder** – Reads the input sequence all at once.  
2) **Decoder** – Writes the output sequence, one token at a time, while attending to the encoder and to what it has already written.

Inside each stack, blocks repeat:
- **Self-Attention:** Every token asks, “Which other tokens matter for me right now?” and mixes information accordingly.  
- **Feed-Forward Network (FFN):** A small MLP applied to each token’s vector to transform it further.  
- **Residual + LayerNorm:** Shortcuts and normalization keep training stable.  
- **Positional Encoding:** Since attention is order-agnostic, add position info so the model knows *who came first/next*.

> **Masking:** In the decoder, masks hide “future” tokens so the model can’t peek ahead while generating.

---

## A tiny (gentle) math peek
- Make three projections per token: **Q** (query), **K** (key), **V** (value).  
- Attention scores = `softmax(Q·Kᵀ / √d)`; output = scores·V.  
- **Multi-Head:** Do that several times with different projections, then concat. Different heads learn different “views” (syntax, coreference, etc.).

---

## Popular shapes (pick what fits your task)
- **Encoder-only** (e.g., BERT-style): Best for *understanding* tasks (classify, tag, retrieve).  
- **Decoder-only** (e.g., GPT-style): Best for *generation* (chat, write, code).  
- **Encoder–Decoder** (e.g., T5-style): Best for classic seq-to-seq (translate, summarize).   

## Why they won (strengths)
- **Scales like crazy:** Parallelism → train on huge datasets.  
- **Transfer learning:** Pretrain once; fine-tune for your niche task with modest data.  
- **Multimodal friendly:** With the right embeddings, text, images, audio—even video—can plug into the same blocks.  
- **Flexible blueprint:** Swap stacks (encoder-only, decoder-only), change depth/width/heads, plug into other tools.  
- **Thriving ecosystem:** Tooling, checkpoints, tutorials, and community everywhere.   

---

## Reality check (limits)
- **Compute-hungry:** Training/inference can be expensive (GPUs/TPUs).  
- **Data-hungry:** Big, diverse corpora help; low-resource domains need care.  
- **Quadratic attention cost:** Long contexts are costly (many variants try to fix this).  
- **Interpretability:** Great results, hard to fully explain decisions.  
- **Bias & ethics:** Models reflect training data; handle safety and licensing responsibly.   

---

## What they power (everyday examples)
- **Chat & assistants:** conversational AI, customer support, agents.  
- **Writer & coder co-pilots:** content drafting, code completion, refactoring.  
- **Translate & summarize:** multilingual support, meeting notes, gist extraction.  
- **Vision & science:** image captioning, visual QA, protein structure modeling, more.   

---

## Build one (minimal mental checklist)
1. **Tokenize** text (subwords are common).  
2. **Embed** tokens (+ add **positional** info).  
3. **Stack** N encoder/decoder blocks (self-attention → FFN, with residual+norm).  
4. **Mask** future tokens in the decoder.  
5. **Train** with a language/seq2seq objective (teacher forcing + cross-entropy).  
6. **Pretrain → Fine-tune** for your downstream task.

---

## Quick glossary
- **Attention:** A learnable way to focus on the most relevant tokens.  
- **Self-Attention:** Attend within the same sequence.  
- **Cross-Attention:** Decoder attends to encoder outputs.  
- **Head:** One attention view; **multi-head** = several views at once.  
- **Context length:** How many tokens the model can “see” at once.  
- **Parameters:** Learnable weights; bigger isn’t always better, but capacity matters.

---

## Roadmap for this folder
- `01_intro_transformers/README.md` (this file)  
- `02_self_attention/` (intuition + math with tiny examples)  
- `03_positional_encoding/` (sinusoidal vs learned)  
- `04_architecture_blocks/` (multi-head, FFN, residual, norm)  
- `05_encoder_only/` (BERT-style tasks)  
- `06_decoder_only/` (GPT-style generation)  
- `07_encoder_decoder/` (T5-style translation/summarization)  
- `08_long_context_variants/` (efficient attention families)  
- `09_training_tips/` (tokenization, batching, masking, LR schedules)  
- `10_serving/` (sampling, beam search, caching, quantization)

---