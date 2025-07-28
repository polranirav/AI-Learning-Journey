# 🧾 7 – NoSQL Query Examples (MongoDB + Redis Focus)

In AI applications, you often need to store, retrieve, and filter data rapidly. NoSQL query syntax is tailored for flexibility and speed — especially with **MongoDB** (document DB) and **Redis** (in-memory DB).

---

## 📄 1. MongoDB – Querying Documents

### 🧪 Example: Find all experiments with accuracy > 0.9

```javascript
db.experiments.find({ "metrics.accuracy": { $gt: 0.9 } })
```

---

### 🔍 Example: Get last 10 logs by timestamp

```javascript
db.logs.find().sort({ timestamp: -1 }).limit(10)
```

---

### 🔧 Insert experiment result

```javascript
db.experiments.insertOne({
  model: "bert",
  accuracy: 0.93,
  timestamp: new Date()
})
```

---

### 🔄 Update model config

```javascript
db.models.updateOne(
  { name: "gpt-3" },
  { $set: { lr: 0.001 } }
)
```

---

### ❌ Delete old logs

```javascript
db.logs.deleteMany({ timestamp: { $lt: ISODate("2023-01-01") } })
```

---

## ⚡ 2. Redis – Key-Value AI Use Cases

### 🎯 Store model output cache

```bash
SET result:user42:token123 "gpt-response-text"
EXPIRE result:user42:token123 60
```

---

### 🕓 Store time-series value

```bash
ZADD predictions 1656678000 "0.91"
ZADD predictions 1656678060 "0.92"
ZRANGE predictions 0 -1 WITHSCORES
```

---

### ✅ Store user embeddings (JSON-style in RedisJSON)

```bash
JSON.SET user:42 $ '{"embedding": [0.1, 0.2, 0.3]}'
```

---

### 📊 Count access by key

```bash
INCR inference_count:user42
```

---

## 🔬 Bonus: Aggregation in MongoDB

### Average accuracy of all runs:

```javascript
db.experiments.aggregate([
  { $group: { _id: null, avg_acc: { $avg: "$accuracy" } } }
])
```

---

## 🔁 MongoDB vs Redis

| Task                        | MongoDB                        | Redis                          |
|-----------------------------|--------------------------------|--------------------------------|
| Store JSON documents        | ✅                              | ❌ (unless using RedisJSON)    |
| Store TTL cache             | Limited TTL support            | ✅ Built-in TTL via `EXPIRE`   |
| Real-time ranking           | ❌                             | ✅ ZSETs, INCR, leaderboard     |
| AI logs or metadata         | ✅                              | ❌                              |
| Session store/cache         | ❌                              | ✅                              |

---

## ✅ Summary

| Use Case                  | Tool           | Example         |
|---------------------------|----------------|-----------------|
| Store logs                | MongoDB        | `insertOne()`   |
| Cache model response      | Redis          | `SET + EXPIRE`  |
| Track user inference usage| Redis          | `INCR key`      |
| Query high-accuracy runs  | MongoDB        | `find({ $gt })` |

---

📁 **Next File:** [`8_nosql_in_real_ai_projects.md`](./8_nosql_in_real_ai_projects.md)
```