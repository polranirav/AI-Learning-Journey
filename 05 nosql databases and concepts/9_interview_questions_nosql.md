# 🎯 9 – NoSQL Interview Questions (With AI Engineering Context)

These are commonly asked **NoSQL database interview questions**, especially relevant for roles involving **AI, data pipelines, or backend infrastructure**.

---

## 🔍 Section 1: Fundamentals

### Q1: What is NoSQL?
> NoSQL stands for “Not Only SQL.” It refers to **non-relational databases** that provide flexible schemas, scalability, and fast performance for unstructured or semi-structured data.

---

### Q2: Types of NoSQL Databases?
| Type              | Example      | Description |
|-------------------|--------------|-------------|
| Document Store    | MongoDB      | Stores data as JSON-like documents |
| Key-Value Store   | Redis        | Simple lookup using a unique key |
| Column Family     | Cassandra    | Optimized for wide tables and fast writes |
| Graph DB          | Neo4j        | Stores nodes & relationships (graph format) |

---

### Q3: Differences: SQL vs NoSQL?

| Feature           | SQL (Relational)        | NoSQL (Non-relational)          |
|-------------------|--------------------------|----------------------------------|
| Schema            | Fixed schema              | Dynamic, schema-less             |
| Joins             | Supported                 | Rare or avoided                  |
| Scalability       | Vertical (scale-up)       | Horizontal (scale-out)           |
| Best for          | Structured, tabular data  | Unstructured, scalable systems   |

---

### Q4: What is CAP Theorem?
> In distributed systems, the CAP theorem says you can only guarantee **two out of three**:  
> - **C**onsistency  
> - **A**vailability  
> - **P**artition Tolerance  
> → No system can guarantee all three simultaneously.

---

## ⚙️ Section 2: AI Engineering Context

### Q5: Where is NoSQL used in AI?

| Component           | NoSQL Use                  |
|---------------------|----------------------------|
| Logs & metrics      | MongoDB, Cassandra         |
| Chat sessions       | Redis, MongoDB             |
| Feature stores      | Redis, DynamoDB            |
| Embeddings          | RedisVector, Pinecone      |
| Session tracking    | Redis with TTL             |

---

### Q6: Why choose MongoDB over SQL for AI logs?
> MongoDB allows **schema flexibility**, fast insertions, and easy storage of JSON-like documents — perfect for logs, experiment metadata, and nested AI config objects.

---

### Q7: How does Redis help in real-time inference?
> Redis is in-memory and supports **millisecond latency**. Ideal for:
- Caching model responses
- Storing session variables
- Ranking results via ZSETs

---

### Q8: Difference between Sharding and Replication?

| Term        | Meaning                          |
|-------------|-----------------------------------|
| Sharding    | Splits data across multiple servers |
| Replication | Duplicates data across nodes for fault-tolerance |

---

### Q9: How do you design NoSQL schema for AI apps?
> Design based on **access patterns** (reads/writes). Prefer **embedding** for nested queries, **referencing** for reusable data. Avoid deep nesting beyond 2-3 levels.

---

### Q10: Common pitfalls with NoSQL?

- Not indexing query-heavy fields  
- Over-embedding large arrays  
- Misconfigured TTLs in Redis  
- Assuming strong consistency in BASE systems  
- Ignoring write durability (risk of data loss)

---

## 🧠 Bonus: Coding/Scenario Questions

### Q11: Write a MongoDB query to find experiments with loss < 0.2
```javascript
db.experiments.find({ "metrics.loss": { $lt: 0.2 } })
```

---

### Q12: How to expire a Redis key after 1 hour?
```bash
SET user123:cache "value"
EXPIRE user123:cache 3600
```

---

## ✅ Summary: Must-Prepare Areas

| Topic                      | Prep Type     |
|----------------------------|---------------|
| MongoDB schema modeling    | Concepts + code |
| Redis TTL, INCR, ZSET      | Syntax + use cases |
| CAP theorem tradeoffs      | Explain with examples |
| AI pipeline integration    | Real-world relevance |
| Sharding vs Replication    | Diagram + pros/cons |

---

🎓 Pro Tip:
> Always tie your answers to **AI project examples** — it shows practical experience, not just theory.

📁 **End of Week 9.**  
Next up: [`Week 10 – Pandas Series`](../5 pandas and numpy/2 pandas series/README.md)
```