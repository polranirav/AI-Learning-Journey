# 🔍 Algorithms: Searching Techniques

This folder covers the most essential **searching algorithms** used to find values in data structures.  
Efficient search is critical in AI/ML pipelines for:

- Token/label lookup
- Dataset filtering
- Config search
- Fast response time in deployed models

---

## 📌 Programs in This Folder

### 1. `1_linear_search.py`

Searches each element one-by-one.

```python
for i in range(len(arr)):
    if arr[i] == target:
        return i
```

🧠 Used when data is unsorted or very small.

---

### 2. `2_binary_search_recursive_iterative.py`

Searches a **sorted list** in `O(log n)` time.

```python
mid = (low + high) // 2
if target < arr[mid]:
    high = mid - 1
```

💡 Recursion or iteration — both are useful in search-heavy apps (e.g. document retrieval, ID lookup).

---

### 3. `3_search_in_2d_matrix.py`

Searches a **2D grid** sorted row-wise and column-wise.

```python
Start at top-right → move left or down
```

📌 Used in image processing, confusion matrix, NLP attention maps.

---

### 4. `4_find_duplicate_elements.py`

Uses `set()` to detect duplicates in a list.

```python
if val in seen: duplicates.add(val)
```

💡 Common in data cleaning — e.g., check for duplicate samples or labels.

---

### 5. `5_search_performance_comparison.py`

Compares:
- List → O(n)
- Set → O(1)
- Dict → O(1)

```python
timer(lambda: target in big_list, "List search")
```

🧠 Useful for performance decisions when optimizing model input pipelines.

---

### 6. `6_search_real_usecase_token_lookup.py`

Maps tokens to IDs using `dict`.

```python
indexed = [token_to_index[token] for token in sentence]
```

💡 Used in:
- Tokenizers (BERT/GPT)
- Label encoding
- Config management

---

## 🎯 Real-World Relevance in AI/ML

| Search Concept      | AI/ML Use Case |
|---------------------|----------------|
| Linear Search       | Fallback lookup, config scanning |
| Binary Search       | Sorted predictions, log-scaled model ID search |
| 2D Matrix Search    | Attention matrices, pixel search |
| Set Search          | Fast label/token filtering |
| Dict Search         | ID-to-label, token-to-index mappings |
| Duplicate detection | Data cleaning, validation |

---

## 🧠 Interview Questions to Practice

1. When would you use linear vs binary search?
2. How does Python `in` behave for set vs list?
3. Why is dictionary lookup so fast?
4. How would you detect duplicates efficiently?

---

## ✅ Tip

> Always choose `set` or `dict` for frequent searches —  
> they’re optimized for speed with **hash tables (O(1))**, not loops.

---

📁 **Next Topic:** [12 sorting practical →](../12 sorting practical/)