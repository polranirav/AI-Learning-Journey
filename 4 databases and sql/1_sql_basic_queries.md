# 🧠 SQL Basics – SELECT, WHERE, LIKE, BETWEEN, ORDER BY

This folder introduces the **most essential SQL commands** used by AI/ML engineers to extract and filter data before modeling. Nearly every dataset you’ll work with (in PostgreSQL, BigQuery, SQLite, etc.) will start with these operations.

---

## 📌 Core SQL Commands

### ✅ 1. `SELECT`

Used to extract columns from a table.

```sql
SELECT name, age FROM users;
```

---

### ✅ 2. `WHERE`

Filters rows based on a condition.

```sql
SELECT * FROM customers
WHERE age > 30 AND city = 'Toronto';
```

---

### ✅ 3. `LIKE`

Pattern matching with `%` (wildcard for any character sequence).

```sql
SELECT * FROM emails
WHERE address LIKE '%@gmail.com';
```

---

### ✅ 4. `BETWEEN`

Selects a range (inclusive).

```sql
SELECT * FROM orders
WHERE total BETWEEN 100 AND 500;
```

---

### ✅ 5. `ORDER BY`

Sorts results ascending or descending.

```sql
SELECT name, accuracy
FROM models
ORDER BY accuracy DESC;
```

---

## 🔍 Real-World AI/ML Use Cases

| SQL Feature | AI Task Example |
|-------------|-----------------|
| `SELECT` | Extract features before preprocessing |
| `WHERE` | Filter rows with missing/invalid values |
| `LIKE` | Find text columns (e.g., product_category LIKE '%ml%') |
| `BETWEEN` | Query samples in specific ranges (e.g., price, age) |
| `ORDER BY` | Rank models by performance, data by priority |

---

## ✅ Practice Queries for AI Context

1. **Get top 10 highest-accuracy models:**

```sql
SELECT name, accuracy
FROM models
ORDER BY accuracy DESC
LIMIT 10;
```

2. **Find all users who mentioned “machine learning” in bio:**

```sql
SELECT * FROM users
WHERE bio LIKE '%machine learning%';
```

3. **List records of data samples between 2018–2022:**

```sql
SELECT *
FROM dataset
WHERE year BETWEEN 2018 AND 2022;
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| What's the difference between `WHERE` and `HAVING`? | `WHERE` filters rows before grouping; `HAVING` filters after `GROUP BY` |
| Can `LIKE` match case-insensitive? | Depends on DB engine (`ILIKE` for PostgreSQL) |
| Can you use `ORDER BY` on non-selected columns? | Yes, as long as it's part of the table |

---

## 🧠 Tip

> Combine `WHERE` with `BETWEEN`, `LIKE`, and `ORDER BY` to narrow down massive datasets before feeding into ML pipelines.

---

📁 **Next Folder:** [2 sql grouping and filters →](../2 sql grouping and filters/)