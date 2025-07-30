import pandas as pd

# Sample DataFrame — could represent ML dataset
df = pd.DataFrame({
    "name": ["Nirav", "Alex", "Maya"],
    "age": [25, 30, 22],
    "score": [0.85, 0.90, 0.78]
})

# ✅ Select a single column (as Series)
print("Names:\n", df["name"])

# ✅ Select multiple columns
print("\nName + Score:\n", df[["name", "score"]])

# ✅ Select a row by index position
print("\nFirst row:\n", df.iloc[0])

# ✅ Select multiple rows by index range
print("\nFirst 2 rows:\n", df.iloc[0:2])

# ✅ Row and column selection together
print("\nAlex's score:\n", df.loc[1, "score"])

# 🎯 AI Use Case:
# - Select feature columns: `df[["feature1", "feature2"]]`
# - Get label by row: `df.loc[i, "label"]`