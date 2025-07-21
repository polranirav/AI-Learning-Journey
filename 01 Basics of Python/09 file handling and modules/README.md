# 🧠 Basics of Python: File Handling & Modules

This folder covers how to **read/write files** and **organize code into modules** — both of which are essential in AI and real-world projects. You’ll use file handling to read datasets, logs, and configs, and use modules to split large projects into reusable files.

---

## 📌 Programs in This Folder

### 1. `1_file_read_basic.py`

Covers:
- Reading entire file content
- Reading line by line

Example:
```python
file = open("sample.txt", "r")
content = file.read()
```

💡 Useful for reading raw datasets, logs, or plain text input.

---

### 2. `2_file_write_append.py`

Covers:
- Writing new content to a file (`w`)
- Adding content without deleting old content (`a`)

Example:
```python
file = open("output.txt", "a")
file.write("Appending this line.\n")
```

---

### 3. `3_with_open_syntax.py`

Covers:
- Safe file handling using `with`

Example:
```python
with open("file.txt", "r") as file:
    print(file.read())
```

💡 Automatically closes the file — avoids memory leaks or locked files.

---

### 4. `4_file_modes_demo.py`

Covers:
- File modes: `'r'`, `'w'`, `'a'`, `'x'`, `'rb'`, `'wb'`

Example:
```python
open("file.txt", "w")  # write mode
```

💡 Knowing modes prevents accidental file overwrites.

---

### 5. `5_read_csv_like_data.py`

Covers:
- Reading CSV-style file line by line and splitting

Example:
```python
for line in file:
    row = line.strip().split(",")
```

💡 Simulates reading a real dataset row by row.

---

### 6. `6_module_import_basics.py`

Covers:
- Importing from another `.py` file (custom module)

Example:
```python
import helper_module
```

💡 Helps you reuse logic like `square()`, `clean_text()`, etc.

---

### 7. `helper_module.py`

Covers:
- Custom reusable functions

Example:
```python
def square(x): return x * x
```

💡 Like your personal toolbox for reusable functions.

---

### 8. `8_builtin_module_usage.py`

Covers:
- Using standard modules like `math`, `random`, `os`

Example:
```python
import math
math.sqrt(16)
```

💡 Useful for calculations, randomness, file paths, etc.

---

### 9. `9_main_guard_demo.py`

Covers:
- Preventing auto-execution of code on import

Example:
```python
if __name__ == "__main__":
    say_hello()
```

💡 Critical when you build large projects with multiple files.

---

## 🎯 Real-World Relevance in AI/ML

| Concept           | Use Case |
|------------------|----------|
| File Read/Write  | Load datasets, write logs/results |
| `with open()`    | Avoid file leaks in long training jobs |
| Modules          | Organize data cleaning, training, evaluation |
| `if __name__...` | Keeps code reusable and import-safe |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between `w` and `a` file modes?
2. How does `with open(...)` help?
3. Why use `__name__ == "__main__"` in a Python file?
4. How can you reuse functions from another `.py` file?

---

## ✅ Tip

> Build your own `helpers.py` for preprocessing, logging, evaluation functions and import them as modules in any future project.

---

📁 **Next Topic:** [10_exceptions and error handling →](../10_exceptions_and_error_handling/)