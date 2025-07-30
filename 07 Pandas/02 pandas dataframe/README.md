# 📊 Pandas DataFrame – ML Table Structure

This folder introduces **Pandas DataFrames**, which represent structured datasets in Python. Think of them as **Excel sheets for ML pipelines** — used for storing and manipulating features, labels, metrics, predictions, and more.

---

## 📌 Programs in This Folder

### 1. `1_df_creation.py`

Covers:
- Create DataFrame from dict or list of dicts
- Understand `.shape` and `.columns`

Used in:
- Reading tabular data
- Structuring datasets for ML models
- Wrapping predictions from model inference

---

### 2. `2_df_selection.py`

Covers:
- Select column(s), row(s)
- Use `.iloc[]`, `.loc[]` for specific cells
- Slice subsets by range or label

Used in:
- Selecting features and target
- Accessing test samples or predictions
- Comparing actual vs predicted values

---

### 3. `3_df_editing.py`

Covers:
- Add column using logic (`.apply`)
- Update cell values
- Add a new row
- Drop unnecessary columns

Used in:
- Post-processing model predictions
- Label corrections and data cleanup
- Creating derived features

---

## 🧠 AI/ML Relevance

| DataFrame Task | AI Workflow Use |
|----------------|-----------------|
| Create from dicts | Wrap training/testing batches |
| Slice columns/rows | Select features or results |
| Add new column | Generate predictions, encode labels |
| Drop column | Remove ID or metadata before training |

---

## 💬 Interview Questions

1. How is a DataFrame different from a Series?
2. When would you use `.loc[]` vs `.iloc[]`?
3. How can you filter rows where prediction is incorrect?

---

## ✅ Tip

> Use `.apply()` + `lambda` to create powerful features and labels in one line — it’s a favorite ML trick in Pandas!

---

📁 **Next Topic:** [03 pandas filtering and grouping →](../03 pandas filtering and grouping/)