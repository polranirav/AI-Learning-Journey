# 🧠 Python: Comprehensions

This folder covers **list, set, dict, and generator comprehensions** — compact ways to build new collections from existing ones.

Comprehensions are commonly used in:
- AI pipelines to transform or filter data
- NLP tasks for cleaning text
- Quick preprocessing and feature engineering

---

## 📌 Programs in This Folder

### 1. `1_list_comprehension_basic.py`

Covers:
- Convert a loop to a single-line list expression

Example:
```python
[x ** 2 for x in range(5)]
```

💡 Cleaner and faster than traditional `for` loops.

---

### 2. `2_list_comprehension_with_condition.py`

Covers:
- Add a condition inside the comprehension

Example:
```python
[x for x in range(10) if x % 2 == 0]
```

💡 Common in filtering out bad values, even/odd selection, etc.

---

### 3. `3_nested_list_comprehension.py`

Covers:
- Flatten a nested list in one line

Example:
```python
[num for row in matrix for num in row]
```

💡 Great for working with 2D data or tabular rows/columns.

---

### 4. `4_set_comprehension.py`

Covers:
- Create a set with only unique values

Example:
```python
{x ** 2 for x in data}
```

💡 Removes duplicates automatically — great for fast lookups.

---

### 5. `5_dict_comprehension.py`

Covers:
- Build a dictionary in one line

Example:
```python
{k: v for k, v in zip(keys, values)}
```

💡 Common in converting two lists into key-value pairs or mapping labels to IDs.

---

### 6. `6_generator_expression.py`

Covers:
- Lazy evaluation using generators (memory efficient)

Example:
```python
(x * 2 for x in range(1000))
```

💡 Used for big data streams, reading large files, or infinite loops.

---

## 🎯 Real-World Relevance in AI/ML

| Type             | Example Use Case |
|------------------|------------------|
| List Comp        | Clean or filter data in-place |
| Set Comp         | Remove duplicates in preprocessing |
| Dict Comp        | Map feature names to indexes |
| Generator        | Stream large batches efficiently |

---

## 🧠 Interview Questions to Practice

1. What is the benefit of using list comprehension over a regular loop?
2. How would you flatten a 2D list using comprehension?
3. What’s the difference between a list and a generator comprehension?
4. Can you add conditions inside a comprehension?

---

## ✅ Tip

> Use comprehensions when you want **clear, concise, and efficient transformations** — but avoid making them too complex to read.

---

📁 **Next Topic:** [14 lambda map filter reduce →](../14 lambda map filter reduce/)