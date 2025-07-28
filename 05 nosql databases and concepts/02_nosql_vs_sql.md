🔍 2 – NoSQL vs SQL (AI-Centric Comparison)

This guide compares **NoSQL and SQL databases** with a focus on **AI/ML systems**. It’s not just about syntax — it’s about which system fits better for the scale, flexibility, and performance your AI workflow demands.

---

## 🧠 Big Picture

| Category             | SQL (Relational DB)             | NoSQL (Non-relational DB)         |
|----------------------|----------------------------------|------------------------------------|
| Schema               | Fixed, strict schema             | Flexible, dynamic schema           |
| Scaling              | Vertical (add RAM/CPU)           | Horizontal (add nodes)             |
| Transactions         | ACID (strong consistency)        | BASE (eventual consistency)        |
| Data Structure       | Rows & tables                    | JSON, key-value, graphs, etc.      |
| Best For             | Structured tabular data          | Semi/unstructured, fast-changing   |
| Query Language       | SQL (JOINs, WHERE, etc.)         | Varies (Mongo, Redis, CQL, etc.)   |
| AI Use Cases         | Training datasets, joins         | Real-time logs, embeddings, prompts |
| Example DBs          | MySQL, PostgreSQL, Oracle        | MongoDB, Redis, Cassandra, Neo4j   |

---

## 📦 Use Both in Real Projects

| Component              | SQL DB                         | NoSQL DB                      |
|------------------------|---------------------------------|-------------------------------|
| User accounts, payments | PostgreSQL / MySQL             | —                             |
| Model logs/configs      | —                               | MongoDB                       |
| Chatbot history         | —                               | Redis                         |
| Feature store (real-time)| —                              | Cassandra                     |
| Knowledge graph         | —                               | Neo4j                         |

> 🧬 In AI systems, SQL is often used for structured metadata, and NoSQL for fast-changing, nested, or large-scale data.

---

## 🧱 Schema Flexibility

### ✅ SQL:
```sql
CREATE TABLE users (
    id INT,
    name VARCHAR(50),
    email VARCHAR(100)
);
```

- Any extra field must be predefined.

### ✅ NoSQL (MongoDB style):
```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@email.com",
  "preferences": {
    "theme": "dark",
    "notifications": true
  }
}
```

- Add any new fields on-the-fly without migrations.

---

## 📈 Scalability: Vertical vs Horizontal

| SQL                      | NoSQL                      |
|--------------------------|----------------------------|
| Scale-up: bigger server  | Scale-out: more servers    |
| Harder to shard          | Built for distributed systems |
| Good for structured apps | Ideal for high-volume AI data |

---

## 🔁 Transactions: ACID vs BASE

| Feature      | SQL (ACID)                       | NoSQL (BASE)                          |
|--------------|----------------------------------|---------------------------------------|
| Atomic       | All or nothing                   | Partial writes accepted               |
| Consistent   | Always valid state               | Eventual consistency                  |
| Isolated     | One transaction at a time        | Often async operations                |
| Durable      | Writes survive crashes           | Often uses logs/checkpoints           |

**ACID = Financial & critical data**  
**BASE = Fast, large-scale, distributed AI systems**

---

## 🧪 AI Workflow Comparison

| Step                          | SQL Example              | NoSQL Example                |
|-------------------------------|--------------------------|------------------------------|
| Store user data               | PostgreSQL `users` table | —                            |
| Log model inference           | —                        | MongoDB `inference_logs`     |
| Cache real-time predictions   | —                        | Redis                        |
| Save session states           | —                        | Redis (key-value TTL)        |
| Store prompt-response history | —                        | MongoDB or Neo4j             |

---

## ⚖️ When to Use What?

### ✅ Use **SQL** when:
- Data structure is fixed and known ahead of time
- You need joins and relational constraints
- Consistency is top priority
- Reports, dashboards, analytics require complex queries

### ✅ Use **NoSQL** when:
- Schema may change over time (e.g., logs, metrics)
- Speed, flexibility, scale matter more than joins
- You handle nested/graph-based/unstructured data
- AI pipelines require real-time ingestion or cache

---

## 🔍 Summary Table

| Use Case                     | Recommended DB Type |
|------------------------------|---------------------|
| User registrations, billing  | SQL (PostgreSQL, MySQL) |
| Logging inference results    | NoSQL (MongoDB)     |
| Chat session storage         | NoSQL (Redis)       |
| Real-time feature cache      | NoSQL (Cassandra)   |
| Complex joins and reports    | SQL                 |

---

📁 **Next File:** [`3_base_vs_acid.md`](03_base_vs_acid.md)