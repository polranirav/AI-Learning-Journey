# 🧪 Pandas Series – Foundation for ML Vectors

A **Pandas Series** is a one-dimensional labeled array — similar to a column in a DataFrame. It’s used to store model predictions, labels, loss values, and feature vectors in ML workflows.

---

## 📌 Programs in This Folder

### 1. `1_series_creation.py`

Covers:
- Create Series from list, dict
- Add custom index
- Check dtype and index

Used in:
- Confidence scores
- Class predictions
- One-hot label mappings

---

### 2. `2_indexing_access.py`

Covers:
- Access by label: `s["img1"]`
- Access by position: `s.iloc[0]`
- Loop through `.items()`
- Find `.idxmax()` and `.max()`

Used in:
- Finding top prediction
- Iterating over model outputs
- Getting prediction from specific sample

---

### 3. `3_series_apply.py`

Covers:
- Use `.apply()` with `lambda` to:
  - Round values
  - Convert to binary labels
  - Create custom categories

Used in:
- Post-processing predictions
- Thresholding results
- Grading performance

---

## 🧠 Real-World Relevance in AI/ML

| Series Feature | AI/ML Use |
|----------------|-----------|
| Custom Index   | Map scores to IDs (e.g., image1, tweet42) |
| `.apply()`     | Threshold, grade, or normalize outputs |
| `.idxmax()`    | Get predicted label for max score |
| `.items()`     | Iterate results for reporting |

---

## 💬 Interview Questions

1. What’s the difference between Pandas Series and a list?
2. How would you map prediction scores to binary labels?
3. Why is `.iloc[0]` preferred over `s[0]` for position access?

---

## ✅ Tip

> Pandas Series is like a **NumPy array + label engine**.  
> Always prefer `.iloc` or `.loc` to avoid future warnings or bugs.

---

📁 **Next Topic:** [02 pandas dataframe →](../02 pandas dataframe/)