# 🏗️ Database Design and Indexing – Table Creation, Primary Keys, Indexes

This folder covers how to **design efficient databases** for ML pipelines and AI systems — especially for storing large datasets, logs, and experiment metadata. Understanding keys and indexing helps optimize query speed for preprocessing, dashboards, and analysis.

---

## 🧱 1. CREATE TABLE

Create a structured table with types and constraints.

```sql
CREATE TABLE model_logs (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100),
    accuracy FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

🧠 `SERIAL` auto-increments IDs (useful for experiments, logs, etc.)

---

## 🔑 2. PRIMARY KEY

Ensures each row is uniquely identifiable.

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

📌 Used for **joins**, lookup tables, and tracking samples or users.

---

## 🔒 3. UNIQUE Constraints

Prevent duplicate values in columns like email or experiment name.

```sql
CREATE TABLE models (
    model_id INT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);
```

---

## 📂 4. INDEXING for Speed

Indexes accelerate WHERE/JOIN/ORDER BY queries on large datasets.

```sql
CREATE INDEX idx_model_accuracy ON model_logs (accuracy);
```

🧠 Index = Like a lookup shortcut for faster search.

---

## 🔍 When to Index?

| Field Type       | Index? | Why |
|------------------|--------|-----|
| Foreign Keys     | ✅     | Speeds up joins |
| Frequently Filtered Columns (`WHERE`) | ✅ | Faster lookups |
| Ordered/Ranked Output (`ORDER BY`) | ✅ | Improve sort speed |
| Low-cardinality columns (e.g., boolean) | ❌ | Little benefit |

---

## 🧠 Real Use in AI Engineering

| Task | DB Design Benefit |
|------|-------------------|
| Store model logs | Track model names, accuracy, timestamps |
| Cache embeddings | Use indexed table with hash ID |
| Fast retrieval for experiments | Index by model name, user ID |
| Join logs and users | Primary & foreign keys ensure integrity |

---

## 🧪 Sample AI Table Design

```sql
CREATE TABLE experiment_results (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(50),
    f1_score FLOAT,
    run_time INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| Why use primary keys? | Uniquely identify rows, enforce consistency |
| When does indexing slow things down? | On frequent INSERT/UPDATE/DELETE (write-heavy ops) |
| What’s the difference between PRIMARY KEY and UNIQUE? | Both enforce uniqueness, but PK also prevents nulls and sets default index |

---

## ✅ Tip

> Index columns you **filter or sort often**.  
> But avoid indexing small/static columns or ones with too many duplicates.

---

📁 **Next Folder:** [7 ai query examples →](../7 ai query examples/)