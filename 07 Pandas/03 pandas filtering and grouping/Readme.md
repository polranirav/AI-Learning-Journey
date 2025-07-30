# 🔎 Pandas Filtering and Grouping – AI Data Selection Toolkit

This folder teaches you how to filter, combine, and summarize rows in a DataFrame — essential for preprocessing, error analysis, and understanding model behavior across classes.

---

## 📌 Programs in This Folder

### 1. `1_filtering_rows.py`

Covers:
- Filter rows using single condition
- Confidence thresholds
- Compare `label` vs `predicted`

Used in:
- Selecting high-confidence samples
- Identifying wrong predictions
- Isolating strong true positives

---

### 2. `2_logical_operators.py`

Covers:
- Combine filters with `&` (AND), `|` (OR)
- Use `~` (NOT) to inverse logic
- Complex conditional filtering

Used in:
- Filter risky, low-confidence predictions
- Extract only incorrect rows
- Advanced rule-based filtering

---

### 3. `3_groupby_aggregate.py`

Covers:
- `groupby()` on categorical column
- `.mean()` and `.count()` aggregation
- Analyze class-wise metrics

Used in:
- Calculating per-class confidence
- Evaluating accuracy per label
- Class imbalance checking

---

## 🧠 Real-World Relevance in AI/ML

| Concept        | Use Case |
|----------------|----------|
| `df[df[...]]`  | Filter predictions above/below threshold |
| `&`, `|`, `~`  | Combine logic rules (confidence + label) |
| `groupby()`    | Per-class summary, model audit |
| `.mean()`      | Class-wise confidence or accuracy |
| `.value_counts()` | Label distribution for imbalance detection |

---

## 💬 Interview Questions

1. How do you filter rows where prediction is wrong and confidence is low?
2. What’s the difference between `&` and `and` in Pandas filtering?
3. How can you compute average confidence per class?

---

## ✅ Tip

> Use `.groupby("label").mean()` to generate compact dashboards of model performance.

---

📁 **Next Topic:** [04 pandas merge and join →](../04 pandas merge and join/)