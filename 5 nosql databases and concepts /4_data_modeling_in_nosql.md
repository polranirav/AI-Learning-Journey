# 🧩 4 – Data Modeling in NoSQL

Unlike relational databases where data modeling is schema-first and normalized, **NoSQL data modeling is application-first** and designed for performance, flexibility, and scale — perfect for fast-changing AI systems.

---

## 🧠 Key Modeling Differences

| Concept               | SQL                           | NoSQL                          |
|------------------------|-------------------------------|---------------------------------|
| Schema                | Fixed                         | Flexible (schema-less)         |
| Normalization         | Normalize (3NF)               | Denormalize (embed data)       |
| Relationships         | Foreign keys, joins           | Embedded or referenced docs    |
| Data evolution        | Hard to change                | Easy to evolve per use-case    |
| Indexing              | Table indexes                 | Field or document-level indexes|

---

## 🧱 NoSQL Modeling Techniques

### 1. Embedded Documents (Denormalization)
```json
{
  "user_id": 1,
  "name": "Alice",
  "subscriptions": [
    { "plan": "basic", "start": "2024-01-01" },
    { "plan": "pro", "start": "2024-06-01" }
  ]
}
```

- 🔥 Fast reads
- ✅ Ideal for AI logs, nested configs, experiment metadata

---

### 2. Referenced Documents (Normalization)
```json
# users collection
{ "_id": 1, "name": "Alice" }

# experiments collection
{ "user_id": 1, "run_id": "exp42", "metrics": {"loss": 0.2} }
```

- 🔁 Good for avoiding data duplication
- ✅ Useful when a document is shared or reused across many entities

---

### 3. Polymorphic Fields (Flexible Types)
```json
{ "feature_value": "hello" }
{ "feature_value": 42 }
{ "feature_value": { "vector": [0.1, 0.2, 0.3] } }
```

- 🧬 Accepts any kind of data (string, number, object)
- ✅ Perfect for AI pipelines where features vary across runs

---

## 📦 AI-Specific Examples

### 🧪 ML Experiment Metadata (MongoDB)
```json
{
  "model": "bert-base",
  "task": "text-classification",
  "metrics": {
    "accuracy": 0.91,
    "loss": 0.12
  },
  "params": {
    "lr": 0.001,
    "batch_size": 32
  }
}
```

- ✅ Easily store different model configs
- ✅ Flexible for future metrics (e.g., add F1, recall later)

---

### 🔁 Real-Time Prediction Stream (Redis Hash)
```bash
HMSET prediction:user123 timestamp 165123 model_id gpt4 score 0.78
```

- ✅ Fast lookup for cached responses
- ✅ Used in live chatbots, recommendation engines

---

## 🔥 Design Principles

| Principle              | Meaning |
|------------------------|---------|
| Data is accessed more than written | Optimize for reads |
| Model based on application needs  | Not relational theory |
| Avoid joins, prefer embedding     | Reduce multi-query operations |
| Precompute when needed            | Store derived values (loss %, avg) |
| Choose right data types           | Strings, arrays, nested docs |

---

## ✅ Best Practices

| Tip | Why it matters |
|-----|----------------|
| Start from access patterns | Model around how your AI app reads data |
| Use embedded docs for fast lookup | Reduces JOINs and latency |
| Avoid deeply nested docs | Hard to index, query, and update |
| Always index query-heavy fields | Boosts performance |
| Design for scale from day one | Plan for growth in AI logs, usage, sessions |

---

## 🤖 AI Use Case Summary

| Scenario                        | Modeling Style         |
|----------------------------------|-------------------------|
| Chatbot session history         | Embedded messages       |
| Model training metadata         | One doc per experiment  |
| User feature store              | Key-value lookup (Redis)|
| Graph-based reasoning           | Separate nodes/edges    |
| Log aggregation & filtering     | Append-only documents   |

---

📁 **Next File:** [`5_partitioning_sharding_replication.md`](./5_partitioning_sharding_replication.md)