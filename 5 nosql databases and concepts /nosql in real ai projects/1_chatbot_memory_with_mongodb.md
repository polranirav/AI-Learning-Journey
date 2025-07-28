
# 🤖 1 – Chatbot Memory with MongoDB (AI Context)

Storing user conversations is crucial in building **context-aware chatbots**. MongoDB, being document-based, is ideal for saving entire conversations in flexible JSON-like structures.

---

## 🧩 Project Scenario

You're building an AI assistant like ChatGPT. Each user message and bot response must be stored for:

- Persistent memory
- Analytics
- Prompt tuning
- Multi-turn conversations

---

## 🛠️ Tech Stack

| Component     | Tool            |
|---------------|-----------------|
| Backend API   | FastAPI         |
| NoSQL DB      | MongoDB (via PyMongo) |
| Data Format   | JSON documents  |
| AI Logic      | OpenAI or Local model |

---

## 📦 MongoDB Document Design

```json
{
  "session_id": "abc123",
  "user_id": 42,
  "messages": [
    { "role": "user", "text": "Hi" },
    { "role": "bot", "text": "Hello! How can I help you?" },
    { "role": "user", "text": "Tell me a joke." },
    { "role": "bot", "text": "Why did the AI cross the road? To optimize the chicken." }
  ],
  "created_at": "2025-07-25T20:10:00Z"
}
```

---

## ⚙️ MongoDB Setup with PyMongo

### 1. Install

```bash
pip install pymongo
```

### 2. Connect to DB

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.chatbot_db
memory_collection = db.chat_memory
```

---

## 💾 Save a Conversation

```python
chat_session = {
    "session_id": "abc123",
    "user_id": 42,
    "messages": [
        {"role": "user", "text": "Hi"},
        {"role": "bot", "text": "Hello! How can I help you?"}
    ]
}

memory_collection.insert_one(chat_session)
```

---

## 🔍 Retrieve Past Memory

```python
session_id = "abc123"
memory = memory_collection.find_one({"session_id": session_id})
for msg in memory["messages"]:
    print(f"{msg['role']}: {msg['text']}")
```

---

## 🔁 Update with New Message

```python
memory_collection.update_one(
    {"session_id": "abc123"},
    {"$push": {"messages": {"role": "user", "text": "Tell me a joke."}}}
)
```

---

## 🧠 AI Use Cases for This Memory Store

| Feature             | Benefit                                 |
|---------------------|------------------------------------------|
| Context continuity  | Carry past messages into prompts         |
| Memory injection    | Help LLM remember prior instructions     |
| Personalization     | Tailor responses by user history         |
| Chat history viewer | Show logs to admins or users             |

---

## ✅ Best Practices

- Use `session_id` as index for faster lookup
- Consider TTL for old/inactive sessions
- Sanitize inputs before writing to DB
- Cap memory length per session (limit messages)
- Encrypt sensitive content if needed

---

## 📁 Directory Snapshot

```
chatbot-memory/
├── main.py              # FastAPI logic
├── db.py                # MongoDB connection code
├── models/
│   └── memory_schema.json
├── requirements.txt     # pymongo, fastapi
```

---

## 🚀 Production Tips

| Task                     | Tool           |
|--------------------------|----------------|
| Deploy MongoDB           | Atlas or Docker |
| Enforce schema           | MongoDB Validator |
| Visualize data           | Mongo Compass or Robo 3T |
| Backup data              | mongodump/mongorestore |
| Real-time viewer         | Integrate with Streamlit |

---

📁 **Next File:** [`2_fastapi_mongodb_crud_api.md`](./2_fastapi_mongodb_crud_api.md)