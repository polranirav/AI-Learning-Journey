# LLMs_Primer — Large Language Models (LLMs)

## memory hooks

- **LLM = next-token predictor.** It reads a sequence of tokens and predicts the next one.
- **Transformer inside.** Self-attention lets every token “look at” other tokens.
- **Quality = data × model × decoding.** Good prompts and decoding matter as much as size.
- **Context window rules.** If it’s not in the window (or training), the model can’t “know” it.
- **RAG beats raw recall.** Retrieve facts first, then ask the model to reason over them.
- **Guardrails always.** Expect hallucinations; constrain outputs; verify.

---

## What is an LLM?

A **Large Language Model** is a neural network trained to **predict the next token** (a sub-word piece) given previous tokens. With enough data and compute, this simple objective learns **grammar, style, facts, and patterns**. At inference, repeating “predict next token” produces text, code, answers, or plans.

**Great at:** drafting, summarizing, Q&A, conversion (JSON/CSV), code help, brainstorming.  
**Weak at:** exact facts, math with long chains, very long contexts, fresh news, private data.

---

## A tiny glossary

- **Token:** a chunk of text (≈ 3–5 characters on average).
- **Context window:** max tokens the model can read at once (input + its own output).
- **Embedding:** numeric vector for each token.
- **Self-attention:** score of “how much should token A attend to token B”.
- **Head / multi-head:** parallel attention “views”.
- **Transformer block:** LayerNorm → Attention (+ residual) → MLP (+ residual).
- **Logits:** raw scores before softmax.
- **Decoding:** how we pick tokens from logits (greedy, top-k, top-p, etc.).

---

## How an LLM works (mental model in 5 steps)

1) **Tokenize** input text → `[t1, t2, ..., tN]`  
2) **Embed + positional info** → vectors that capture meaning + order  
3) **Stacked Transformer blocks**  
   - Queries/Keys/Values computed per token  
   - **Causal mask** stops peeking at the future  
   - Residual + normalization keep training stable  
4) **Output head** maps each token state to vocabulary logits  
5) **Decode** logits into the **next token**; append and repeat

> Think of it as: *look at all prior tokens → decide what’s likely next → commit → repeat.*

---

## Training stages (why models feel helpful)

- **Pretraining (unsupervised):** predict next token on massive text. Learns language + world patterns.
- **Supervised fine-tuning (SFT):** train on *instruction → response* pairs. Learns to follow directions.
- **Preference optimization (DPO/RLHF-like):** teach “which responses are preferred”. Aligns tone, safety.
- **Task fine-tuning / adapters (LoRA):** cheap specialization to your domain without retraining the base.

---

## Decoding 101 (how sampling changes behavior)

- **Greedy:** take the top logit. Deterministic, fast, can be dull or stuck.
- **Beam search:** keep several best partial sequences. Better for exact tasks; costly; can be verbose.
- **Top-k sampling:** sample from the top *k* tokens only. More creative, less nonsense than pure softmax.
- **Top-p (nucleus):** sample from the smallest set whose probabilities sum to *p* (e.g., 0.9). Adapts per step.
- **Temperature:** scale logits before sampling. `<1` = precise, `>1` = diverse.
- **Repetition penalties:** reduce score of seen tokens to avoid loops.

**Rule of thumb**
- Factual/tasky → `temperature≈0–0.3`, `top_p≈0.1–0.5`, maybe greedy/beam.
- Creative/brainstorm → `temperature≈0.7–1.0`, `top_p≈0.8–0.95`, avoid beam.

---

## Prompting patterns that actually help

- **Set the role + goal:** “You are a strict validator. Task: check JSON schema.”
- **Give constraints:** length, format, tone, *what not to do*.
- **Show 1–3 examples:** few-shot beats long essays.
- **Use delimiters:** triple backticks or XML-ish tags to fence inputs.
- **Ask for structure:** “Return valid JSON with keys: `answer`, `confidence`.”
- **Force steps (when needed):** “Think step-by-step; show the final answer in one line.”
- **Refuse gracefully:** “If unsure, say ‘I don’t know’ and request info.”
- **Test prompts:** keep a tiny suite of representative cases and check outputs.

