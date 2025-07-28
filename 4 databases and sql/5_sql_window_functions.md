# 🔍 SQL Window Functions – Ranking, Rolling Stats, Partitions

Window functions are powerful SQL features used to **perform analytics across rows without collapsing them**. They're perfect for tasks like ranking models, computing moving averages, or comparing grouped data — all very common in AI workflows.

---

## 📌 Common Window Functions

### ✅ 1. `ROW_NUMBER()`

Gives a unique row number **within a partition**.

```sql
SELECT user_id, score,
       ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY score DESC) AS rank
FROM model_scores;
```

---

### ✅ 2. `RANK()` and `DENSE_RANK()`

Assigns rank values to rows — useful for leaderboards or score analysis.

```sql
SELECT model, accuracy,
       RANK() OVER (ORDER BY accuracy DESC) AS model_rank
FROM models;
```

---

### ✅ 3. `OVER(PARTITION BY ...)`

Groups the data before applying window function.

```sql
SELECT user_id, score,
       AVG(score) OVER (PARTITION BY user_id) AS avg_user_score
FROM model_scores;
```

---

### ✅ 4. `LAG()` / `LEAD()`

Access previous/next row value.

```sql
SELECT timestamp, accuracy,
       LAG(accuracy) OVER (ORDER BY timestamp) AS prev_score
FROM training_log;
```

---

## 📊 AI/ML Use Cases for Window Functions

| Feature | Use Case |
|---------|----------|
| `ROW_NUMBER()` | Select best model per user |
| `RANK()` | Create ML model leaderboards |
| `AVG() OVER` | Rolling average validation loss |
| `LAG()` / `LEAD()` | Detect performance drops between training runs |

---

## 🧪 Example Use Cases

### a) Pick highest model per user:

```sql
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY score DESC) AS r
  FROM model_scores
)
SELECT * FROM ranked WHERE r = 1;
```

---

### b) Rolling average of F1 score over time:

```sql
SELECT run_id, f1_score,
       AVG(f1_score) OVER (ORDER BY run_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM results;
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| Difference between `RANK()` and `ROW_NUMBER()`? | `RANK()` allows gaps, `ROW_NUMBER()` is always unique |
| When do you use `PARTITION BY`? | When you want to compute stats **within each group** |
| Use case of `LAG()` in ML? | Track previous score to detect drops/improvements |

---

## ✅ Tip

> Window functions **don’t reduce rows**, unlike `GROUP BY`. They **augment** each row with extra insight — great for dashboards and model diagnostics.

---

📁 **Next Folder:** [6 database design and index →](../6 database design and index/)