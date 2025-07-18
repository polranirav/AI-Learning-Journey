# 🧠 Basics of Python: Data Types

This folder covers the **core built-in data types in Python**, which form the foundation of how you store, process, and interact with data in AI/ML or automation projects.

---

## 📌 Programs in This Folder

### 1. `1_integer_type.py`

Covers:
- Declaring integer values
- Basic arithmetic operations

Example:
```python
age = 25
items_in_stock = 120

total_items = items_in_stock + 10
remaining_items = items_in_stock - 5
```

💡 **Why it matters:**  
Used to store counts, quantities, and IDs in datasets.

---

### 2. `2_float_type.py`

Covers:
- Float values (decimal numbers)
- Precision and rounding

Example:
```python
price = 49.99
tax = 0.13
total = price + (price * tax)
print("Rounded total:", round(total, 2))
```

💡 **Why it matters:**  
Used in ML models for loss values, accuracy percentages, probabilities, etc.

---

### 3. `3_string_type.py`

Covers:
- String creation, indexing, and slicing

Example:
```python
product = "Laptop"
print(product[0])     # L
print(product[-3:])   # top
```

💡 **Why it matters:**  
Essential in text data processing (NLP), file names, column names, etc.

---

### 4. `4_boolean_type.py`

Covers:
- `True` and `False` values

Example:
```python
in_stock = True
is_discounted = False
```

💡 **Why it matters:**  
Booleans are used in flags, conditions, and binary classification outputs.

---

### 5. `5_none_type.py`

Covers:
- Using `None` as a placeholder for “no value yet”

Example:
```python
email = None
```

💡 **Why it matters:**  
Used when a value is missing in a dataset or is yet to be assigned.

---

### 6. `6_type_casting.py`

Covers:
- Converting between data types using `int()`, `float()`, `str()`

Example:
```python
a = "100"
b = float(a) + 0.5
c = str(b)
```

💡 **Why it matters:**  
You'll constantly convert between types when reading from files, APIs, or user inputs.

---

### 7. `7_type_checking.py`

Covers:
- Checking data type using `type()` and `isinstance()`

Example:
```python
x = 10
print(type(x))               # <class 'int'>
print(isinstance(x, int))    # True
```

💡 **Why it matters:**  
Type checking prevents bugs in model training and input validation.

---

### 8. `8_data_type_mixed_usage.py`

Covers:
- Mixing multiple types in one realistic context

Example:
```python
name = "Patient A"
age = 30
temperature = 98.6
is_critical = False

print(f"{name}, Age: {age}, Temp: {temperature}, Critical: {is_critical}")
```

💡 **Why it matters:**  
Most AI/ML data samples are a combination of strings, numbers, and boolean flags.

---

## 🎯 Real-World Relevance in AI/ML

| Data Type | Real Use Case Example |
|-----------|------------------------|
| `int`     | Index, class labels, epoch count |
| `float`   | Accuracy, learning rate, loss |
| `str`     | NLP text, column names |
| `bool`    | Binary classifier output, flags |
| `None`    | Missing values in datasets |

---

## 🧠 Interview Questions to Practice

1. What's the difference between `int` and `float` in Python?
2. What is `NoneType` and how is it different from `False`?
3. What’s the difference between `type()` and `isinstance()`?

---

## ✅ Tip

> In real AI datasets, always clean and convert data types before training models.  
> Use `type()` and `isinstance()` to debug issues early.

---

📁 **Next Topic:** [4_operators_and_expressions →](../04 operators and expressions/)