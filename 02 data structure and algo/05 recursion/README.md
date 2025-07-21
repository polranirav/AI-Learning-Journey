# 🧠 Algorithms: Recursion

This folder introduces **recursion** — a function calling itself until a base condition is met.  
It’s a key concept behind tree traversal, search algorithms, backtracking, and memory-efficient solutions in AI systems.

---

## 📌 Programs in This Folder

### 1. `1_recursive_hello.py`

Simple example to demonstrate recursion flow.

```python
def say_hello(n):
    if n == 0:
        return
    print("Hello", n)
    say_hello(n - 1)
```

---

### 2. `2_factorial_recursive.py`

Calculates factorial recursively.

```python
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)
```

---

### 3. `3_fibonacci_recursive.py`

Classic recursion example for Fibonacci series.

```python
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)
```

⚠️ Not efficient — use memoization in AI apps.

---

### 4. `4_sum_of_list_recursive.py`

Adds numbers in a list using recursion.

```python
def sum_list(nums):
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])
```

---

### 5. `5_reverse_string_recursive.py`

Reverses a string using recursive slicing.

```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
```

---

### 6. `6_binary_search_recursive.py`

Performs binary search recursively.

```python
def binary_search(arr, target, low, high):
    # base + mid logic
    return index or -1
```

💡 Faster search in sorted features, thresholds, etc.

---

### 7. `7_tree_traversal_recursive.py`

Recursive **preorder traversal** of a binary tree.

```python
def preorder(root):
    print(root.value)
    preorder(root.left)
    preorder(root.right)
```

💡 Foundation for decision trees, parsing, RAG, etc.

---

### 8. `8_recursion_vs_iteration.py`

Compare recursion vs loop for summing.

```python
def sum_recursive(n): ...
def sum_iterative(n): ...
```

---

### 9. `9_recursion_call_stack_debug.py`

Visualize recursion entry/exit using print tracing.

```python
def trace(n):
    print("Entering:", n)
    trace(n-1)
    print("Returning from:", n)
```

---

## 🎯 Real-World Relevance in AI/ML

| Concept          | Use Case |
|------------------|----------|
| Recursion        | Tree traversal (decision trees, syntax parsing) |
| Backtracking     | Beam search, game trees |
| Base + call logic| Explainability in prediction chains |
| Binary search    | Search thresholds or sorted feature bins |
| Stack trace      | Useful for debugging recursive agents or loops |

---

## 🧠 Interview Questions to Practice

1. What is recursion? When do you use it?
2. What’s the difference between recursion and iteration?
3. How does recursion affect memory (call stack)?
4. How would you reverse a string or list recursively?

---

## ✅ Tip

> Always define a clear **base case**, then handle the problem in **smaller steps**.  
> Think of recursion as **delegation** to a smaller subproblem.

---

📁 **Next Topic:** [6 binary search →](../06%20binary%20search/)