**Anti-patterns**
- Vague asks, mixed goals, hidden constraints, and unbounded outputs.

---

## RAG (Retrieval-Augmented Generation) in one glance

When you need **fresh or niche facts**, don’t rely on the model’s memory. Instead:

1) **Ingest:** chunk your docs, compute embeddings, store in a vector DB.  
2) **Retrieve:** for a query, get top-k relevant chunks.  
3) **Compose prompt:** instructions + retrieved snippets + the question.  
4) **Generate & cite:** have the model answer *using only* retrieved context.  
5) **Verify:** optionally re-rank, cross-check, or ask the model to justify with quotes.

Benefits: higher factuality, traceability, smaller models can punch above their weight.

---

## Evaluating LLM systems (simple and pragmatic)

- **Functional tests:** given inputs X, outputs match patterns/JSON schema.
- **Task metrics:** accuracy/F1 (classification), BLEU/ROUGE (gen), exact match (QA), latency, cost.
- **Adversarial tests:** prompt injection, jailbreak attempts, toxic content.
- **Human review:** small curated set; rubric for correctness, helpfulness, safety.
- **Regression suite:** lock prompts; compare outputs over time.

---

## Safety & limits (always assume fallibility)

- **Hallucinations:** model states facts with confidence; verify critical claims.
- **Privacy:** never paste secrets into prompts; redact or use secure pathways.
- **Bias & harm:** filter inputs, constrain outputs, add refusal rules.
- **Over-generalization:** model may apply patterns where they don’t fit.
- **Context overflow:** once over the window, earlier tokens are dropped or compressed.

**Mitigations**
- Constrain format; validate; post-process; use RAG; chain small, checkable steps.

---

## Practical build choices

- **Model size vs. latency:** small (fast, worse quality) ↔ large (slow, better).
- **Context length:** long windows help retrieval and coding sessions; cost ↑ with tokens² in attention.
- **Quantization:** 8-bit/4-bit can cut memory and latency with minor quality loss.
- **Adapters (LoRA):** add domain skill cheaply; keep the base frozen.
- **Caching:** reuse KV-cache for long chats to speed up continuation.

---

## Mini “cheat sheet” (stick this by your keyboard)

- **If answers are fluffy:** lower temperature; ask for bullet points + JSON.
- **If facts are wrong:** add RAG; quote sources; say “do not guess”.
- **If it ignores format:** show a *tiny* example and say “match this exactly”.
- **If it’s too verbose:** set word budget; “no preamble”; “final answer only”.
- **If it’s stuck:** reframe the task; add one example; remove distractors.
- **If cost/latency hurts:** shorter prompts; smaller model; quantize; cache.

---

## Minimal generation pseudo-code (for intuition)

```python
def generate(model, tokenizer, prompt, max_new_tokens=128, temperature=0.7, top_p=0.9):
    ids = tokenizer.encode(prompt)
    for _ in range(max_new_tokens):
        logits = model.forward(ids)              # last-token logits
        logits = logits / max(temperature, 1e-6)
        probs  = softmax(logits)
        probs  = nucleus_filter(probs, p=top_p)  # keep smallest mass ≥ p; renormalize
        next_id = sample(probs)                  # or argmax for greedy
        ids.append(next_id)
        if next_id == tokenizer.eos_id: break
    return tokenizer.decode(ids)
```
## Folder hints (how this connects to the rest of your repo)
-  Put this file in 05_LLMs_Primer/README.md.
-  Add small notebooks:
-  prompting_playground.ipynb — try temperature/top-p and prompt styles.
-  decode_strategies.ipynb — compare greedy vs. top-k vs. top-p on the same prompt.
-  Keep a prompts/ folder with tested prompts and fixtures for regression checks.

## Key mantra

-  Encode → Attend → Predict → (Retrieve) → Verify.

