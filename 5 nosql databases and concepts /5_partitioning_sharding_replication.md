🧬 5 – Partitioning, Sharding & Replication in NoSQL
---

## 🧱 1. Partitioning

> **Partitioning** means splitting your database into smaller segments, often called **partitions** or **buckets**, based on a rule (like user ID, region, or time).

| Feature        | Description                          |
|----------------|--------------------------------------|
| Method         | Divide data by a key (e.g., user_id) |
| Goal           | Spread data across nodes             |
| Benefit        | Load balancing, faster lookups       |
| Example        | All logs from user_42 go to Node A   |

✅ Used for: log data, chat sessions, AI model output by user/project

---

## 🧩 2. Sharding (Distributed Partitioning)

> **Sharding** is a form of partitioning where each shard is hosted on a **separate server or cluster**.

| Feature         | Description |
|-----------------|-------------|
| Horizontal scale| Adds more nodes instead of upgrading one |
| Query Routing   | Query goes directly to the right shard |
| Hashing         | Often uses hash of key for uniform spread |
| Failure Zone    | Isolated — one shard failing won’t crash others |

🧠 MongoDB, Cassandra, Elasticsearch all support sharding

---

### 🔁 Example (Sharded Log Storage)

```json
# Node A (shard 1)
{ "user_id": 1, "log": "Inference started" }

# Node B (shard 2)
{ "user_id": 99, "log": "Inference complete" }
```

> Each document is routed to a shard based on the hashed user_id

---

## 📡 3. Replication

> **Replication** means copying your data across multiple servers (nodes) to ensure fault tolerance and high availability.

| Type         | Description |
|--------------|-------------|
| Master-Slave | One primary, others follow             |
| Peer-to-Peer | All nodes are equal (eventual sync)    |
| Read Replicas| Some nodes handle read-only queries    |
| Async Sync   | Some systems replicate in the background|

✅ Use in AI: Keep multiple copies of user embeddings, logs, chat history across zones

---

## 🔄 Combined in Production

| Feature     | Role in AI Infra |
|-------------|------------------|
| Sharding    | Spread model output logs per user/task |
| Partitioning| Store chunks of time-series sensor data |
| Replication | Prevent data loss during training crash |

> Example: Redis Cluster = Partitioning + Sharding + Replication  
> Example: MongoDB Replica Set = Auto-failover + High read availability

---

## 📊 Visual Overview

```
         +-----------+      +-----------+
Shard 1  |  User 1–50| ---> | Node A    |<--+
         +-----------+      +-----------+   |
                                            |
         +-----------+      +-----------+   |  Replication
Shard 2  | User 51–100| --->| Node B    |<--+
         +-----------+      +-----------+
```

---

## 🤖 AI/ML Use Cases

| Use Case                          | What’s Used |
|----------------------------------|-------------|
| Chat history at massive scale    | Sharded MongoDB |
| Cached vector DB across zones    | Redis replication |
| IoT model with region-wise logs  | Partitioned Cassandra |
| High-volume feature ingestion    | Sharded time-series DB |

---

## 💡 Best Practices

| Practice                  | Benefit |
|---------------------------|---------|
| Hash keys evenly          | Avoid hotspot shards |
| Add replica lag alerts    | Detect sync issues early |
| Use geographic replication| Reduce global latency |
| Monitor shard growth      | Rebalance as data increases |
| Prefer quorum writes      | Safer AI data updates |

---

## ✅ Quick Summary

| Term         | Purpose                    | Real-world in AI |
|--------------|-----------------------------|------------------|
| Partitioning | Divide data logically       | Logs by region   |
| Sharding     | Distribute across servers   | AI data streams  |
| Replication  | Copy data for backup/faults | Avoid loss on crash |

---

📁 **Next File:** [`6_cap_theorem.md`](./6_cap_theorem.md)