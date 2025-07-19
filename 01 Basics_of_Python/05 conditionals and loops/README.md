# 🧠 Basics of Python: Conditionals and Loops

This folder introduces how to **control the flow of your Python program** using conditions and loops. These are critical for logic, decision-making, and automation in any AI, ML, or backend application.

---

## 📌 Programs in This Folder

### 1. `1_if_statement.py`

Checks if a condition is true, and executes code block.

```python
temperature = 38
if temperature > 37:
    print("You may have a fever.")
```

---

### 2. `2_if_else_statement.py`

Provides two options based on the condition.

```python
age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### 3. `3_if_elif_else.py`

Checks multiple conditions in order.

```python
score = 75
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C or lower")
```

---

### 4. `4_nested_conditions.py`

Condition inside another condition.

```python
if is_logged_in:
    if has_access:
        print("Access granted")
```

---

### 5. `5_while_loop.py`

Repeats a block of code **while** the condition is true.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

### 6. `6_for_loop.py`

Loops over a **sequence (list, string, range, etc.)**

```python
for item in ["Python", "ML", "AI"]:
    print(item)
```

---

### 7. `7_nested_loops.py`

A loop inside another loop — useful for grids, matrices.

```python
for row in range(1, 3):
    for col in range(1, 4):
        print(f"({row},{col})")
```

---

### 8. `8_loop_control_break_continue.py`

Control how loops behave using `break` and `continue`.

```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
```

---

## 🎯 Real-World Relevance in AI/ML

| Concept     | Use Case Example |
|-------------|------------------|
| `if`        | Decide model outcome or user access |
| `for`       | Iterate over dataset rows or image pixels |
| `while`     | Polling, streaming, continuous checks |
| `break`     | Exit early if condition met (e.g., threshold) |
| `continue`  | Skip invalid entries |

---

## 🧠 Interview Questions to Practice

1. Difference between `for` and `while` loop?
2. When would you use `continue` in a loop?
3. How does `if-elif-else` flow work?

---

## ✅ Tip

> Always keep your logic **clean and readable**. Nesting too deep makes code hard to debug.

---

📁 **Next Topic:** [6_functions →](../6 functions/)