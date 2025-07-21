# 🧠 Algorithms: Sorting Techniques

This folder covers all essential **sorting algorithms** — both classic and Pythonic.  
Sorting is fundamental in AI/ML for:
- Ranking models
- Sorting accuracy/loss values
- Arranging predictions
- Cleaning and organizing feature sets

---

## 📌 Programs in This Folder

### 1. `1_bubble_sort.py`

Step-by-step comparison and swap.

```python
for j in range(n - 1 - i):
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

💡 Easy to visualize, but not efficient for large data.

---

### 2. `2_selection_sort.py`

Pick the smallest item and place it in the sorted area.

```python
min_idx = i
if arr[j] < arr[min_idx]:
    min_idx = j
```

💡 Builds logic for greedy algorithms — helpful in understanding optimization flow.

---

### 3. `3_insertion_sort.py`

Insert elements one-by-one in correct position.

```python
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
```

💡 Good when working with streaming sorted data (e.g., real-time ranking).

---

### 4. `4_merge_sort.py`

Divide and conquer, then merge in order.

```python
left = merge_sort(arr[:mid])
right = merge_sort(arr[mid:])
return merge(left, right)
```

💡 Stable sort used behind the scenes in many libraries (like Pandas).

---

### 5. `5_quick_sort.py`

Use a pivot to recursively sort sublists.

```python
pivot = arr[0]
left = [x for x in arr[1:] if x < pivot]
```

💡 Preferred for fast sorting in large datasets. Core idea behind many ranking engines.

---

### 6. `6_python_builtin_sort.py`

Use Python’s built-in `sorted()` and `.sort()` methods.

```python
sorted(arr)  # returns new list
arr.sort()   # modifies original
```

💡 Use this in real-world ML for preprocessing, feature ranking, etc.

---

### 7. `7_sorting_by_custom_key.py`

Sort list of dicts using a custom field.

```python
sorted(models, key=lambda x: x["accuracy"], reverse=True)
```

💡 Critical for sorting results by metrics: accuracy, loss, confidence scores, etc.

---

## 🎯 Real-World Relevance in AI/ML

| Sorting Method       | AI/ML Use Case |
|----------------------|----------------|
| Bubble/Selection     | Conceptual foundation |
| Merge/Quick Sort     | Efficient dataset sorting |
| Python `sorted()`    | Model results, feature lists |
| Custom key sorting   | Rank models by accuracy or loss |
| Stable sort          | Maintain order in tie cases (merge sort) |

---

## 🧠 Interview Questions to Practice

1. What’s the difference between bubble and insertion sort?
2. Why is quick sort faster than merge in most cases?
3. What’s the advantage of Python’s built-in `sorted()` over custom sort?
4. How do you sort a list of dictionaries by a nested key?

---

## ✅ Tip

> In real AI projects, use `sorted()` or NumPy/Pandas sort.  
> But mastering these algorithms gives you **control, intuition, and optimization logic**.

---

📁 **Next Topic:** [8 time complexity and Big O →](../08%20time%20complexity%20and%20Big%20O/)