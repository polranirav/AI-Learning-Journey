# 🧠 Basics of Python: Data Structures (Intro)

This folder introduces the **core built-in data structures** in Python — such as lists, tuples, sets, and dictionaries. These structures help store, organize, and access data efficiently, and they are used heavily in data science, machine learning, and real-world applications.

---

## 📌 Programs in This Folder

### 1. `1_list_basics.py`

Covers:
- List creation
- Indexing and accessing nested values

Example:
```python
numbers = [1, 2, 3]
mixed = [1, "text", True, None, [10, 20]]
```

💡 Lists are ordered and mutable — useful for storing datasets, model predictions, etc.

---

### 2. `2_tuple_vs_list.py`

Covers:
- Difference between tuples and lists

Example:
```python
my_list = [1, 2, 3]       # mutable
my_tuple = (1, 2, 3)      # immutable
```

💡 Tuples are often used for fixed data and function returns.

---

### 3. `3_set_usecase.py`

Covers:
- Sets: unordered collections of unique values

Example:
```python
unique_vals = set([1, 2, 2, 3, 4])
```

💡 Use sets to remove duplicates or perform union/intersection operations.

---

### 4. `4_dict_basics.py`

Covers:
- Key-value mapping with dictionaries

Example:
```python
person = {"name": "Nirav", "age": 25}
```

💡 Dictionaries are useful for storing structured data like records, config files, JSON responses.

---

### 5. `5_nested_data_structures.py`

Covers:
- Deep nesting of list, dict, and more

Example:
```python
student = {
    "name": "Nirav",
    "grades": {"math": 90},
    "projects": [{"title": "AI Bot"}]
}
```

💡 Nested data structures are common in APIs, JSON, and ML pipelines.

---

### 6. `6_slice_examples.py`

Covers:
- How to extract sub-parts of a list using slicing

Example:
```python
data = [10, 20, 30, 40]
print(data[1:3])      # [20, 30]
print(data[::-1])     # reversed list
```

💡 Slicing is a powerful way to select ranges or reverse sequences without loops.

---

### 7. `7_bracket_vs_types.py`

Covers:
- The purpose of different brackets in Python

Example:
```python
[]  → list
()  → tuple
{}  → dictionary or set (depending on usage)
```

💡 Knowing the meaning of bracket styles helps you instantly recognize the data type you're working with.

---

## 🎯 Real-World Relevance in AI/ML

| Data Structure | Used For |
|----------------|----------|
| List           | Store rows, columns, model outputs |
| Tuple          | Return multiple values from a function |
| Set            | Store unique features or label classes |
| Dict           | Represent structured data like config, parameters |
| Slice          | Extract subsets from data (e.g., training split) |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between a list and a tuple?
2. How do you remove duplicates from a list?
3. How is a dictionary different from a list?
4. What does `[::-1]` do in a list?

---

## ✅ Tip

> Use lists when order matters and you need to modify values.  
> Use tuples for fixed values.  
> Use dictionaries for fast lookups.  
> Use sets to automatically remove duplicates.

---

📁 **Next Topic:** [8 object oriented programming →](../08%20object%20oriented%20programming/)