import pandas as pd

# Sample transaction data
data = {
    "user_id": [101, 102, 103, 104],
    "transactions": [2, 10, 1, 8],
    "total_spent": [100, 2500, 50, 1800]
}
df = pd.DataFrame(data)

# Add a binary flag: is_high_value_user
df["is_high_value_user"] = df["total_spent"] > 1000

# Add a flag based on transaction count
df["is_frequent_buyer"] = df["transactions"] >= 5

print("✅ Flag features added:")
print(df)