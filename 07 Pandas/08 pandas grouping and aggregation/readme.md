# 📊 Pandas Grouping & Aggregation – Feature Statistics for ML

This folder teaches you how to group, summarize, and analyze your AI/ML data using `groupby()` and `.agg()`. These techniques are **critical for feature engineering, reporting model performance, and exploratory data analysis**.

---

## 📌 Programs in This Folder

### 1. `1_groupby_basic.py`

Covers:
- Grouping by one column (`groupby("model")`)
- Calculating mean, count

Used in:
- Model-level score summaries
- Class-wise prediction counts

---

### 2. `2_groupby_multiple_columns.py`

Covers:
- Grouping by multiple columns (e.g. model + label)
- Multi-key performance stats

Used in:
- Accuracy per class per model
- User-task or class-time breakdown

---

### 3. `3_agg_sum_mean_count.py`

Covers:
- `.agg()` for multiple aggregation functions
- Mean, max, count, sum in one shot

Used in:
- Performance dashboards
- Feature summary per category or label
- Aggregating inference logs, user stats

---

## 🧠 Real-World AI/ML Relevance

| Grouping Goal                     | Pandas Logic |
|----------------------------------|--------------|
| Class-wise precision breakdown   | `groupby("label")["score"].mean()` |
| Model + Label matrix             | `groupby(["model", "label"])` |
| User/session-level summarization | `groupby(["user", "session"]).agg(...)` |
| Preprocessing dataset stats      | `groupby(...).agg()` |

---

## 💬 Interview Questions

1. How does `groupby()` work in Pandas?
2. How do you group by multiple columns?
3. What’s the use of `.agg()`?
4. How can you compute count and mean together for a group?

---

## ✅ Tip

> Use `.agg()` to reduce post-processing steps — especially when logging or tracking multiple KPIs per category.

---

📁 **Next Module:** You’ve completed the **Pandas Track!**