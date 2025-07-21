# 🧠 Python Sorting: Practical Use Cases

This folder covers **real-world sorting tasks** you’ll perform in AI, ML, and data-heavy applications.  
Unlike algorithm theory, these examples show how to sort real objects like model scores, configs, and experiment logs.

---

## 📌 Programs in This Folder

### 1. `1_sort_dict_by_value.py`

Sorts a dictionary based on its values.

```python
dict(sorted(model_scores.items(), key=lambda x: x[1]))
```

💡 Use it to sort models by accuracy, loss, or confidence.

---

### 2. `2_sort_list_of_tuples.py`

Sorts a list of tuples by index.

```python
sorted(results, key=lambda x: x[1])
```

💡 Used in paired data like (model, score), (feature, weight).

---

### 3. `3_sort_list_of_dicts.py`

Sorts a list of dictionaries by key.

```python
sorted(models, key=lambda x: x["acc"], reverse=True)
```

💡 Very common in experiment tracking or leaderboard generation.

---

### 4. `4_stable_vs_unstable_sort.py`

Demonstrates that Python’s sort is **stable**.

```python
# Equal values preserve input order
```

💡 Useful when secondary order matters (e.g. model versions with same score).

---

### 5. `5_sort_by_multiple_keys.py`

Sorts by multiple fields — like accuracy and then name.

```python
key=lambda x: (-x["acc"], x["name"])
```

💡 Great for breaking ties or custom ranking systems.

---

### 6. `6_real_usecase_model_result_sorting.py`

Realistic example: sort by `accuracy` first, then `f1-score`.

```python
sorted(results, key=lambda x: (-x["accuracy"], -x["f1"]))
```

💡 Used in ML competitions, dashboards, and automated report generation.

---

## 🎯 Real-World Relevance in AI/ML

| Task                  | AI/ML Use Case |
|-----------------------|----------------|
| Dict sort             | Model performance ranking |
| Tuple sort            | Paired feature importance |
| List of dict sort     | Logs, metrics, configs |
| Multi-key sort        | Sort by accuracy, then F1 |
| Stable sort           | Maintain order in tie-breaks |

---

## 🧠 Interview Questions to Practice

1. How do you sort a list of dictionaries by value?
2. What is stable sort? Why is it useful?
3. How do you sort using multiple keys?
4. When should you use `lambda` in sorting?

---

## ✅ Tip

> In AI, sorting isn't just about order — it's about **evaluation**, **ranking**, and **decision-making**.  
> Use sorting to make your models explainable and results digestible.

---

📁 **Next Topic:** [13 recursion advanced and dynamic programming →](../13 recursion advanced and dynamic programming/)