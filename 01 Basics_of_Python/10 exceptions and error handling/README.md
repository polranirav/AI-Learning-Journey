# 🧠 Basics of Python: Exceptions and Error Handling

This folder covers how to write **crash-proof Python code** using `try/except`, validations, and custom error messages. This is especially useful in AI/ML pipelines where one bad input, file, or config shouldn't break the entire system.

---

## 📌 Programs in This Folder

### 1. `1_basic_try_except.py`

Covers:
- Simple `try` block with fallback

Example:
```python
try:
    result = 10 / 0
except:
    print("An error occurred.")
```

💡 Prevents program from crashing.

---

### 2. `2_specific_exceptions.py`

Covers:
- Catching specific errors like `ValueError`, `ZeroDivisionError`

Example:
```python
except ValueError:
    print("Only numbers are allowed.")
```

💡 Helps you write clearer, more targeted error messages.

---

### 3. `3_try_else_finally.py`

Covers:
- Full structure: `try`, `except`, `else`, `finally`

Example:
```python
try:
    ...
except:
    ...
else:
    ...
finally:
    ...
```

💡 `finally` always runs — useful for closing files or cleaning up.

---

### 4. `4_raise_custom_error.py`

Covers:
- Raising an exception on purpose when conditions aren't met

Example:
```python
if amount > balance:
    raise ValueError("Insufficient balance.")
```

💡 Used to catch invalid ML parameters, thresholds, etc.

---

### 5. `5_assert_statement.py`

Covers:
- Internal logic check with `assert`

Example:
```python
assert y != 0, "Denominator cannot be zero"
```

💡 Helps ensure input/output expectations are met during development.

---

### 6. `6_custom_exception_class.py`

Covers:
- Creating your own exception class

Example:
```python
class NegativeNumberError(Exception):
    pass
```

💡 Asked in interviews. Useful in frameworks where you define domain-specific rules.

---

### 7. `7_file_read_safe.py`

Covers:
- Handling file-not-found gracefully

Example:
```python
except FileNotFoundError:
    print("File is missing.")
```

💡 Very useful when loading data, models, configs in AI projects.

---

### 8. `8_input_validation_example.py`

Covers:
- Validating user input with `try/except` and `raise`

Example:
```python
if age < 0:
    raise ValueError("Age cannot be negative.")
```

💡 Prevents invalid user input or corrupt pipeline configs.

---

## 🎯 Real-World Relevance in AI/ML

| Concept         | Use Case Example |
|-----------------|------------------|
| `try/except`    | Handle bad inputs or missing files |
| `raise`         | Stop training if config is invalid |
| `assert`        | Ensure shapes/values are valid in preprocessing |
| File handling   | Catch `FileNotFoundError` during data/model loading |
| Custom errors   | Create domain-specific validators for ML logic |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `except:` and `except ValueError:`?
2. When would you use `raise` instead of `assert`?
3. How do you define a custom exception in Python?
4. What’s the purpose of `finally` in a try block?

---

## ✅ Tip

> In production AI code, always wrap file reads, model loading, and data parsing in `try/except` to keep systems running even with bad inputs.

---

📁 **Next Topic:** [11 regular expressions →](../11 regular expressions/)