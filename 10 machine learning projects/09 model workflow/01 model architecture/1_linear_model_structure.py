"""
Basic Linear Model Architecture
y = mx + b — straight-line logic
Used for regression tasks (continuous prediction)
"""

from sklearn.linear_model import LinearRegression
import numpy as np

# Sample feature (X) and label (y)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([100, 150, 200, 250, 300])

# Define the linear regression model
model = LinearRegression()

# Train (fit) the model
model.fit(X, y)

# Coefficients (m = slope, b = intercept)
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

# Predict
pred = model.predict([[6]])
print("Prediction for X=6:", pred[0])