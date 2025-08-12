import pandas as pd

# Invalid sample data
data = {
    "age": [25, -3, 150, 35],
    "bmi": [21.5, 18.9, 400, -5]
}
df = pd.DataFrame(data)

# 1. Detect domain issues
invalid_ages = df[(df["age"] < 0) | (df["age"] > 120)]
invalid_bmi = df[(df["bmi"] < 10) | (df["bmi"] > 80)]

print("❌ Invalid age entries:\n", invalid_ages)
print("❌ Invalid BMI entries:\n", invalid_bmi)

# 2. Handle domain issues (e.g., replace with median or drop)
df_cleaned = df.copy()
df_cleaned["age"] = df_cleaned["age"].apply(lambda x: x if 0 < x <= 120 else df["age"].median())
df_cleaned["bmi"] = df_cleaned["bmi"].apply(lambda x: x if 10 < x <= 80 else df["bmi"].median())

print("\n✅ Cleaned data:")
print(df_cleaned)