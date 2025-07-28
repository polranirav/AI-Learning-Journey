
# 🧪 7 – Store AI Pipeline Configs in MongoDB (Reproducibility)

One of the most underrated aspects of AI development is **config management** — especially for:

- Model architecture settings
- Hyperparameters
- Preprocessing choices
- Dataset references

Storing all of this in MongoDB allows you to **track**, **reproduce**, and **audit** past pipeline runs.

---

## 🧩 Why Config Storage Matters

| Problem                     | MongoDB Advantage           |
|-----------------------------|-----------------------------|
| Lost config files           | Centralized DB store        |
| Too many YAML/JSON versions | Use indexed searchable logs |
| Team collaboration          | Shared cloud access         |
| Model reproducibility       | Frozen settings per run     |

---

## 📘 Pipeline Config Schema (Sample)

```json
{
  "experiment": "ai_pipeline_xgboost_v1",
  "dataset": "customer_churn_v2.csv",
  "preprocessing": {
    "scaler": "StandardScaler",
    "encoding": "OneHot",
    "missing_values": "mean"
  },
  "model": {
    "type": "XGBoost",
    "n_estimators": 100,
    "max_depth": 5,
    "learning_rate": 0.1
  },
  "eval": {
    "metric": "AUC",
    "cross_val": 5
  },
  "timestamp": "2025-07-25T21:00:00Z",
  "status": "completed"
}
```

---

## ⚙️ 1. MongoDB Setup

```bash
pip install pymongo
```

---

## 🔌 2. Connect to DB

```python
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client.pipeline_configs
collection = db.xgboost_configs
```

---

## 💾 3. Save Config

```python
config = {
    "experiment": "ai_pipeline_xgboost_v1",
    "dataset": "customer_churn_v2.csv",
    "preprocessing": {
        "scaler": "StandardScaler",
        "encoding": "OneHot",
        "missing_values": "mean"
    },
    "model": {
        "type": "XGBoost",
        "n_estimators": 100,
        "max_depth": 5,
        "learning_rate": 0.1
    },
    "eval": {
        "metric": "AUC",
        "cross_val": 5
    },
    "timestamp": datetime.utcnow(),
    "status": "completed"
}

collection.insert_one(config)
```

---

## 🔍 4. Retrieve Past Configs

```python
for cfg in collection.find({"model.type": "XGBoost"}):
    print(cfg["experiment"], cfg["model"]["learning_rate"])
```

---

## 🧠 Use Cases in AI/ML

| Scenario                             | Field Example              |
|--------------------------------------|----------------------------|
| Training multiple model variants     | change `max_depth`, log runs |
| Comparing data preprocessing         | log `scaler`, `encoding`  |
| Experiment tracking (like MLflow)    | use `status`, `timestamp` |
| Deployment audit                     | match config with model version |

---

## 📁 Example Directory

```
config-store/
├── config_manager.py
├── configs.json
├── run_experiment.py
└── requirements.txt
```

---

## ✅ Best Practices

- Use `experiment` as unique run identifier
- Track `status`: pending, running, completed, failed
- Add `"notes"` or `"tags"` field for easy filtering
- Include dataset version or checksum

---

📁 **Next File:** [`8_nosql_design_ai_project.md`](./8_nosql_design_ai_project.md)