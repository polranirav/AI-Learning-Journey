"""
Pipeline Architecture
Chains preprocessing + modeling steps in one clean pipeline
Great for production ML systems
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# Input features and binary labels
X = np.array([[1, 100], [2, 150], [3, 130], [4, 170]])
y = np.array([0, 1, 0, 1])

# Pipeline: scale data → apply logistic regression
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

# Train model
model.fit(X, y)

# Predict
print("Prediction:", model.predict([[2.5, 140]]))