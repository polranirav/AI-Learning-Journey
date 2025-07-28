
# 📡 4 – Real-Time User Logging with Redis Streams

Redis Streams allow you to build **real-time event pipelines** — perfect for tracking **user actions**, **inference logs**, or **AI decision flow** as they happen.

---

## 🧩 Project Scenario

You're running a web-based AI platform (chatbot, recommendation engine, model dashboard), and want to:

- Track user interactions (clicks, prompts, pageviews)
- Stream logs to dashboards or data lake
- Do it all without blocking your main app

**Redis Streams** are a perfect fit.

---

## ⚙️ Tech Stack

| Component       | Tool              |
|------------------|-------------------|
| Logging Backend  | Redis Streams     |
| Language         | Python            |
| Visualization    | Streamlit (optional) |
| Processing       | Stream Consumers  |

---

## 📘 What is a Redis Stream?

A Redis stream is a **log-based data structure** where you:

- Push new entries (`XADD`)
- Read latest entries (`XREAD`)
- Set consumer groups to scale readers

---

## 🛠️ 1. Install Redis + Python Client

```bash
pip install redis
```

---

## 🔌 2. Connect to Redis

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
```

---

## 📝 3. Push User Event to Stream

```python
event = {
    "user_id": "42",
    "event_type": "prompt",
    "message": "What is quantum computing?",
    "timestamp": "2025-07-25T18:00:00Z"
}

r.xadd("user_logs", event)
```

➡️ `user_logs` is your stream name (auto-created)

---

## 🔍 4. Read Events (Simple)

```python
events = r.xrange("user_logs", count=5)
for event_id, data in events:
    print(f"{event_id}: {data}")
```

---

## 🔁 5. Consumer Group (Advanced Scaling)

### Create consumer group:

```python
r.xgroup_create("user_logs", "analytics_group", mkstream=True)
```

### Consume in a background service:

```python
while True:
    events = r.xreadgroup("analytics_group", "bot_1", {"user_logs": ">"}, count=1, block=1000)
    for stream, messages in events:
        for msg_id, msg_data in messages:
            print("⏺️ Event:", msg_data)
            r.xack("user_logs", "analytics_group", msg_id)
```

---

## 📁 Project Layout

```
redis-stream-logger/
├── logger.py          # Push events
├── consumer.py        # Read + process events
├── dashboard.py       # (Optional) Streamlit view
├── requirements.txt
```

---

## 🧠 Real AI Use Cases

| Event Type         | Description |
|--------------------|-------------|
| User prompt        | Logged to stream |
| Model response     | Streamed to dashboard |
| Feedback rating    | Used for RLHF or fine-tuning |
| Feature toggle     | Enable/disable real-time A/B |

---

## ✅ Redis Streams vs Kafka

| Feature            | Redis Streams     | Kafka            |
|--------------------|------------------|------------------|
| Setup              | Easy              | Heavy            |
| Scale              | Good (GBs/day)    | Excellent (PBs/day) |
| Latency            | Low               | Low              |
| Storage            | In-memory (or RDB) | Disk-based       |

> Redis is best for **lightweight internal streaming**. Use Kafka for large-scale pub/sub across teams.

---

## ✅ Tips for Production

- Set a **max length** on the stream (`MAXLEN 10000`)
- Use **consumer groups** to parallelize log readers
- Archive data to a DB or file once processed
- Monitor with Redis Insight / CLI tools

---

📁 **Next File:** [`5_vector_db_vs_redis_vector.md`](./5_vector_db_vs_redis_vector.md)
```