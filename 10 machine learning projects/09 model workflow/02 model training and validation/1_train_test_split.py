"""
🎯 GOAL:
Split the dataset into training and testing sets, and train a regression model.

This is the first step in any ML model building workflow.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# 1. Generate a synthetic regression dataset
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# 2. Convert to pandas DataFrame for better readability
df = pd.DataFrame(X, columns=["feature"])
df["target"] = y

# 3. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df[["feature"]],
    df["target"],
    test_size=0.2,
    random_state=42
)

print(f"Training size: {len(X_train)}, Testing size: {len(X_test)}")

# 4. Train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate on test set
r2 = model.score(X_test, y_test)
print(f"R² Score on test set: {r2:.2f}")

# 6. Visualize
plt.scatter(X_test, y_test, label="True values")
plt.plot(X_test, model.predict(X_test), color="red", label="Prediction")
plt.title("Test Set vs Prediction")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.grid(True)
plt.show()