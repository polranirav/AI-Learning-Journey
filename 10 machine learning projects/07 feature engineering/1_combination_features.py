import pandas as pd

# Create basic dataset
data = {
    "area": [1000, 1500, 1200, 1300],
    "bedrooms": [2, 3, 2, 4],
    "price": [300000, 450000, 360000, 520000]
}
df = pd.DataFrame(data)

# Create a new feature: price per sqft
df["price_per_sqft"] = df["price"] / df["area"]

# Create another feature: rooms per 1000 sqft
df["bedrooms_per_1000_sqft"] = df["bedrooms"] / (df["area"] / 1000)

# Print transformed dataset
print("🔍 Engineered Features:")
print(df)