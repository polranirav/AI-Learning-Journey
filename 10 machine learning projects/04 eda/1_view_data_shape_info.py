import pandas as pd

# Load example dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# View top 5 rows
print("🔍 Preview data:")
print(df.head())

# Shape of dataset (rows, columns)
print("\n📐 Data shape:", df.shape)

# Info about data types, nulls
print("\nℹ️ Dataset Info:")
print(df.info())