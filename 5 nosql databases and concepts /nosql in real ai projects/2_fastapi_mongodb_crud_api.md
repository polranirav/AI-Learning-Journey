
# 🚀 2 – FastAPI + MongoDB: Build a CRUD API for AI Logs

FastAPI + MongoDB is a **production-grade stack** to build APIs that can **log AI usage**, **store user input**, or **track model results** in real time.

This is ideal for:
- Chatbot logging
- Prompt/result storage
- AI experiment tracking

---

## ⚙️ Stack Overview

| Component       | Tool          |
|------------------|---------------|
| API framework    | FastAPI       |
| NoSQL database   | MongoDB       |
| Driver           | PyMongo       |
| DB name          | `ai_logs`     |
| Collection       | `chat_history`|

---

## 🧩 MongoDB Document Structure

```json
{
  "user_id": 1,
  "prompt": "Translate to German",
  "response": "Übersetzen Sie ins Deutsche",
  "model": "gpt-4",
  "timestamp": "2025-07-25T18:00:00Z"
}
```

---

## 🛠️ 1. Setup

### Install dependencies:

```bash
pip install fastapi uvicorn pymongo
```

---

## 📄 2. MongoDB Connection (`db.py`)

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.ai_logs
collection = db.chat_history
```

---

## 🌐 3. FastAPI Server (`main.py`)

```python
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from db import collection

app = FastAPI()

class Log(BaseModel):
    user_id: int
    prompt: str
    response: str
    model: str

@app.post("/log/")
def log_interaction(log: Log):
    data = log.dict()
    data["timestamp"] = datetime.utcnow()
    collection.insert_one(data)
    return {"msg": "Logged successfully"}
```

---

## 🔎 4. Get All Logs

```python
@app.get("/logs/")
def get_logs():
    logs = list(collection.find({}, {"_id": 0}))
    return logs
```

---

## ✏️ 5. Update a Log Entry

```python
@app.put("/logs/{user_id}")
def update_response(user_id: int, new_response: str):
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"response": new_response}}
    )
    return {"msg": "Updated"}
```

---

## ❌ 6. Delete Logs for User

```python
@app.delete("/logs/{user_id}")
def delete_user_logs(user_id: int):
    result = collection.delete_many({"user_id": user_id})
    return {"msg": f"Deleted {result.deleted_count} logs"}
```

---

## ▶️ Run Server

```bash
uvicorn main:app --reload
```

Visit:  
- POST: `http://localhost:8000/log/`  
- GET: `http://localhost:8000/logs/`

---

## 📂 Folder Structure

```
ai-fastapi-mongo/
├── main.py
├── db.py
├── requirements.txt
└── README.md
```

---

## 🧠 AI Use Cases

| Use Case                     | Endpoint       |
|------------------------------|----------------|
| Save prompt + response       | POST /log/     |
| Show past interactions       | GET /logs/     |
| Update old model reply       | PUT /logs/{id} |
| Delete specific user logs    | DELETE /logs/{id} |

---

## ✅ Production Tips

- 🔐 Use `pydantic.BaseModel` for validation
- 🧼 Always sanitize inputs to MongoDB
- 📊 Add indexes on `user_id`, `timestamp`
- 🌐 Use `MongoDB Atlas` for cloud deployment
- 📁 Export logs using `mongodump` or API routes

---

📁 **Next File:** [`3_redis_for_llm_cache.md`](./3_redis_for_llm_cache.md)
```