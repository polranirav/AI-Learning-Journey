import pandas as pd

# Sample messy dataset
data = {
    "id": ["001", "002", "003"],
    "price": ["1000", "1500", "2000"],
    "join_date": ["2024-01-10", "2024/02/15", "15-03-2024"]
}
df = pd.DataFrame(data)

print("🧪 Before Fix:")
print(df.dtypes)

# 1. Convert ID and price to integer
df["id"] = df["id"].astype(int)
df["price"] = df["price"].astype(float)

# 2. Convert join_date to datetime (with mixed formats)
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

print("\n✅ After Fix:")
print(df.dtypes)
print(df)