# 🧠 Algorithms: Time Complexity & Big O

This folder covers the most important concept in algorithm efficiency — **Big O Notation**.  
It helps you understand **how fast your code runs** as input size grows.  
In AI/ML, this is crucial for:
- Large dataset preprocessing
- Model inference optimization
- Choosing the right data structures

---

## 📌 Programs in This Folder

### 1. `1_intro_big_o_notation.py`

Introduces O(1), O(n), and O(n²).

```python
def constant_example(arr): return arr[0]       # O(1)
def linear_example(arr): for i in arr: print(i)  # O(n)
def quadratic_example(arr): nested loops        # O(n²)
```

---

### 2. `2_time_complexity_examples.py`

Demos of key time complexities:

```python
print(arr[0])          # O(1)
binary search step     # O(log n)
for i in arr           # O(n)
nested for loops       # O(n²)
```

---

### 3. `3_data_structure_complexity.py`

Shows complexity of list, dict, and set.

| Operation       | List     | Dict     | Set      |
|----------------|----------|----------|----------|
| Lookup         | O(n)     | O(1)     | O(1)     |
| Insertion      | O(1)     | O(1)     | O(1)     |
| Search         | O(n)     | O(1)     | O(1)     |

💡 Use `dict` or `set` for fast lookups (token IDs, labels, configs)

---

### 4. `4_recursive_vs_iterative_complexity.py`

Factorial by recursion vs loop.

```python
def factorial_recursive(n): return n * f(n-1)  # O(n)
def factorial_iterative(n): loop from 2 to n   # O(n)
```

💡 Loop is usually faster and safer (avoids stack overflow)

---

### 5. `5_real_ai_pipeline_tradeoff.py`

Naive loop vs list comprehension.

```python
[x ** 2 for x in data]     # Faster, same O(n)
```

💡 Always optimize loops for preprocessing large datasets.

---

### 6. `6_visual_call_count_with_counter.py`

Tracks function call count in recursion.

```python
def call_me(n): call_me(n-1)   # O(n) → 10 calls = 10 stack frames
```

💡 Helps visualize what “grows linearly” or exponentially in memory.

---

## 🎯 Real-World Relevance in AI/ML

| Concept             | AI/ML Use Case |
|---------------------|----------------|
| O(n²) nested loops  | Avoid in feature selection or scoring |
| O(1) dictionary     | Used in label mapping, fast lookup |
| O(log n) search     | Binary search on sorted features |
| List vs Set vs Dict | Pick based on speed needs in pipeline |
| Iteration tradeoffs | Preprocessing speed before model training |

---

## 🧠 Interview Questions to Practice

1. What is Big O notation?
2. What is the time complexity of searching in a Python list vs dict?
3. Why is O(log n) faster than O(n)?
4. What happens to recursion if you don’t define a base case?

---

## ✅ Tip

> Don’t memorize Big O — **understand the shape of growth**:  
> O(1) → constant  
> O(n) → grows with data  
> O(n²) → avoid in large datasets  
> O(log n) → ideal in search

---

📁 **Next Topic:** [9 object oriented programming →](../9%20trees/)