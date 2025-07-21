# 🧠 Basics of Python: Operators and Expressions

This folder introduces you to **Python operators** — special symbols used to perform operations on variables and values. You’ll use these in every program, ML model, and even while writing logic for AI applications.

---

## 📌 Programs in This Folder

### 1. `1_arithmetic_operators.py`

Covers:
- Basic math operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`

Example:
```python
a = 10
b = 3
print(a + b)   # 13
print(a // b)  # 3 (floor division)
```

💡 **Why it matters:**  
You'll use these when calculating metrics like accuracy, loss, learning rate, etc.

---

### 2. `2_assignment_operators.py`

Covers:
- `=`, `+=`, `-=`, `*=`, `/=`

Example:
```python
x = 5
x += 2  # x becomes 7
```

💡 **Why it matters:**  
Common in loops and ML training counters (like `epoch += 1`)

---

### 3. `3_comparison_operators.py`

Covers:
- Compare values: `==`, `!=`, `>`, `<`, `>=`, `<=`

Example:
```python
a = 10
print(a > 5)   # True
```

💡 **Why it matters:**  
Used in filtering data, validating inputs, comparing predictions.

---

### 4. `4_logical_operators.py`

Covers:
- Boolean logic: `and`, `or`, `not`

Example:
```python
a = True
b = False
print(a and b)  # False
```

💡 **Why it matters:**  
Very useful for combining multiple ML conditions (e.g., "is image valid and has label?")

---

### 5. `5_bitwise_operators.py`

Covers:
- Bitwise operations: `&`, `|`, `^`, `~`, `<<`, `>>`

🧠 **Beginner-Friendly Explanation:**

Bitwise operators work at the **binary level** (0s and 1s).
They are:
- `&` → AND  
- `|` → OR  
- `^` → XOR  
- `~` → NOT  
- `<<` → Left shift (multiply by 2)  
- `>>` → Right shift (divide by 2)

Example:
```python
a = 5   # binary = 0101
b = 3   # binary = 0011
print(a & b)  # 0001 → 1
```

💡 **Why it matters:**  
Not often used in AI/ML, but common in:
- Embedded systems
- Image filters
- Interview logic puzzles

---

### 6. `6_membership_identity.py`

Covers:
- Membership: `in`, `not in`
- Identity: `is`, `is not`

Example:
```python
colors = ["red", "blue"]
print("red" in colors)  # True
```

💡 **Why it matters:**  
Used in checking if a value exists in a list or comparing memory references (e.g., `is None`).

---

### 7. `7_ai_expression_example.py`

Covers:
- Real-world logic using multiple operators

Example:
```python
is_logged_in = True
has_permission = True
age = 22
can_access = is_logged_in and has_permission and age >= 18
```

💡 **Why it matters:**  
This kind of compound expression is used in dashboards, access control, feature toggles, etc.

---

## 🎯 Real-World Relevance in AI/ML

| Operator Type     | Real Use Case |
|------------------|---------------|
| Arithmetic        | Math for metrics (accuracy, loss) |
| Assignment        | Loop counters, weights, tracking |
| Comparison        | Threshold logic, filtering |
| Logical           | Conditions in model config |
| Membership        | Column checking in DataFrames |
| Identity          | Checking `None`, object IDs |
| Bitwise (rare)    | Compression, low-level optimization |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `=` and `==`?
2. What does the expression `a and not b` mean in Python?
3. How does `is` differ from `==`?
4. What does `a << 1` do to the value of `a`?

---

## ✅ Tip

> You can combine any number of operators in one line — but keep it readable.

---

📁 **Next Topic:** [5_conditionals_and_loops →](../05 conditionals and loops/)