# 📊 3. Data Distributions – Shape, Spread, and Z-Scores

This folder explores how your data is distributed — which is **critical before applying ML models**. Understanding histograms, skewness, normal distribution, and z-scores helps you **choose the right preprocessing and model assumptions**.

---

## 📁 Files in This Folder

### `1_histograms.py`

Covers:
- What is a histogram
- How to bin continuous data into frequency groups
- How it differs from bar charts

Used in:
- Visualizing age, prices, word lengths
- Feature distribution before model training

---

### `2_density_curve.py`

Covers:
- Frequency polygon and density curve from histogram
- Interpreting total area = 1 (100% of data)
- Bell curve and normal shape

Used in:
- Probability estimation in ML
- Understanding spread of inputs, like scores or pixel values

---

### `3_skewness_and_normal.py`

Covers:
- Symmetric vs. skewed distributions
- Left-skew (mean < median), right-skew (mean > median)
- When to use median vs. mean

Used in:
- Feature selection
- Choosing appropriate central tendency before training

---

### `4_z_score.py`

Covers:
- Z-score formula: `(x - mean) / std`
- Empirical rule (68-95-99.7)
- Interpreting relative position of a point

Used in:
- Outlier detection
- Feature scaling before applying models like k-NN, SVM

---

## 🧠 Real-World AI/ML Relevance

| Concept                  | ML Use Case |
|--------------------------|-------------|
| Histogram                | Detect skew, outliers, noise in features |
| Density Curve            | Visualize overall data shape |
| Normal Distribution      | Assumed in Linear Regression, Naive Bayes |
| Z-score                  | Identify outliers, normalize features |

---

## 💬 Interview Questions

1. What’s the difference between a histogram and a bar chart?
2. Why does skewness matter in machine learning?
3. How is z-score useful for outlier detection?
4. When should you prefer median over mean?

---

## ✅ Tip

> For skewed distributions, use **median and IQR**. For symmetric distributions, use **mean and standard deviation**.

---

📁 **Next Topic:** [4 relationships in data →](../4_relationships_in_data/)