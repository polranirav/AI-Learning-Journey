# 🧠 Python: Decorators

Decorators let you **modify or enhance the behavior of functions** without changing their actual code.  
They’re used heavily in Python APIs, ML pipelines, logging, monitoring, and more.

You’ve likely seen them in:
- `@app.get()` (FastAPI)
- `@staticmethod`, `@classmethod`
- `@retry`, `@log`, `@timer` in production ML code

---

## 📌 Programs in This Folder

### 1. `1_decorator_basics.py`

Covers:
- Creating and applying a simple decorator

Example:
```python
@my_decorator
def func(): ...
```

💡 Adds extra logic before/after a function.

---

### 2. `2_decorator_with_args.py`

Covers:
- Create decorators that accept arguments

Example:
```python
@repeat(3)
def greet(): ...
```

💡 Useful for retries, timed loops, etc.

---

### 3. `3_multiple_decorators.py`

Covers:
- Stack multiple decorators on a single function

Example:
```python
@bold
@italic
def text(): ...
```

💡 Great for formatting, validation, or multiple checks.

---

### 4. `4_class_based_decorator.py`

Covers:
- Create a class-based decorator using `__call__`

💡 Gives you more control over state, reuse, and arguments.

---

### 5. `5_real_usecase_logging.py`

Covers:
- Add logging before and after a function runs

Example:
```python
@log_call
def train_model(): ...
```

💡 Very useful for monitoring ML training or data tasks.

---

### 6. `6_real_usecase_timing.py`

Covers:
- Measure how long a function takes to run

Example:
```python
@timer
def compute(): ...
```

💡 Ideal for profiling feature engineering or model scoring time.

---

### 7. `7_builtin_decorators_reference.py`

Covers:
- `@staticmethod` and `@classmethod` usage

💡 Often used in OOP-heavy ML classes (e.g., PyTorch `nn.Module`)

---

## 🎯 Real-World Relevance in AI/ML

| Decorator Use Case | Example |
|--------------------|---------|
| `@timer`           | Measure training time, preprocessing latency |
| `@log_call`        | Monitor when models or stages are called |
| `@repeat(n)`       | Retry API fetch or model inference |
| `@staticmethod`    | Utility tools inside ML classes |
| `@classmethod`     | Config builders or shared setup logic |

---

## 🧠 Interview Questions to Practice

1. What is a decorator in Python?
2. How do you pass arguments into a decorator?
3. What’s the difference between `@staticmethod` and `@classmethod`?
4. Can you create a decorator that logs and times a function?

---

## ✅ Tip

> Decorators are great for adding cross-cutting concerns like logging, validation, or performance tracking — without touching the core logic.

---

📁 **Next Topic:** [17 generators and iterators →](../17 generators and iterators/)