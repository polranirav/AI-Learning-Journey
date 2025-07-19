# 🧠 Python: Generators and Iterators

This folder teaches how to **generate values on the fly** using `yield`, `next()`, and custom iterator classes.  
Generators are perfect for large datasets, data pipelines, and memory-efficient AI tasks.

---

## 📌 Programs in This Folder

### 1. `1_generator_function_basic.py`

Covers:
- Writing a function that yields values using `yield`

Example:
```python
def gen(): yield 1
```

💡 Generator functions return an iterator — useful for batch processing in ML.

---

### 2. `2_using_next_on_generator.py`

Covers:
- Use `next()` manually to get values from a generator

Example:
```python
gen = count_up()
next(gen)
```

💡 Helps control flow in custom loops or AI data streaming.

---

### 3. `3_custom_iterator_class.py`

Covers:
- Create your own iterator with `__iter__()` and `__next__()`

Example:
```python
class Countdown: def __next__()...
```

💡 Used in building custom PyTorch DataLoaders or config-driven iterables.

---

### 4. `4_infinite_generator_example.py`

Covers:
- Infinite loop using generator (`while True` + `yield`)

Example:
```python
while True: yield 1
```

💡 Great for test data streams or real-time data feeds in inference.

---

### 5. `5_generator_expression_demo.py`

Covers:
- Generator expressions (like list comps but lazy)

Example:
```python
(x * x for x in range(5))
```

💡 Helps reduce memory load for streaming datasets.

---

### 6. `6_compare_list_vs_generator.py`

Covers:
- Compare memory usage of list vs generator

Example:
```python
sys.getsizeof(list vs generator)
```

💡 Proves that generators are lighter — better for large ML pipelines.

---

## 🎯 Real-World Relevance in AI/ML

| Concept      | Use Case |
|--------------|----------|
| Generator    | Load large dataset in batches (no full memory load) |
| `next()`     | Pull model predictions one at a time |
| Custom Iter  | Build reusable data iterators (e.g., `DataLoader`) |
| Generator Expr | Real-time token processing in NLP |
| Infinite Gen | Feed time-series or live inference loops |

---

## 🧠 Interview Questions to Practice

1. What is the difference between a generator and a list?
2. How does `yield` differ from `return`?
3. How do you manually get values from an iterator?
4. Why use generators in AI pipelines?

---

## ✅ Tip

> Generators make your AI code **faster and memory-efficient** — ideal for streaming, batch feeding, lazy computations, and real-time pipelines.

---

📁 **Next Topic:** [18 math and statistics basics →](../18 math and statistics basics/)