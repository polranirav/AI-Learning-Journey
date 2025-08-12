import warnings

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

# Sample dataset
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [30000, 35000, 40000, 45000, 50000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["Experience"]]  # input feature
y = df["Salary"]        # target variable

# Build a pipeline:
# 1. Standardize the feature (scaling)
# 2. Fit a linear regression model
model_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("lr_model", LinearRegression())
])

# Train the model using pipeline
model_pipeline.fit(X, y)

# Predict salary for 6 years of experience
predicted_salary = model_pipeline.predict([[6]])

print("📊 Predicted salary for 6 years of experience:", predicted_salary[0])