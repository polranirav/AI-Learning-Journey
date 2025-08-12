# 🧠 Supervised Learning – Learn from labeled data (inputs + known outputs)

from sklearn.linear_model import LinearRegression
import numpy as np

# Experience vs Salary data (input → output)
X = np.array([[1], [2], [3], [4], [5]])  # Input: years of experience
y = np.array([30000, 35000, 40000, 45000, 50000])  # Output: salary

model = LinearRegression()
model.fit(X, y)

# Predict salary for 6 years of experience
predicted_salary = model.predict([[7]])
print(f"📊 Predicted salary for 7 years: ${predicted_salary[0]:.2f}")