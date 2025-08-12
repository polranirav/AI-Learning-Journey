import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset with missing values
df = sns.load_dataset("titanic")

# 1. Check for missing values
print(df.isnull().sum())

# 2. Visualize missing values
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Value Heatmap")
plt.show()

# 3. Drop rows with missing age
df_cleaned = df.dropna(subset=["age"])

# 4. Impute missing 'embarked' with mode
df["embarked"].fillna(df["embarked"].mode()[0], inplace=True)

# 5. Impute missing 'age' with median
df["age"].fillna(df["age"].median(), inplace=True)

print("\n✅ Cleaned missing values:")
print(df.isnull().sum())