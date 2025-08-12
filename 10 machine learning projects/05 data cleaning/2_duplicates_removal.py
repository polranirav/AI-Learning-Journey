import pandas as pd

# Load a sample dataset
data = {
    "name": ["Nirav", "Aisha", "Nirav", "John"],
    "age": [25, 30, 25, 22],
    "city": ["Toronto", "NY", "Toronto", "LA"]
}
df = pd.DataFrame(data)

# 1. Check for duplicates
print("🔍 Duplicate rows:")
print(df[df.duplicated()])

# 2. Remove exact duplicates
df_cleaned = df.drop_duplicates()

print("\n✅ Cleaned DataFrame:")
print(df_cleaned)