
# 📊 6 – Store Fine-Tuning Logs & Metrics in MongoDB

During model fine-tuning (LLMs, image models, etc.), you generate:

- Loss metrics per epoch
- Accuracy per batch
- Checkpoint references
- Learning rates, hyperparams

Rather than logging this in a `.txt` file or Excel, let’s **store it structurally in MongoDB** — so it’s searchable, visualizable, and sharable.

---

## 🧩 Why Log to a NoSQL DB?

| Reason                | Benefit                         |
|-----------------------|----------------------------------|
| Schema flexibility    | Add/remove metrics easily        |
| Time-series support   | Log by epoch or batch            |
| JSON format           | Natural fit for ML stats         |
| Scalable storage      | Store hundreds of runs           |
| Analysis              | Compare runs, filter configs     |

---

## 📘 Log Entry Schema Example

```json
{
  "experiment": "bert-finetune-news",
  "model": "bert-base-uncased",
  "epoch": 3,
  "train_loss": 0.232,
  "val_accuracy": 0.87,
  "learning_rate": 3e-5,
  "timestamp": "2025-07-25T20:25:00Z",
  "checkpoints": {
    "path": "/checkpoints/bert-epoch3",
    "saved": true
  }
}
```

---

## ⚙️ 1. Setup

```bash
pip install pymongo
```

---

## 🔌 2. Connect to MongoDB

```python
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client.training_logs
collection = db.bert_runs
```

---

## 💾 3. Save Log at End of Epoch

```python
log_entry = {
    "experiment": "bert-finetune-news",
    "model": "bert-base-uncased",
    "epoch": 3,
    "train_loss": 0.232,
    "val_accuracy": 0.87,
    "learning_rate": 3e-5,
    "timestamp": datetime.utcnow(),
    "checkpoints": {
        "path": "/checkpoints/bert-epoch3",
        "saved": True
    }
}

collection.insert_one(log_entry)
```

---

## 🔍 4. Query Logs for Specific Run

```python
cursor = collection.find({"experiment": "bert-finetune-news"})
for doc in cursor:
    print(f"Epoch {doc['epoch']}: val_acc = {doc['val_accuracy']}")
```

---

## 📊 5. Visualize Logs with Pandas/Matplotlib

```python
import pandas as pd

df = pd.DataFrame(list(collection.find()))
df.plot(x="epoch", y=["train_loss", "val_accuracy"], kind="line")
```

---

## 🧠 Real-World Benefits

| Feature            | Use Case                           |
|--------------------|-------------------------------------|
| Compare runs       | View performance across different seeds or models |
| Auto dashboard     | Feed into Streamlit or Gradio UI   |
| Alerting           | Send Slack/Email if accuracy drops |
| Experiment tagging | Group runs via `experiment` field  |

---

## ✅ Pro Tips

- Add indexes on `timestamp`, `experiment`, or `model`
- Export logs to CSV with `pandas.to_csv()` for sharing
- Structure logs as documents per epoch (not one big doc)
- Backup with `mongodump` weekly

---

📁 **Next File:** [`7_ai_pipeline_config_mongo.md`](./7_ai_pipeline_config_mongo.md)