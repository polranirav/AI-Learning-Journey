# 🚫 Handling Missing Values in Pandas – AI Data Cleaning

Missing values (NaN, None) are extremely common in real-world ML datasets. This folder teaches you how to **detect, drop, and fill missing values** using Pandas — a key step in preprocessing pipelines.

---

## 📌 Programs in This Folder

### 1. `1_detect_missing_values.py`

Covers:
- `.isnull()` to detect NaN
- `.sum()` to count missing values per column
- `.any(axis=1)` to detect rows with missing data

Used in:
- Dataset quality checks
- Finding broken labels
- Early EDA for tabular or NLP inputs

---

### 2. `2_drop_missing.py`

Covers:
- `dropna()` to remove rows with missing values
- `axis=1` to remove columns with missing values
- `how="all"` to remove fully empty rows

Used in:
- Cleaning small test sets
- Filtering sparse log files
- Ensuring model doesn’t train on broken inputs

---

### 3. `3_fill_missing.py`

Covers:
- `fillna()` with mean, default value
- Replacing NaN in numerical/categorical columns

Used in:
- Imputing missing values for model input
- Avoiding bias in training data
- Fixing inconsistencies in survey/NLP data

---

## 🧠 Real-World Relevance in AI/ML

| Task                             | Method |
|----------------------------------|--------|
| Detect missing entries           | `df.isnull()` |
| Drop incomplete rows             | `df.dropna()` |
| Fill numerical features          | `fillna(df.mean())` |
| Fill text/category gaps          | `fillna("Unknown")` |

---

## 💬 Interview Questions

1. How do you check for missing values in a dataset?
2. What’s the difference between `dropna()` and `fillna()`?
3. When would you fill missing values instead of dropping them?
4. How do you fill NaNs with column-wise average?

---

## ✅ Tip

> Always check for missing values before training a model. Even one NaN can break your pipeline.

---

📁 **Next Topic:** [06 pandas date/time →](../06 pandas date time/)
