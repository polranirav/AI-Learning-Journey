"""
🎯 GOAL:
Use K-Fold Cross-Validation to evaluate model stability.
"""

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np

# 1. Load dataset
data = load_diabetes()
X = data.data
y = data.target

# 2. Initialize model
model = LinearRegression()

# 3. Perform 5-fold cross-validation with R² as metric
scores = cross_val_score(model, X, y, cv=5, scoring="r2")

# 4. Show scores and average
print("R² scores per fold:", scores)
print("Average R²:", np.mean(scores))