# 📊 Exploratory Data Analysis (EDA)

This folder covers **Exploratory Data Analysis** — the essential step in any machine learning project where we analyze, visualize, and understand the dataset before building a model.

> "You can’t clean or model what you don’t understand." – Every ML Engineer

---

## 📦 Programs in This Folder

### ✅ `1_view_data.py`
- Load dataset using Pandas
- View `.head()`, `.tail()`, `.shape`, `.info()`

### ✅ `2_summary_statistics.py`
- Get mean, median, std, correlation
- Use `.describe()` and `.corr()`

### ✅ `3_value_counts_and_uniques.py`
- Use `.value_counts()` and `.unique()` for category analysis

### ✅ `4_missing_values_check.py`
- Check missing values using `.isnull()`
- Visualize gaps using Seaborn heatmap

### ✅ `5_eda_visualizations.py`
- Histograms, Boxplots, Scatter plots, Heatmaps
- Use Matplotlib + Seaborn

### ✅ `6_target_variable_exploration.py`
- Explore how target (like `tip`) relates to features
- Groupby-based aggregations and visualizations

---

## 🧠 Real-World AI/ML Relevance

| EDA Technique | AI/ML Use |
|---------------|-----------|
| `.describe()` | Understand feature ranges & variance |
| `.value_counts()` | Categorical feature distribution |
| Heatmaps | Detect feature correlations |
| Boxplots | Spot outliers in continuous data |
| Groupby | Feature impact on target variable |

---

## 💬 Interview Questions

1. Why is EDA important before model building?
2. How do you find outliers in numeric data?
3. What are some common tools for EDA in Python?
4. What do you look for in a correlation matrix?

---

## ✅ Tip

> Always perform EDA **before and after** data cleaning.  
> Raw EDA tells you what needs fixing, cleaned EDA confirms it's fixed.

---

📁 **Next Folder:** [5_data_cleaning →](../05%20data%20cleaning/)