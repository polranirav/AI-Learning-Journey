import pandas as pd
import numpy as np

# Dataset: income values
data = {
    "income": [22000, 35000, 48000, 61000, 75000, 90000, 105000]
}
df = pd.DataFrame(data)

# Bin into income groups (manual binning)
bins = [0, 30000, 60000, 90000, np.inf]
labels = ["Low", "Medium", "High", "Very High"]
df["income_group"] = pd.cut(df["income"], bins=bins, labels=labels)

# Print result
print("📊 Income Binning:")
print(df)