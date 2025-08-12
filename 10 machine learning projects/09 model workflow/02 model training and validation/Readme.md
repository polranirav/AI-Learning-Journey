# 🧠 Model Workflow – Train, Evaluate, Validate ML Models

This folder covers the complete end-to-end machine learning workflow — from dataset splitting to model evaluation and overfitting detection. These are essential steps in any real-world AI pipeline.

---

## 📌 Programs in This Folder

### ✅ `1_train_test_split.py`
```python
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("data.csv")
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
```

🧠 Used For: Preparing unseen test data to verify generalization.

---

### ✅ `2_evaluate_regression.py`
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_true = [3.2, 2.8, 4.0, 5.1]
y_pred = [3.0, 2.9, 4.2, 5.0]

print("MAE:", mean_absolute_error(y_true, y_pred))
print("MSE:", mean_squared_error(y_true, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
print("R² Score:", r2_score(y_true, y_pred))
```

🧠 Used For: Regression model performance comparison.

---

### ✅ `3_evaluate_classification.py`
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 1, 0, 0]

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
```

🧠 Used For: Analyzing model effectiveness across different classification metrics.

---

### ✅ `4_overfitting_underfitting.py`
```python
import matplotlib.pyplot as plt

train_score = [0.45, 0.60, 0.75, 0.88, 0.92]
test_score = [0.43, 0.58, 0.70, 0.65, 0.60]
complexity = [1, 2, 3, 4, 5]

plt.plot(complexity, train_score, label="Train")
plt.plot(complexity, test_score, label="Test")
plt.title("Overfitting vs Underfitting")
plt.xlabel("Model Complexity")
plt.ylabel("Score")
plt.legend()
plt.grid()
plt.show()
```

🧠 Used For: Model diagnostics — early stopping, tuning, regularization.

---

### ✅ `5_cross_validation.py`
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target

model = LogisticRegression(max_iter=1000)
scores = cross_val_score(model, X, y, cv=5)

print("Cross-Validation Scores:", scores)
print("Mean CV Score:", scores.mean())
```

🧠 Used For: Ensuring robustness and preventing data leakage.

---

## 🤖 Real-World AI/ML Use Cases

| Task                    | Real Application                             |
|-------------------------|----------------------------------------------|
| `train_test_split()`    | Separating validation set from training      |
| Regression Metrics      | Predict house prices, revenue, score         |
| Classification Scores   | Fraud detection, spam filtering              |
| Overfitting detection   | Tuning decision trees, neural nets           |
| Cross-validation        | Ensuring model is robust, not lucky on split |

---

## 💬 Interview Questions

1. What is the difference between `train_test_split()` and `cross_val_score()`?
2. Why is R² score used in regression and not classification?
3. What are signs of overfitting?
4. How do you evaluate an imbalanced classification model?

---

## ✅ Tip

> Always use **cross-validation + stratification** for small datasets and imbalanced classes.  
> Overfitting can often be fixed with **early stopping**, **regularization**, or **simplifying the model**.

---

📁 **Next Folder:** [`10 model deployment →`](../10 model deployment/)