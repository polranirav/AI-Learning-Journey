# 🧠 Basics of Python: Variables and Constants

This folder covers one of the most important foundations of Python — **how data is stored, named, and managed in memory**. Every machine learning model, dataset, and algorithm depends heavily on variables to function correctly.

---

## 📌 Programs in This Folder

### 1. `1_variable_assignment.py`

Covers:
- How to declare variables
- How to store different types of values
- Using `type()` to check data type

Example:
```python
name = "Nirav"
age = 25
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
```

---

### 2. `2_dynamic_typing_demo.py`

Covers:
- Python allows changing variable type on the fly (dynamic typing)
- Using `type()` to debug
- 🔸 Basic use of function (full topic in Folder 6)

Example:
```python
x = 10
print("x:", x, "|", type(x))

x = "AI Engineer"
print("Now x:", x, "|", type(x))

# 🔸 Function used here — we'll fully cover functions in Folder 6
def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Nirav"))
```

---

### 3. `3_multiple_assignments.py`

Covers:
- Assigning multiple values in one line
- Swapping values without temporary variable (Python trick)

Example:
```python
a, b, c = 10, 20.5, "Python"
a, b = b, a  # Swap values
```

---

### 4. `4_constants_convention.py`

Covers:
- Python has no built-in `const` keyword
- Use **UPPERCASE names** to declare constants by convention
- Constants can still be changed, but it’s considered bad practice

Example:
```python
PI = 3.14159
GRAVITY = 9.8
```

---

### 5. `5_variable_scope.py`

Covers:
- Local vs Global scope
- Using the `global` keyword

Example:
```python
global_var = "I'm global"

def change_global():
    global global_var
    global_var = "Changed"
```

---

### 6. `6_variable_naming_rules.py`

Covers:
- Valid and invalid variable names
- Python keywords (e.g., `class`, `def`, `if`) can’t be used as variable names
- PEP8 naming style

Examples:
```python
student_name = "Nirav"
_age = 21
DOB2025 = "01-01-2025"
```

---

## 🧪 Bonus Interview Practice

These are small logic-based programs that are often used in interviews to test your thinking and variable usage.

### 7. `7_swap_variables.py`

```python
# Swap two numbers without a third variable
a = 5
b = 10
a, b = b, a
print("a =", a, "b =", b)
```

---

## 🎯 Real-World Relevance in AI/ML

- Variables hold config values (like learning rate, batch size, epochs)
- Constants store fixed paths, thresholds, or hyperparameters
- Clean naming reduces bugs and improves model readability
- Scope affects reusability of helper functions and models

---

## 🧠 Interview Questions to Practice

1. What’s the difference between variable declaration in Python vs Java/C++?
2. How does Python handle constants?
3. What happens if you use the same variable name inside and outside a function?

---

## ✅ Tip

> Use meaningful variable names in ML projects like `num_epochs`, `input_dim`, `learning_rate` — not `a`, `b`, `c`.

---

📁 **Next Topic:** [3_data_types →](../03 data types/)