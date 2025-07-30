# 🧠 Pandas Apply vs Map – Transforming AI DataFrame Logic

This folder explains how to use `.apply()` and `.map()` — essential tools to transform or tag data programmatically. These are widely used in AI pipelines for scoring, feature engineering, prediction classification, and label encoding.

---

## 📌 Programs in This Folder

### 1. `1_apply_function.py`

Covers:
- Define a custom Python function
- Apply it to a column using `.apply()`

Used in:
- Mapping probability → "high/medium/low"
- Post-processing model output with custom rules

---

### 2. `2_apply_lambda.py`

Covers:
- Use inline lambda function for quick logic
- Add columns like risk flag or string length

Used in:
- Quick feature engineering
- Compact logic without defining full functions

---

### 3. `3_map_vs_apply.py`

Covers:
- Difference between `.map()` and `.apply()`
- `.map()` with dictionary for label replacement
- `.apply()` with lambda for scoring bucket

Used in:
- Token to emoji conversion
- Converting predictions into interpretable outputs

---

## 🧠 Real-World Relevance in AI/ML

| Transformation     | Best Tool |
|--------------------|-----------|
| Label to token ID  | `map()`   |
| Label to emoji     | `map()`   |
| Score to grade     | `apply()` |
| Custom postprocess | `apply()` |
| Count tokens/length| `apply()` |

---

## 💬 Interview Questions

1. What’s the difference between `.map()` and `.apply()` in Pandas?
2. When would you use a lambda inside `.apply()`?
3. Can `.apply()` be used on the entire DataFrame?

---

## ✅ Tip

> Use `.map()` for dictionary replacements or simple column transforms.  
> Use `.apply()` when logic needs a function or row-level logic.

---

📁 **Next Topic:** [9 pandas grouping and aggregation →](../9 pandas grouping and aggregation/)