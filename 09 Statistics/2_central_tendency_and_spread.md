# 📊 2. Central Tendency and Spread

This folder introduces the **core statistical measures** used to understand how your dataset behaves — both in terms of its **center** and its **variability**. These concepts are **crucial for preprocessing**, **outlier removal**, and **standardization** in AI/ML pipelines.

---

## 🗂️ Files in This Folder

### 1. `1_mean_median_mode.py`
- **Covers:** Mean (average), median (middle), and mode (most frequent)
- **Use in AI:** Feature center analysis, missing value imputation, class mode for baseline models

---

### 2. `2_range_and_iqr.py`
- **Covers:** Range calculation and Interquartile Range (IQR) using Q1 and Q3
- **Use in AI:** Detecting outliers, understanding feature spread, preparing box plots

---

### 3. `3_standard_deviation.py`
- **Covers:** Population vs. sample standard deviation, variance
- **Use in AI:** Z-score normalization, statistical significance testing, anomaly detection

---

### 4. `4_outliers_detection.py`
- **Covers:** Outlier detection using IQR and fences (lower/upper bounds)
- **Use in AI:** Data cleaning before training, removing noise from regression/classification tasks

---

### 5. `5_five_number_summary.py`
- **Covers:** Min, Q1, Median (Q2), Q3, Max
- **Use in AI:** Box plot creation, identifying skewness, EDA summarization

---

## 🧠 AI/ML Relevance Table

| Concept               | ML/AI Usage Example                                      |
|-----------------------|-----------------------------------------------------------|
| Mean                  | Normalize features, compute model error (MSE)            |
| Median                | Handle skewed features or outliers                       |
| Mode                  | Impute missing values for categorical variables          |
| Range                 | Basic understanding of data spread                       |
| IQR                   | Robust outlier detection (used in preprocessing)         |
| Std Deviation         | Z-score standardization, feature variance control        |
| Five-number summary   | Box plots, skewness detection, feature summarization     |

---

## 💬 Interview Questions

1. What’s the difference between mean, median, and mode?
2. When would you use IQR instead of standard deviation?
3. How do you detect outliers using IQR method?
4. Why is the median preferred for skewed distributions?
5. What is the five-number summary and how is it used?

---

## ✅ Pro Tip

> If your dataset contains outliers, use **median and IQR** instead of **mean and standard deviation** — they are more robust and won’t be distorted by extreme values.

---

📁 **Next Folder:** [`3_data_distributions`](../3_data_distributions/)