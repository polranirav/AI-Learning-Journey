# 🧠 Data Structures: Stack and Queue

This folder covers two of the most fundamental linear data structures — **Stack (LIFO)** and **Queue (FIFO)** — used widely in AI pipelines, recursion, graph traversal, and streaming operations.

Python makes implementation easy using both `list` and `collections.deque`.

---

## 📌 Programs in This Folder

### 1. `1_stack_using_list.py`

Implements a simple LIFO Stack using Python list.

```python
stack = []
stack.append("model")
stack.append("train")
print(stack)      # ['model', 'train']
print(stack.pop())  # train
```

---

### 2. `2_queue_using_list.py`

Implements a FIFO Queue using list.

```python
queue = []
queue.append("job1")
queue.append("job2")
print(queue.pop(0))  # job1
```

⚠️ Not memory-efficient — use `deque` for large-scale queues.

---

### 3. `3_stack_using_deque.py`

Uses `collections.deque` for faster pop/push operations.

```python
from collections import deque
stack = deque()
stack.append("AI")
print(stack.pop())  # AI
```

---

### 4. `4_queue_using_deque.py`

More efficient queue implementation with `popleft()`.

```python
queue = deque()
queue.append("token")
print(queue.popleft())  # token
```

---

### 5. `5_bfs_queue_usecase.py`

Applies a Queue in real BFS graph traversal.

```python
q = deque([start])
while q:
    node = q.popleft()
    # process node
```

💡 Used in graph search, RAG, pathfinding.

---

### 6. `6_stack_expression_parser.py`

Parses brackets using a stack — common interview pattern.

```python
stack = []
for ch in expr:
    if ch == "(":
        stack.append(ch)
    elif ch == ")" and stack:
        stack.pop()
```

---

### 7. `7_queue_sliding_window_usecase.py`

Uses a queue as a fixed-size sliding window.

```python
window = deque(maxlen=3)
window.append(data_point)
```

💡 Used in signal processing, time series, sensor data, live dashboards.

---

## 🎯 Real-World Relevance in AI/ML

| Concept      | Use Case |
|--------------|----------|
| Stack        | Backtracking, recursive calls, undo systems |
| Queue        | BFS, job scheduling, inference pipelines |
| Deque        | Efficient structure for both directions |
| Sliding window | Rolling average, batch windows in signal data |
| Expression parsing | Syntax trees, bracket balancing in token analysis |

---

## 🧠 Interview Questions to Practice

1. What is the difference between Stack and Queue?
2. Why use `deque` over list for large data?
3. How does BFS use a queue?
4. How would you check for balanced parentheses?

---

## ✅ Tip

> Use `deque` for **performance**, and remember:  
> **Stack = LIFO** (last in, first out)  
> **Queue = FIFO** (first in, first out)

---

📁 **Next Topic:** [5 recursion →](../05%20recursion/)