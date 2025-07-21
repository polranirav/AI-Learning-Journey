import seaborn as sns
import matplotlib.pyplot as plt

# Example data
tips = sns.load_dataset("tips")

# Scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Bill vs Tip")
plt.show()

# Heatmap
sns.heatmap(tips.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()