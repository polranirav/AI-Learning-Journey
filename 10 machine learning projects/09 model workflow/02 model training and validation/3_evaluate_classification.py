"""
🎯 GOAL:
Evaluate a classification model using Accuracy, Precision, Recall, and F1-score.
"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Load sample classification dataset
data = load_iris()
X = data.data
y = data.target

# 2. Binary classification only (0 vs 1)
X = X[y != 2]
y = y[y != 2]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Predictions
y_pred = model.predict(X_test)

# 6. Evaluation
print("🔍 Accuracy:", accuracy_score(y_test, y_pred))
print("🎯 Precision:", precision_score(y_test, y_pred))
print("🚨 Recall:", recall_score(y_test, y_pred))
print("🧮 F1 Score:", f1_score(y_test, y_pred))