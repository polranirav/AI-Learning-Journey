import pandas as pd

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Summary statistics for numeric columns
print("📊 Descriptive Statistics:")
print(df.describe())

# Median
print("\n📌 Median of total_bill:", df["total_bill"].median())

# Standard deviation
print("📏 Std of tip:", df["tip"].std())

# Correlation matrix
print("\n🔗 Correlation between features:")
print(df.corr(numeric_only=True))