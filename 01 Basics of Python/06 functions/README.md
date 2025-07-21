# 🧠 Basics of Python: Functions

This folder introduces **functions**, the building blocks for writing reusable, readable, and organized code. You'll use them in every AI/ML project — from data preprocessing to API development.

---

## 📌 Programs in This Folder

### 1. `1_define_function.py`

Defines and calls a basic function.

```python
def greet():
    print("Hello!")
greet()
```

---

### 2. `2_return_vs_print.py`

Shows the difference between returning a value and printing it.

```python
def add(a, b):
    return a + b
```

Use `return` to reuse values, `print()` just displays them.

---

### 3. `3_default_arguments.py`

Adds optional default values to parameters.

```python
def greet(name="Guest"):
    print("Hello", name)
```

---

### 4. `4_positional_keyword_args.py`

Demonstrates different ways to pass arguments.

```python
def user_info(name, age):
    print(name, age)
```

---

### 5. `5_lambda_functions.py`

One-line anonymous function.

```python
square = lambda x: x * x
```

Useful for sorting, filtering, ML preprocessing.

---

### 6. `6_variable_scope_in_functions.py`

Shows local vs global scope.

```python
x = "global"
def func():
    x = "local"
```

---

### 7. `7_args_function.py`

Handles any number of positional arguments.

```python
def sum_all(*args):
    return sum(args)
```

---

### 8. `8_kwargs_function.py`

Handles any number of keyword arguments.

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

---

### 9. `9_yield_function.py`

Creates a **generator** using `yield`.

```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
```

Efficient for looping through large data — commonly used in batch processing.

---

## 🎯 Real-World Relevance in AI/ML

| Concept         | Use Case Example |
|-----------------|------------------|
| `def`           | Model training steps, cleaning |
| `*args`         | Pass multiple values (hyperparameters) |
| `**kwargs`      | Pass dynamic options (API configs) |
| `lambda`        | Quick logic in sorting, filtering |
| `yield`         | Efficient iteration (large data, generators) |

---

## 🧠 Interview Questions to Practice

1. What is the difference between `*args` and `**kwargs`?
2. What is the purpose of `yield` in Python?
3. What’s the difference between `return` and `print()`?
4. What happens when you change a global variable inside a function?

---

## ✅ Tip

> Keep your functions short, well-named, and reusable. Avoid writing long logic blocks inside loops.

---

📁 **Next Topic:** [7_data_structures_intro →](../7_data_structures_intro/)