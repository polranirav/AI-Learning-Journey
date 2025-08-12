import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Sample dataset with categorical and numeric features
data = {
    "Region": ["East", "West", "North", "South", "East", "West"],
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [30000, 32000, 40000, 50000, 52000, 60000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Separate features and target
X = df[["Region", "Experience"]]
y = df["Salary"]

# Define preprocessing:
# OneHotEncoder for categorical column "Region"
# StandardScaler for numerical column "Experience"
preprocessor = ColumnTransformer(transformers=[
    ("onehot", OneHotEncoder(), ["Region"]),
    ("scale", StandardScaler(), ["Experience"])
])

# Build full pipeline: preprocessing + linear regression model
pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", LinearRegression())
])

# Train the pipeline
pipeline.fit(X, y)

# Predict salary for a new example
# Region = "South", Experience = 7 years
test_input = pd.DataFrame({"Region": ["South"], "Experience": [7]})
predicted_salary = pipeline.predict(test_input)

print("📈 Predicted salary for South region with 7 years experience:", predicted_salary[0])