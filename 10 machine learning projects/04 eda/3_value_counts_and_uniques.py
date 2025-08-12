import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Unique values in categorical columns
print("🎯 Unique values in 'day':", df["day"].unique())
print("🎯 Unique values in 'sex':", df["sex"].unique())

# Frequency counts
print("\n🔢 Value counts for 'day':")
print(df["day"].value_counts())

print("\n🔢 Value counts for 'smoker':")
print(df["smoker"].value_counts())