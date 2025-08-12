# 🧹 Folder 6: Data Preprocessing – Clean Input for Better ML Models

This folder covers essential data preprocessing techniques to **prepare your data for machine learning models**. You’ll explore how to scale values, encode categories, transform skewed data, and use pipelines — all beginner-friendly and 100% relevant to AI/ML.

---

## 📌 Programs in This Folder

### 1. `1_encoding_label_vs_onehot.py`

Covers:
- Difference between Label Encoding and One-Hot Encoding
- When to use each
- `LabelEncoder` vs `OneHotEncoder` from Scikit-learn

Used in:
- Converting text features into numeric before model training

---

### 2. `2_onehot_dataframe.py`

Covers:
- How to apply `pd.get_dummies()` to create dummy variables from categorical columns

Used in:
- Preparing categorical features without needing Scikit-learn

---

### 3. `3_feature_scaling_minmax.py`

Covers:
- Min-Max Scaling (Normalization)
- Brings values between 0 and 1

Used in:
- Algorithms like KNN, Logistic Regression, Neural Nets

---

### 4. `4_feature_scaling_standard.py`

Covers:
- Standardization with mean = 0, std = 1 using `StandardScaler`

Used in:
- ML models sensitive to data distribution (SVM, Logistic Regression)

---

### 5. `5_log_transformation.py`

Covers:
- Log transformation using `np.log1p()`
- Reduces right-skewed distributions

Used in:
- Handling skewed features like price, income, etc.

---

### 6. `6_pipeline_intro.py`

Covers:
- Creating a pipeline with scaler + model
- Simplifies training and inference process

Used in:
- Building clean production-level model pipelines

---

### 7. `7_pipeline_scaling_encoding.py`

Covers:
- Combining encoding and scaling in a single `ColumnTransformer`
- Full-feature ML pipeline

Used in:
- Real-world ML projects with mixed data types

---

## 🧠 AI/ML Relevance

| Technique        | AI/ML Use Case |
|------------------|----------------|
| Label Encoding   | Tree models, ordinal features |
| One-Hot Encoding | Linear models, categorical input |
| MinMax Scaling   | KNN, ANN, logistic regression |
| StandardScaler   | SVM, PCA, regression models |
| Log Transform    | Right-skewed feature fix |
| Pipelines        | Reusable, production-ready preprocessing |

---

## 💬 Interview Prep

1. What’s the difference between standardization and normalization?
2. Why is encoding important in ML?
3. How do you handle skewed features?
4. What’s the role of `Pipeline` in Scikit-learn?

---

## ✅ Tip

> Clean data is 80% of the ML project.  
> Build your preprocessing steps into **pipelines** for reproducibility and maintainability.

---

📁 **Next Folder:** [`7 feature engineering →`](../07%20feature%20engineering/)