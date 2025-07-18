# 🧠 Basics of Python: Hello World & Input/Output

This folder contains the **first five Python programs** every beginner must understand before diving into complex logic. These form the backbone of all future AI, ML, or automation code you'll write.

---

## 📌 Programs in This Folder

### 1. `1_hello_world.py`

```python
print("Hello, World!")
```

✅ **What it does:**  
Prints the message to the screen.

🔍 **What happens behind the scenes:**
- Python code (`.py`) is converted into **bytecode (.pyc)**.
- Stored in a folder named `__pycache__`.
- Python Virtual Machine (PVM) reads this bytecode and executes it.
- Think of it like:  
  **Source Code → Bytecode → PVM → Machine Code → Output**

💡 **Why important for AI?**  
All your future models, predictions, and APIs will print logs, messages, and errors — so mastering `print()` is essential.

---

### 2. `2_user_input_string.py`

```python
name = input("Enter your name: ")
print("Hello", name)
```

✅ **What it does:**  
Takes a name as input from the user and prints a greeting.

📌 **How it works:**
- `input()` pauses the program and waits for user input.
- The result is always returned as a **string** (even if you type a number).

---

### 3. `3_user_input_integer.py`

```python
age = int(input("Enter your age: "))
print("You will be", age + 1, "next year.")
```

✅ **What it does:**  
Takes an integer from the user, adds 1, and prints the result.

💡 **Why use `int()`?**  
Because `input()` returns text by default, converting it is important for mathematical operations.

---

### 4. `4_multiple_inputs.py`

```python
name, age = input("Enter name and age separated by space: ").split()
print("Name:", name)
print("Age:", age)
```

✅ **What it does:**  
Takes two values in a single line and splits them.

⚙️ **How it works:**
- `.split()` splits the string by default on **spaces**.
- It returns a list — the values are unpacked into `name` and `age`.

---

### 5. `5_type_conversion.py`

```python
a = int("10")
b = float("5.5")
c = str(100)
print(type(c))  # Output: <class 'str'>

print(a + b)   # 15.5
print("Age is " + c)  # Age is 100
```

✅ **What it does:**  
Shows how to convert data types between `str`, `int`, `float`.

🧠 **Why important in ML?**  
In real data, you get everything as a string (from CSV files, APIs, etc). You must convert them to numeric types before training models.

---
### 6. `6_formatted_string.py`

Covers:
- Traditional string printing using commas
- Newer and cleaner method using **f-strings**

Example:
```python
name = "Nirav"
age = 25
print(f"Hello {name}, you are {age} years old.")
```

✅ **What it does:**
- f-strings are widely used in AI dashboards, logs, and APIs
- Cleaner syntax, supports inline expressions ({age + 1})
- Used in Jupyter, Streamlit, FastAPI, etc.


## 🎯 Real-World AI/ML Relevance

- ✅ Input/output is needed in every ML model — especially for training and inference.
- ✅ Type conversion is common when reading real-world datasets.
- ✅ Console print is your first debugging tool before using loggers.

---

## 🧠 Quick Interview Questions (Beginner Level)

1. What is the difference between `input()` and `print()` in Python?
2. Why does `input()` return a string even if I enter a number?
3. What is `__pycache__` and why does Python create `.pyc` files?

---

## ✅ Tip

> Use `type()` to quickly debug variable types when writing ML or data processing code.

```python
print(type(age))  # Output: <class 'int'>
```

---

📁 **Next Topic:** [2_variables_and_constants →](../02 variables and constants/)