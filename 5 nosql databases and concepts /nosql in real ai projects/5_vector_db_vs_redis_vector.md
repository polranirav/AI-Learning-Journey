
# 🧲 5 – Vector DBs vs Redis Vector Search for AI Embeddings

Storing and searching **high-dimensional vectors** is critical in modern AI systems — for tasks like:

- Semantic search
- Embedding lookups
- RAG (Retrieval-Augmented Generation)

Let’s compare two popular approaches:
- **Redis (with Vector Search module)**
- **Dedicated Vector DBs** like Pinecone, FAISS, Weaviate

---

## 🧩 When Are Vector DBs Needed?

| AI Use Case              | Why Vectors Matter                  |
|--------------------------|--------------------------------------|
| Semantic document search | Match meaning, not exact text        |
| Image similarity         | Match based on latent features       |
| Question-answering bots  | Retrieve from context using embeddings |
| Personalized recs        | Store user/item embeddings           |

---

## 📌 Example: Query with Redis vs Pinecone

### Prompt:
> "Find me FAQs similar to: 'What’s your refund policy?'"

### Backend:
- User query → Convert to embedding
- Query DB for nearest neighbor
- Return top matches

---

## ⚙️ Redis Vector Search Overview

Requires Redis Stack or RediSearch module (>= v2.4+).

### Example Schema (128-dim vector):

```bash
FT.CREATE faqs_idx ON HASH PREFIX 1 faq: SCHEMA
  question TEXT
  embedding VECTOR FLAT 6
  DIM 128
  TYPE FLOAT32
  DISTANCE_METRIC COSINE
```

### Add Item:

```python
r.hset("faq:1", mapping={
    "question": "What is the return policy?",
    "embedding": np_array.tobytes()
})
```

### Search:

```python
query = Query("*=>[KNN 3 @embedding $vec]")
query.dialect(2)
results = r.ft("faqs_idx").search(query, {"vec": user_vector.tobytes()})
```

---

## ⚙️ Pinecone Overview (Cloud Vector DB)

```bash
pip install pinecone-client
```

```python
import pinecone

pinecone.init(api_key="...", environment="us-east1-gcp")
index = pinecone.Index("faq-index")

index.upsert([
    ("faq1", user_vector.tolist(), {"question": "What’s your return policy?"})
])
```

### Query:

```python
index.query(vector=user_vector.tolist(), top_k=3, include_metadata=True)
```

---

## 🧠 Redis vs Vector DBs (Side-by-Side)

| Feature                | Redis Vector         | Pinecone / FAISS     |
|------------------------|----------------------|-----------------------|
| Setup                  | Self-hosted (or Redis Cloud) | Fully managed (Pinecone) |
| Latency                | Very low             | Low                   |
| Index customization    | Limited              | Extensive (HNSW, IVF, etc.) |
| Vector size            | Up to 4096 (Redis 7.2+) | 100k+ scale optimized |
| Scalability            | Moderate             | High (cloud-native)   |
| Text support           | Full RediSearch      | Depends on platform   |
| Use case fit           | Light to medium AI workloads | Large-scale RAG, e-commerce search |

---

## 💼 When to Use What?

| Situation                            | Choose              |
|--------------------------------------|----------------------|
| You already use Redis + want simple vector search | ✅ Redis Vector |
| You need production-grade RAG at scale            | ✅ Pinecone / Weaviate |
| You work offline or on-device                     | ✅ FAISS (local) |
| You need full document + vector hybrid search     | ✅ Redis or Weaviate |

---

## 🧠 Best Practices for AI Projects

- Normalize all vectors (L2 norm)
- Store both `metadata + vector` together
- Use cosine distance for semantic similarity
- Keep dimensionality ≤ 1536 (e.g. OpenAI embeddings)

---

📁 **Next File:** [`6_finetuning_logs_in_mongodb.md`](./6_finetuning_logs_in_mongodb.md)