
# 🏗️ 8 – NoSQL DB Design for Real AI Projects (MongoDB Example)

Designing your **database schema** is crucial in production AI systems.

In NoSQL (especially MongoDB), it’s not about **normalization** like SQL — it’s about **performance, flexibility, and fast retrieval** of JSON-like documents.

---

## 🧩 AI Project Scenario: Chatbot + Logging + Feedback + Vector Search

Your AI app has:

- 👤 Users interacting with a chatbot
- 💬 Prompts and responses from LLMs
- ⭐ Feedback and ratings on responses
- 🧠 Embeddings for semantic search

---

## 🧱 NoSQL Schema Design Overview

| Collection         | Purpose                            |
|--------------------|-------------------------------------|
| `users`            | Store user info & preferences       |
| `chat_logs`        | Log conversations w/ prompts & replies |
| `feedback`         | Store likes/dislikes per response   |
| `embeddings`       | Store vector representations        |
| `configs`          | Store model version, settings       |

---

## 📄 Sample Document Structures

### `users`:

```json
{
  "_id": "user_42",
  "email": "test@example.com",
  "signup_date": "2025-07-25",
  "plan": "free",
  "language": "en"
}
```

---

### `chat_logs`:

```json
{
  "_id": "log_123",
  "user_id": "user_42",
  "prompt": "What is AI?",
  "response": "Artificial Intelligence is...",
  "model_used": "gpt-4",
  "timestamp": "2025-07-25T20:01:00Z"
}
```

---

### `feedback`:

```json
{
  "chat_id": "log_123",
  "user_id": "user_42",
  "rating": "thumbs_up",
  "comment": "Great answer!",
  "timestamp": "2025-07-25T20:03:00Z"
}
```

---

### `embeddings`:

```json
{
  "doc_id": "log_123",
  "vector": [0.21, 0.38, 0.44, ...],  // 1536-d
  "model": "text-embedding-ada-002",
  "source": "chat_logs"
}
```

---

### `configs`:

```json
{
  "experiment": "gpt4_rag_v2",
  "temperature": 0.7,
  "top_k": 5,
  "use_vector_search": true,
  "timestamp": "2025-07-25T20:10:00Z"
}
```

---

## 🧠 Query Patterns (Access Matters!)

| Task                         | Query Example                              |
|------------------------------|--------------------------------------------|
| Get all logs for a user      | `find({"user_id": "user_42"})`             |
| Get feedback on bad answers  | `find({"rating": "thumbs_down"})`          |
| Fetch all vectors for search | `find({}, {"vector": 1})`                  |
| Group logs by model          | `aggregate({"$group": {"_id": "$model"}})` |

---

## 🏎️ Performance Tips

| Tip                        | Description                            |
|----------------------------|-----------------------------------------|
| Use ObjectId for `_id`     | Mongo’s default is fast and efficient  |
| Index `user_id`, `timestamp` | Critical for queries                  |
| Avoid joins via `$lookup`  | Use embedded docs or denormalize       |
| Limit document size        | Stay under 16MB cap                    |

---

## 🛡️ AI Deployment Benefits of This Design

- Logs are instantly traceable by user
- Feedback can be linked to model version
- Vectors can be searched for RAG workflows
- Pipelines can evolve without schema migrations

---

## 🧰 Tools to Help You Design

- [MongoDB Compass](https://www.mongodb.com/products/compass) – GUI visualizer
- [Atlas Charts](https://www.mongodb.com/atlas/charts) – built-in dashboards
- [NoSQLBooster](https://nosqlbooster.com/) – intelligent query IDE

---

## ✅ Final Notes

- MongoDB is perfect for **flexible AI pipelines** with evolving structure
- Think in terms of **access patterns** not normalization
- Use `"source"` or `"experiment"` to tag every doc for traceability

---

🎯 This file ties together everything you've learned: FastAPI APIs, vector caching, streaming logs, fine-tune storage — all into **real MongoDB document modeling**.