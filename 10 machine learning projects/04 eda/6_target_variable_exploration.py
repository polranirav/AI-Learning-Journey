import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Target = tip; let's explore how other features relate to it

# Tip vs Total Bill
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Tip vs Total Bill")
plt.show()

# Average tip by gender
avg_tip_by_sex = df.groupby("sex")["tip"].mean()
print("📊 Avg Tip by Gender:")
print(avg_tip_by_sex)

# Average tip by smoker status
avg_tip_by_smoker = df.groupby("smoker")["tip"].mean()
print("\n📊 Avg Tip by Smoker:")
print(avg_tip_by_smoker)

# Barplot
sns.barplot(data=df, x="smoker", y="tip", ci=None)
plt.title("Avg Tip by Smoker")
plt.show()