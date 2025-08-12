import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Histogram: Distribution of total bill
plt.figure(figsize=(6, 4))
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.show()

# Boxplot: Tip by day
plt.figure(figsize=(6, 4))
sns.boxplot(x="day", y="tip", data=df)
plt.title("Tip Distribution by Day")
plt.show()

# Scatter plot: Total bill vs Tip
plt.figure(figsize=(6, 4))
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.title("Total Bill vs Tip (Colored by Gender)")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()