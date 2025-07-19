# 🧠 Basics of Python: Functions

This folder covers how to write **reusable blocks of code** using functions. Functions help you avoid repetition, make code more organized, and return useful outputs for further use.

In machine learning, functions are used everywhere — for data cleaning, model training, evaluation, API endpoints, and more.

---

## 📌 Programs in This Folder

### 1. `1_define_function.py`

Covers:
- How to define a basic function
- How to call it

Example:
```python
def greet():
    print("Hello, welcome to Python functions!")

greet()
```

💡 This is the foundation for reusable code. Define once, use many times.

---

### 2. `2_return_vs_print.py`

Covers:
- Difference between `return` and `print()`

Example:
```python
def add(a, b):
    return a + b
```

💡 `print()` only shows output, `return` gives you the value back to reuse later.

---

### 3. `3_default_arguments.py`

Covers:
- Setting default values for function parameters

Example:
```python
def greet(name="Guest"):
    print("Hello", name)
```

💡 If no value is passed, it uses the default — great for optional settings in AI/ML configs.

---

### 4. `4_positional_keyword_args.py`

Covers:
- Calling functions using position and keyword-based arguments

Example:
```python
def info(name, age):
    print(f"{name} is {age} years old")
```

💡 Helps you control how values are assigned to parameters.

---

### 5. `5_lambda_functions.py`

Covers:
- Anonymous one-line functions

Example:
```python
square = lambda x: x * x
```

💡 Used for quick calculations inside sorting, filtering, or ML pipeline steps.

---

### 6. `6_variable_scope_in_functions.py`

Covers:
- Local vs Global variable scope

Example:
```python
x = "global"

def print_scope():
    x = "local"
```

💡 Scope matters! Avoid bugs caused by variable name conflicts.

---

### 7. `7_args_function.py`

Covers:
- Passing multiple values using `*args`

Example:
```python
def sum_all(*args):
    return sum(args)
```

💡 Very useful when number of inputs is unknown (e.g. variable-sized feature lists)

---

### 8. `8_kwargs_function.py`

Covers:
- Passing multiple named values using `**kwargs`

Example:
```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

💡 Used in dynamic config setups, form data, API handling.

---

### 9. `9_yield_function.py`

Covers:
- Creating a generator using `yield`

Example:
```python
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
```

💡 Generators are memory-efficient — useful for processing large datasets, logs, or batches.

---

## 🎯 Real-World Relevance in AI/ML

- Use `def` to define preprocessing or model training steps
- Use `return` to output accuracy, predictions, metrics
- Use `lambda` for quick filters, transformations in pandas or sorting
- Use `*args` / `**kwargs` in ML config scripts, dynamic APIs
- Use `yield` to handle big data without loading everything in memory

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `print()` and `return` in a function?
2. When would you use `*args` and `**kwargs`?
3. What is the difference between a normal function and a generator (`yield`)?
4. What happens when you change a global variable inside a function?

---

## ✅ Tip

> Keep your functions short and focused. One function = one task.  
> Name them based on what they do, like `clean_data()`, `train_model()`, `log_accuracy()`.

---

📁 **Next Topic:** [7_data_structures_intro →](../7 data structures intro/)