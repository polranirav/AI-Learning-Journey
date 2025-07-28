# 🧠 SQL Subqueries & CTEs – Clean, Modular Data Logic

Subqueries and CTEs (Common Table Expressions) allow you to **organize complex SQL** in a readable, reusable way. They’re especially useful when chaining logic for preprocessing or analytics in ML workflows.

---

## 📌 Key Concepts

### ✅ 1. Subqueries (Nested Queries)

A query inside another query — usually in `WHERE`, `FROM`, or `SELECT`.

```sql
SELECT name
FROM users
WHERE id IN (
    SELECT user_id FROM predictions WHERE predicted_label = 'fraud'
);
```

---

### ✅ 2. CTE (Common Table Expression)

Defined using `WITH`, it lets you create a **temporary named table** for use in a bigger query.

```sql
WITH high_scores AS (
    SELECT user_id, MAX(score) AS best_score
    FROM model_scores
    GROUP BY user_id
)
SELECT u.name, h.best_score
FROM users u
JOIN high_scores h ON u.id = h.user_id;
```

🧠 Much easier to **debug and modularize** than nesting.

---

## 🧪 Subquery Use Cases in AI

| Task | Subquery Example |
|------|------------------|
| Filter top scorers | WHERE score > (SELECT AVG(score) ...) |
| Find duplicated users | SELECT email FROM users GROUP BY email HAVING COUNT(*) > 1 |
| Detect missing predictions | WHERE user_id NOT IN (SELECT user_id FROM predictions) |

---

## 🔬 CTE Use Cases in ML Pipelines

| Step | CTE Example |
|------|-------------|
| Preprocessing | WITH filtered AS (...) SELECT FROM filtered ... |
| Ranking models | WITH ranked AS (SELECT, RANK() OVER (...)) |
| Reusing base table | Join multiple times without repeating logic |

---

## 📊 When to Use What?

| Feature | When to Use |
|---------|-------------|
| Subquery | Quick filter or one-off logic |
| CTE      | Multi-step analysis or long query |
| Subquery in `SELECT` | Derive custom fields |
| CTE with multiple joins | Track processing stages (great for data pipelines) |

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| What’s the difference between CTE and subquery? | CTE is named, reusable, and easier to debug. Subquery is inline. |
| Can CTEs be nested or chained? | Yes — you can stack multiple CTEs |
| Are CTEs faster than subqueries? | Not always. They’re about **clarity**, not speed |

---

## ✅ Tip

> Use CTEs when your query starts getting **too nested or unreadable** — especially when building AI data pipelines.

---

📁 **Next Folder:** [5 sql window functions →](../5 sql window functions/)