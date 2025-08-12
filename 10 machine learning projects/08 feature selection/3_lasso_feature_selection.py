import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split

# Sample dataset
data = {
    "age": [25, 32, 47, 51, 62, 22, 38, 45],
    "income": [50000, 60000, 80000, 82000, 90000, 42000, 62000, 72000],
    "experience": [2, 5, 15, 20, 25, 1, 10, 12],
    "spending_score": [65, 70, 80, 85, 90, 60, 75, 78]
}
df = pd.DataFrame(data)

# Define features and target
X = df.drop("spending_score", axis=1)
y = df["spending_score"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Lasso model with regularization strength (alpha)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Feature selection
model = SelectFromModel(lasso, prefit=True)
selected_features = X.columns[model.get_support()]

print("✅ Selected Features using Lasso Regression:")
for feat in selected_features:
    print(f"✔️ {feat}")