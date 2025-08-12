# 🧠 Feature Selection – Reducing Input Noise in ML

This folder covers techniques to **select the most relevant features** for machine learning models. It helps reduce noise, prevent overfitting, and speed up training — making your model both efficient and interpretable.

---

## 📌 Programs in This Folder

### ✅ `1_filter_correlation.py`
```python
# This script calculates correlation between features
# Highly correlated (multicollinear) features can confuse models

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
```

Used for: Identifying redundant features (remove one of each highly correlated pair)

---

### ✅ `2_chi2_test_categorical.py`
```python
# Apply Chi-Square test for categorical input features vs target

from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("data.csv")
X = df[["region", "gender", "contract_type"]]
y = df["churn"]

X = X.apply(LabelEncoder().fit_transform)
selector = SelectKBest(score_func=chi2, k="all")
selector.fit(X, y)

print("Scores:", selector.scores_)
```

Used for: Categorical variable selection — e.g., customer churn, fraud

---

### ✅ `3_lasso_feature_selection.py`
```python
# Use Lasso Regression to automatically remove weak predictors

from sklearn.linear_model import LassoCV
from sklearn.datasets import load_diabetes
import pandas as pd

data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

model = LassoCV()
model.fit(X, y)

# Show coefficients
print(pd.Series(model.coef_, index=X.columns))
```

Used for: Feature selection in regression models

---

### ✅ `4_tree_feature_importance.py`
```python
# Random Forest to extract and visualize feature importances

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

importances = model.feature_importances_
features = X.columns

plt.barh(features, importances)
plt.title("Feature Importances (Random Forest)")
plt.xlabel("Importance Score")
plt.show()
```

Used for: Explainability and identifying top-performing input variables

---

## 🤖 AI/ML Use Cases

| Method         | Real-World Usage                                  |
|----------------|----------------------------------------------------|
| Correlation    | Remove redundant numeric features (e.g., features with 0.98+ correlation) |
| Chi-Square     | Select best categorical inputs (e.g., user segment, contract type) |
| Lasso          | Shrink unimportant features in regression models |
| Random Forest  | Understand feature importance in classification tasks |

---

## 💬 Interview Questions

1. What is the difference between feature selection and dimensionality reduction?
2. How does Lasso regression perform variable elimination?
3. Why is removing correlated features important in linear models?
4. What is the advantage of tree-based feature importance over correlation?

---

## ✅ Tip

> Always perform feature selection **after EDA but before training**.  
> This helps reduce input noise and improve model interpretability.

---

📁 **Next Folder:** [`9 model workflow →`](../09%20model%20workflow/)