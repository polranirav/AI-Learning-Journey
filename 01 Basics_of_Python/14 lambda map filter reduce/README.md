# 🧠 Python: Lambda, Map, Filter, Reduce

This folder introduces **functional programming tools** in Python, which help you write **compact, fast, and readable logic**.

These tools are used in:
- Data pipelines
- Feature transformations
- Text preprocessing
- AI/NLP input cleaning

---

## 📌 Programs in This Folder

### 1. `1_lambda_basics.py`

Covers:
- Creating quick, one-line anonymous functions

Example:
```python
lambda x: x * x
```

💡 Use when the function is small and only used once.

---

### 2. `2_map_with_lambda.py`

Covers:
- Apply a transformation to each item

Example:
```python
map(lambda x: x * 2, data)
```

💡 Common in scaling features or formatting text fields.

---

### 3. `3_filter_with_lambda.py`

Covers:
- Filter out unwanted items

Example:
```python
filter(lambda x: x % 2 == 0, numbers)
```

💡 Used in preprocessing to remove outliers, blanks, or bad rows.

---

### 4. `4_reduce_with_lambda.py`

Covers:
- Reduce a list to a single result

Example:
```python
reduce(lambda x, y: x + y, data)
```

💡 Used to calculate total, min/max, or cumulative scores.

---

### 5. `5_function_vs_lambda.py`

Covers:
- Difference between traditional functions and lambda

Example:
```python
lambda x: x + 1 vs def add_one(x): return x + 1
```

💡 Helps you decide when to use which.

---

### 6. `6_real_usecase_text_cleaning.py`

Covers:
- Real-world example: trim and clean list of messy strings

Steps:
1. Use `map()` to `.strip()` whitespace
2. Use `filter()` to remove blanks

💡 Ideal for text cleanup in AI/NLP projects.

---

## 🎯 Real-World Relevance in AI/ML

| Tool      | Use Case Example |
|-----------|------------------|
| `lambda`  | Quick custom logic (sort key, transform) |
| `map()`   | Apply functions to features or text |
| `filter()`| Remove noise or outliers |
| `reduce()`| Aggregate scores or combine results |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `map()` and `filter()`?
2. When would you use `lambda` instead of a `def` function?
3. What does `reduce()` do in Python?
4. How can you chain `map` and `filter` together?

---

## ✅ Tip

> These tools shine when you **chain small transformations together** in a pipeline — especially for cleaning, feature engineering, or fast one-off logic.

---

📁 **Next Topic:** [15 multithreading and multiprocessing →](../15 multithreading and multiprocessing/)