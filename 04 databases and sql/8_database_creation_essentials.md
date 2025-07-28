# 🏗️ Essential SQL for Creating Databases and Tables (AI-Ready)

This folder gives you **just the critical SQL commands** to define tables, manage schema, and prepare a relational database for storing model data, predictions, logs, or user metadata.

---

## 📌 1. Create a New Database (Optional Step)

Most systems (PostgreSQL, MySQL) use:

```sql
CREATE DATABASE ml_pipeline_db;
```

To use it:

```sql
\c ml_pipeline_db  -- PostgreSQL
USE ml_pipeline_db;  -- MySQL
```

---

## 📌 2. Create a Table – Core Pattern

```sql
CREATE TABLE model_logs (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    accuracy FLOAT CHECK (accuracy <= 1.0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

✅ Covers:
- Auto-incrementing `id`  
- `NOT NULL`, `CHECK`, `DEFAULT`  
- Proper datatypes: `VARCHAR`, `FLOAT`, `TIMESTAMP`

---

## 📌 3. Add Relationships (Foreign Keys)

Used when tracking user-model connections, datasets, etc.

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE experiments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    model_name VARCHAR(50),
    f1_score FLOAT
);
```

✅ Enables **joins** and **referential integrity** in AI pipelines.

---

## 📌 4. Alter Table (Optional Additions)

Add column later:

```sql
ALTER TABLE model_logs ADD COLUMN model_type TEXT;
```

Rename:

```sql
ALTER TABLE model_logs RENAME COLUMN model_name TO name;
```

---

## 📌 5. Drop Table / Database (Careful!)

```sql
DROP TABLE IF EXISTS old_table;
DROP DATABASE IF EXISTS test_db;
```

🧠 Only use when resetting/test dev environments.

---

## 🧠 Real Use Cases in AI Projects

| Task | SQL Table Example |
|------|-------------------|
| Store experiment metrics | `CREATE TABLE experiments (...)` |
| Store user actions | `CREATE TABLE logs (...)` |
| Track model performance over time | `model_logs` with timestamps |
| Handle multiple datasets | Create table per dataset or normalize with keys |

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| What’s a primary key? | Unique ID to identify each row. |
| Why foreign keys? | Link related tables (e.g., users → experiments) |
| Should AI logs use relational DBs? | Yes, for structured logs, dashboards, audit trails |

---

## ✅ Tip

> Design tables to match **how your models/data are used**. Always include:
> - `id` field
> - Timestamps
> - Foreign keys if linked data

---

📁 Done with Folder: `8 database creation essentials`

👉 You’re now ready to build solid, AI-friendly SQL schemas from scratch!