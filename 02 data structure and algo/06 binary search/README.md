# 🧠 Algorithms: Binary Search

This folder covers **binary search**, a powerful and fast algorithm used to search sorted data in `O(log n)` time.  
It is foundational in AI/ML pipelines for:
- Threshold matching
- Prediction ranking
- Label lookups
- Efficient ID access in large sorted datasets

---

## 📌 Programs in This Folder

### 1. `1_binary_search_iterative.py`

Classic loop-based binary search.

```python
def binary_search(arr, target):
    while low <= high:
        mid = (low + high) // 2
        # check left or right
```

💡 Use when you want speed in large sorted arrays.

---

### 2. `2_binary_search_recursive.py`

Same logic but implemented using recursion.

```python
def binary_search_recursive(arr, target, low, high):
    if low > high: return -1
```

💡 Adds recursion practice and stack-tracing for deeper logic.

---

### 3. `3_binary_search_edge_cases.py`

Find first and last occurrence of a repeated value.

```python
# Keep going left or right after match
if arr[mid] == target:
    result = mid
    high = mid - 1  # or low = mid + 1
```

💡 Useful in NLP token frequency, data splits, range finders.

---

### 4. `4_binary_search_custom_objects.py`

Search in a list of tuples based on a value.

```python
students = [("A", 50), ("B", 60)]
# Search by score in sorted tuples
```

💡 Use in AI for accessing sorted config objects, thresholds, or ranked results.

---

### 5. `5_binary_search_with_bisect.py`

Use Python's built-in `bisect` module.

```python
import bisect
pos = bisect.bisect_left(arr, target)
bisect.insort(arr, value)
```

💡 Commonly used in AI pre-processing for inserting into sorted batches.

---

## 🎯 Real-World Relevance in AI/ML

| Concept           | Use Case |
|-------------------|----------|
| Binary search     | Locate values in sorted features |
| Threshold finding | Search ideal cutoff point |
| Range finder      | NLP, token or class frequency |
| Ranked lookup     | Classifier score thresholding |
| Bisect module     | Smart insert into sorted datasets |

---

## 🧠 Interview Questions to Practice

1. What is the time complexity of binary search?
2. How does binary search differ from linear search?
3. How would you find the first/last occurrence of a number in duplicates?
4. When would you use the `bisect` module?

---

## ✅ Tip

> Binary search only works when data is **sorted**.  
> Always verify that first — and remember, it’s one of the fastest search techniques used in large-scale data apps.

---

📁 **Next Topic:** [7 sorting algorithms →](../7 sorting algorithms/)