# 🧠 Python: Multithreading and Multiprocessing

This folder covers how to run code in **parallel** using threads and processes — essential when building performance-efficient AI/ML apps, handling data processing, scraping, or running background tasks.

---

## 📌 Programs in This Folder

### 1. `1_threading_basic.py`

Covers:
- Running code in a separate thread

Example:
```python
threading.Thread(target=func).start()
```

💡 Use for I/O-bound tasks (API calls, file reads).

---

### 2. `2_multiprocessing_basic.py`

Covers:
- Running code in a separate process

Example:
```python
multiprocessing.Process(target=func).start()
```

💡 Best for CPU-bound tasks like heavy calculations.

---

### 3. `3_thread_vs_process_demo.py`

Covers:
- Compare thread vs process execution time

💡 Helps decide which to use depending on task type (I/O vs CPU).

---

### 4. `4_io_bound_thread_example.py`

Covers:
- Simulating multiple fake downloads using threads

💡 Threads shine in tasks with lots of wait time (e.g., network latency).

---

### 5. `5_cpu_bound_process_example.py`

Covers:
- Heavy math task across multiple processes

💡 Great for speeding up data processing, image transformations, etc.

---

### 6. `6_thread_with_args.py`

Covers:
- Passing arguments to a thread

Example:
```python
Thread(target=func, args=(val,))
```

---

### 7. `7_threading_with_current_thread.py`

Covers:
- Getting the name of the currently running thread

Example:
```python
threading.current_thread().name
```

💡 Useful for debugging or thread tracking.

---

### 8. `8_process_pool_executor_demo.py`

Covers:
- Running tasks with a pool of processes

Example:
```python
with ProcessPoolExecutor() as executor:
    results = executor.map(func, data)
```

💡 Cleaner syntax for parallel task distribution.

---

## 🎯 Real-World Relevance in AI/ML

| Concept           | Use Case Example |
|------------------|------------------|
| Threading         | Parallel logging, async monitoring |
| Multiprocessing   | Speed up image/data transformations |
| Executor Pool     | Parallel batch scoring |
| Args in Threads   | Process named datasets, logs, or configs |
| I/O vs CPU Choice | Decides architecture of your pipeline |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between threading and multiprocessing?
2. When should you use `join()`?
3. Why does Python need multiprocessing for CPU-bound tasks?
4. What does `ProcessPoolExecutor` simplify?

---

## ✅ Tip

> Use **threading for I/O-heavy tasks** (downloads, logs, API calls).  
> Use **multiprocessing for CPU-heavy tasks** (math, data crunching, model scoring).

---

📁 **Next Topic:** [16 decorators →](../16 decorators/)