# 📈 4. Relationships in Data – Correlation, Covariance & Scatter Plots

This folder explores how variables are **related** — a core concept in AI/ML that helps determine if features influence each other. These statistical techniques help detect **linear relationships, multicollinearity**, or whether features are useful at all.

---

## 📁 Files in This Folder

### `1_covariance.py`

Covers:
- Definition of covariance
- Positive vs. negative vs. zero covariance
- How to compute manually with mean-centered values

Used in:
- Understanding feature-to-feature influence
- Preprocessing checks for data dependencies

---

### `2_correlation.py`

Covers:
- Pearson correlation formula: `cov(X, Y) / (std(X) * std(Y))`
- Interpretation between -1 and 1
- Strong vs. weak correlation

Used in:
- Feature selection
- Detecting multicollinearity
- Reducing redundancy in datasets

---

### `3_scatter_plot_visualization.py`

Covers:
- Visual representation of variable pairs
- Identifying linear vs. non-linear relationships
- Plotting labeled classes with visual separation

Used in:
- EDA before supervised learning
- Pattern detection in unsupervised data

---

## 🧠 Real-World AI/ML Relevance

| Concept      | Usage in AI/ML |
|--------------|----------------|
| Covariance   | Raw indicator of direction between features |
| Correlation  | Feature strength analysis for selection |
| Scatter Plot | Visual feature pairing & separability insights |

---

## 💬 Interview Questions

1. What does a correlation value of 0.95 indicate?
2. How do covariance and correlation differ?
3. Why do we remove highly correlated features before training?
4. What do scatter plots reveal in ML?

---

## ✅ Tip

> A high correlation between input features may confuse ML models — use **PCA** or drop one of the variables if correlation > 0.9.

---

📁 **Next Topic:** [5 probability and hypothesis →](../5_probability_and_hypothesis/)