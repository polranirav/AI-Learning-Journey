"""
Tree-based Model (e.g., DecisionTree)
Splits data into rules for prediction
Used for both classification and regression
"""

from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Feature: [age, income]
X = np.array([[25, 30000], [45, 60000], [35, 45000], [23, 28000]])
y = np.array([0, 1, 1, 0])  # 0 = Not Buy, 1 = Buy

# Create decision tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Make prediction
prediction = model.predict([[30, 50000]])
print("Prediction for [30, 50000]:", prediction[0])