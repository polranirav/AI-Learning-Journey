"""
🎯 GOAL:
Visualize underfitting, good fit, and overfitting using polynomial regression.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 1. Generate sample data
np.random.seed(42)
X = np.sort(np.random.rand(50, 1) * 6 - 3, axis=0)  # Range: -3 to 3
y = X**3 - X**2 + 0.5 * X + np.random.randn(50, 1) * 2  # Add noise

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Define degrees for comparison (1 = underfit, 3 = good, 10 = overfit)
degrees = [1, 3, 10]
colors = ["blue", "green", "red"]

plt.figure(figsize=(15, 4))

for i, degree in enumerate(degrees):
    # Create polynomial features
    poly = PolynomialFeatures(degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    # Train model
    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    # Predict on test
    y_pred = model.predict(X_test_poly)

    # Plot
    plt.subplot(1, 3, i + 1)
    X_plot = np.linspace(-3, 3, 100).reshape(-1, 1)
    X_plot_poly = poly.transform(X_plot)
    y_plot = model.predict(X_plot_poly)

    plt.scatter(X_train, y_train, color='gray', alpha=0.6, label="Train Data")
    plt.plot(X_plot, y_plot, color=colors[i], label=f"Degree {degree}")
    plt.title(f"Degree {degree} | MSE: {mean_squared_error(y_test, y_pred):.2f}")
    plt.legend()

plt.suptitle("Underfitting vs Good Fit vs Overfitting", fontsize=16)
plt.tight_layout()
plt.show()