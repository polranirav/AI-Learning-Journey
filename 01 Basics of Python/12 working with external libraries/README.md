# 🧠 Python: Working with External Libraries

This folder shows how to use popular Python libraries that are commonly used in **AI, data science, and automation**. These tools help with math, data processing, visualization, API calls, and much more.

---

## 📌 Programs in This Folder

### 1. `1_import_math_random.py`

Covers:
- Built-in libraries: `math`, `random`

Example:
```python
math.sqrt(16), random.randint(1, 10)
```

💡 Used for quick math calculations and random selections.

---

### 2. `2_working_with_os_datetime.py`

Covers:
- File system access (`os`)
- Date/time formatting (`datetime`)

Example:
```python
os.getcwd(), datetime.datetime.now()
```

💡 Useful for automation scripts and timestamped logs.

---

### 3. `3_numpy_array_operations.py`

Covers:
- Creating and operating on NumPy arrays

Example:
```python
np.array([1, 2, 3]), np.mean(arr)
```

💡 NumPy is used heavily for numerical operations in ML.

---

### 4. `4_pandas_dataframe_basics.py`

Covers:
- Creating and filtering DataFrames

Example:
```python
pd.DataFrame(data), df[df["age"] > 23]
```

💡 Core tool for tabular data handling in ML.

---

### 5. `5_pandas_series_groupby.py`

Covers:
- Grouping and summarizing data

Example:
```python
df.groupby("department")["score"].mean()
```

💡 Grouping is key in data analysis tasks like feature engineering.

---

### 6. `6_matplotlib_basic_plot.py`

Covers:
- Simple line plot with `matplotlib`

Example:
```python
plt.plot(x, y), plt.show()
```

💡 Great for training loss curves, accuracy plots, etc.

---

### 7. `7_seaborn_visualizations.py`

Covers:
- Visualizing data with `seaborn`

Example:
```python
sns.scatterplot(...), sns.heatmap(...)
```

💡 Used for statistical charts and heatmaps in data exploration.

---

### 8. `8_requests_api_call.py`

Covers:
- Making GET requests using `requests`

Example:
```python
requests.get(url).json()
```

💡 Useful in ML workflows for pulling data from APIs or cloud apps.

---

### 9. `9_library_install_tips.py`

Covers:
- How to install common libraries via `pip`
- Best practices for import names

💡 Good reference when setting up environments for AI projects.

---

## 🎯 Real-World Relevance in AI/ML

| Library      | Use Case Example |
|--------------|------------------|
| `numpy`      | Model inputs, matrix ops |
| `pandas`     | Read, clean, and filter datasets |
| `matplotlib` | Visualize training curves |
| `seaborn`    | Plot correlations, distributions |
| `requests`   | Fetch data from web or API |
| `os` / `datetime` | Handle file paths, timestamps, auto-saving |

---

## 🧠 Interview Questions to Practice

1. What is the difference between `pandas` Series and DataFrame?
2. How do you plot a line graph using matplotlib?
3. When would you use `requests.get()` in a project?
4. Why is NumPy preferred for numerical work over plain Python lists?

---

## ✅ Tip

> In real AI workflows, always use `virtual environments` and `requirements.txt` to manage and reproduce your libraries.

---

📁 **Next Topic:** [13 comprehensions →](../13 comprehensions/)