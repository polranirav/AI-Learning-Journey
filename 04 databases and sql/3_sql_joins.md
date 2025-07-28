# 🔗 SQL Joins – `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`

Joins help you combine data from **multiple related tables**. This is essential in AI/ML workflows, where you may need to pull together metadata, user logs, model results, or external datasets.

---

## 📌 Common Join Types

### ✅ 1. `INNER JOIN`

Returns only matching rows between tables.

```sql
SELECT u.id, u.name, m.model_score
FROM users u
INNER JOIN model_scores m ON u.id = m.user_id;
```

🧠 Used when you **only need rows present in both tables**.

---

### ✅ 2. `LEFT JOIN` (a.k.a. LEFT OUTER)

Returns **all rows from left table**, and matching rows from the right (if any).

```sql
SELECT u.name, m.model_score
FROM users u
LEFT JOIN model_scores m ON u.id = m.user_id;
```

🧠 Used to keep all users, even those with no models yet.

---

### ✅ 3. `RIGHT JOIN`

Returns **all rows from right table**, and matching rows from the left.

```sql
SELECT u.name, m.model_score
FROM users u
RIGHT JOIN model_scores m ON u.id = m.user_id;
```

⚠️ Not supported in some engines (like SQLite) — use `LEFT JOIN` by reversing table order.

---

### ✅ 4. `FULL OUTER JOIN`

Returns all rows from **both tables**, with NULLs where no match.

```sql
SELECT u.name, m.model_score
FROM users u
FULL OUTER JOIN model_scores m ON u.id = m.user_id;
```

🧠 Shows **complete picture** — who has scores, who doesn’t.

---

## 📊 Real-World Use in AI/ML

| Join Type | AI Task Example |
|-----------|------------------|
| INNER     | Join training logs with users who actually trained |
| LEFT      | Keep all users, add model results if available |
| RIGHT     | Rare — keep all scores, even if orphaned |
| FULL      | Combine datasets with partial overlap (e.g., different labeling tools) |

---

## 🧪 Practice Examples

### a) Join users and predictions:

```sql
SELECT u.id, u.name, p.predicted_label
FROM users u
INNER JOIN predictions p ON u.id = p.user_id;
```

---

### b) Keep users even without predictions:

```sql
SELECT u.name, p.predicted_label
FROM users u
LEFT JOIN predictions p ON u.id = p.user_id;
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| Difference between INNER and LEFT JOIN? | INNER = both match. LEFT = keep all left, even if right missing |
| What happens when there’s no match in LEFT JOIN? | NULL is inserted in right-side columns |
| Can we use multiple JOINs? | Yes — chain them for multi-table joins |
| Which JOIN gives biggest result set? | FULL OUTER JOIN (contains all data) |

---

## ✅ Tip

> Use `LEFT JOIN` often in AI pipelines when you want to **preserve your primary dataset** and attach secondary info if available.

---

📁 **Next Folder:** [4 sql subqueries and cte →](../4 sql subqueries and cte/)