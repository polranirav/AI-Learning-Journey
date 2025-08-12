import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Sample dataset
data = {
    "feature": [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Apply polynomial transformation (degree = 2)
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[["feature"]])

# Convert to DataFrame with proper column names
poly_df = pd.DataFrame(poly_features, columns=["feature", "feature_squared"])

# Merge with original data
df = pd.concat([df, poly_df["feature_squared"]], axis=1)

print("📈 Polynomial feature added:")
print(df)