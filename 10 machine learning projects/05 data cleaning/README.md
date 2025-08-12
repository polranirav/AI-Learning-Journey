# 🧹 Folder: 5_data_cleaning – Fixing Dirty Data for Reliable ML

This folder focuses on the **real-world task of cleaning raw datasets** — the most time-consuming but critical step before any AI/ML model. Data cleaning ensures that input values are valid, consistent, and ready for preprocessing.

---

## 📌 Programs in This Folder

### ✅ `1_missing_values_check.py`

Checks for null/missing values in dataset and visualizes them.

- `df.isnull().sum()`
- `sns.heatmap(df.isnull())`

---

### ✅ `2_impute_missing_values.py`

Fills missing values using:
- Mean (numerical)
- Mode (categorical)
- Forward/Backward fill

Used in:
- Tabular AI datasets (e.g., healthcare, finance)

---

### ✅ `3_drop_duplicates_and_fix_types.py`

Handles:
- Removing exact duplicates
- Fixing column types (`object` → `int`, `float`)
- Checking dtypes using `df.dtypes`

---

### ✅ `4_categorical_cleanup.py`

Standardizes messy categories like:
- "MALE", "Male", "male" → `"m"`
- "Yes", "yes", "Y" → `"y"`

Used in:
- Preparing for encoding (next step)

---

### ✅ `5_outliers_handling.py`

Removes outliers using:
- Boxplot visualization
- IQR method (`Q1 - 1.5*IQR` and `Q3 + 1.5*IQR`)

Used in:
- Ensuring robust scaling and model fitting

---

### ✅ `6_logic_and_domain_errors.py`

Fixes values that **don’t make logical sense**, like:
- `age = -3`
- `BMI = 400`

Strategy:
- Replace with median
- Drop or cap using domain rules

---

## 🧠 Real-World AI/ML Relevance

| Problem | Solution |
|--------|----------|
| Missing values → model crash | Impute or remove |
| Duplicates → overfitting | Drop duplicates |
| Inconsistent categories | Standardize text |
| Outliers → bias coefficients | Use IQR, Z-score |
| Domain errors | Validate based on rules |

---

## 💬 Interview Questions

1. What’s the difference between missing values and null values?
2. When would you use mean vs median for imputation?
3. How do you detect and remove outliers?
4. Why is data type correction important before ML?

---

## ✅ Tip

> Clean data ≠ perfect data.  
> But if your model learns from **dirty input**, it’ll produce **noisy predictions**. Always clean first, even for GenAI datasets.

---

📁 **Next Folder:** [`6_data_preprocessing →`](../06%20data%20preprocessing/)