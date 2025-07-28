# 🤖 Real-World SQL Queries for AI/ML Workflows

This folder contains **practical SQL examples** you’re likely to use in machine learning pipelines, dashboards, and model monitoring. These queries tie everything together — from JOINs and aggregation to filtering and ranking.

---

## 📊 Common AI/ML SQL Scenarios

### ✅ 1. Find top-performing models

```sql
SELECT model_name, MAX(f1_score) AS best_score
FROM model_logs
GROUP BY model_name
ORDER BY best_score DESC
LIMIT 5;
```

---

### ✅ 2. Average accuracy per user

```sql
SELECT user_id, AVG(accuracy) AS avg_accuracy
FROM training_logs
GROUP BY user_id;
```

---

### ✅ 3. Track performance trend (using LAG)

```sql
SELECT run_id, accuracy,
       LAG(accuracy) OVER (ORDER BY run_id) AS prev_accuracy
FROM experiment_runs;
```

---

### ✅ 4. Detect duplicate data points

```sql
SELECT input_hash, COUNT(*) AS duplicates
FROM dataset
GROUP BY input_hash
HAVING COUNT(*) > 1;
```

🧠 Used to clean training data.

---

### ✅ 5. Find users without predictions

```sql
SELECT u.id, u.name
FROM users u
LEFT JOIN predictions p ON u.id = p.user_id
WHERE p.user_id IS NULL;
```

---

### ✅ 6. Join user and model info

```sql
SELECT u.name, m.model_name, m.f1_score
FROM users u
JOIN model_logs m ON u.id = m.user_id
WHERE m.f1_score > 0.85
ORDER BY m.f1_score DESC;
```

---

### ✅ 7. Select most recent run for each model (ROW_NUMBER)

```sql
WITH ranked_runs AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY model_name ORDER BY created_at DESC) AS r
  FROM experiment_logs
)
SELECT * FROM ranked_runs WHERE r = 1;
```

---

### ✅ 8. Generate a leaderboard

```sql
SELECT model_name, f1_score,
       RANK() OVER (ORDER BY f1_score DESC) AS position
FROM model_logs;
```

---

### ✅ 9. Calculate class distribution

```sql
SELECT label, COUNT(*) AS count
FROM predictions
GROUP BY label;
```

---

### ✅ 10. Rolling average of accuracy

```sql
SELECT run_id, accuracy,
       AVG(accuracy) OVER (ORDER BY run_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM metrics;
```

---

## 🧠 Tip

> These examples cover **80% of real-world ML SQL use** — especially for data exploration, tracking experiments, and validating preprocessing.

---

📘 You’ve now completed all 7 folders for:

### 📂 `4 databases sql`

Use this knowledge to:
- Analyze and prepare datasets
- Build dashboards
- Track model metrics
- Clean and debug pipelines
- Power analytics in production AI apps

---

🎯 Next Section: [5 pandas and numpy →](../6%20pandas%20and%20numpy/)