import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "age": [25, 32, 47, 51, 62, 22, 38, 45],
    "income": [50000, 60000, 80000, 82000, 90000, 42000, 62000, 72000],
    "experience": [2, 5, 15, 20, 25, 1, 10, 12],
    "spending_score": [65, 70, 80, 85, 90, 60, 75, 78]
}
df = pd.DataFrame(data)

# Features and target
X = df.drop("spending_score", axis=1)
y = df["spending_score"]

# Train Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Get feature importances
importances = model.feature_importances_
feature_names = X.columns

# Print importances
print("🌳 Feature Importances from Random Forest:")
for name, score in zip(feature_names, importances):
    print(f"{name}: {score:.3f}")

# Plot
plt.figure(figsize=(6, 4))
plt.bar(feature_names, importances, color="skyblue")
plt.title("Feature Importance (Random Forest)")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.show()