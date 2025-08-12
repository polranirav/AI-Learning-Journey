import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")

# 1. Visualize outliers using boxplot
sns.boxplot(x=df["total_bill"])
plt.title("Boxplot: total_bill")
plt.show()

# 2. Calculate IQR
Q1 = df["total_bill"].quantile(0.25)
Q3 = df["total_bill"].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 3. Filter out outliers
df_no_outliers = df[(df["total_bill"] >= lower_bound) & (df["total_bill"] <= upper_bound)]

print(f"Original count: {len(df)} | After removing outliers: {len(df_no_outliers)}")