# 📊 SQL Grouping and Filters – `GROUP BY`, `HAVING`, `DISTINCT`

This folder teaches you how to **group, aggregate, and filter data**, which is vital in real-world AI/ML projects for summarizing model runs, class distributions, or user activity patterns.

---

## 📌 Core SQL Clauses

### ✅ 1. `GROUP BY`

Used to aggregate data **by one or more columns**.

```sql
SELECT city, COUNT(*) AS total_users
FROM users
GROUP BY city;
```

---

### ✅ 2. `HAVING`

Filters **aggregated results** (used after `GROUP BY`).

```sql
SELECT model_type, COUNT(*) AS count
FROM models
GROUP BY model_type
HAVING count > 5;
```

---

### ✅ 3. `DISTINCT`

Removes duplicate rows.

```sql
SELECT DISTINCT user_id
FROM model_predictions;
```

---

## 🧠 Real-World Relevance in AI/ML

| SQL Feature | AI Task Example |
|-------------|------------------|
| `GROUP BY`  | Get count of predictions per label or model |
| `HAVING`    | Filter models used more than N times |
| `DISTINCT`  | Remove duplicate entries (e.g., user, email, sample IDs) |

---

## ✅ Common Use Patterns

### a) Count label frequencies (classification task):

```sql
SELECT label, COUNT(*) AS count
FROM predictions
GROUP BY label;
```

---

### b) Get distinct cities with data contributors:

```sql
SELECT DISTINCT city
FROM contributors;
```

---

### c) Find models trained more than once:

```sql
SELECT model_name, COUNT(*) AS runs
FROM training_logs
GROUP BY model_name
HAVING runs > 1;
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| Difference between `WHERE` and `HAVING`? | `WHERE` filters **rows**, `HAVING` filters **aggregates** |
| Can you use `HAVING` without `GROUP BY`? | Technically yes (for aggregate filters), but uncommon |
| Can `DISTINCT` be used with multiple columns? | Yes — it applies to the combination of all selected columns |

---

## ✅ Tip

> `GROUP BY` + aggregation functions (`COUNT()`, `AVG()`, `SUM()`) is one of the most used SQL combos in AI analytics.

---

📁 **Next Folder:** [3 sql joins →](../3 sql joins/)