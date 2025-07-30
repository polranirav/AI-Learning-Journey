import pandas as pd
import numpy as np

# 🎯 Simulated data with missing values
df = pd.DataFrame({
    "feature1": [10, 20, None, 40],
    "feature2": [1.5, None, 3.5, 4.5],
    "label": ["A", "B", "B", None]
})

print("Original DataFrame:\n", df)

# ✅ Fill numeric NaNs with mean of the column
df["feature1"] = df["feature1"].fillna(df["feature1"].mean())
df["feature2"] = df["feature2"].fillna(df["feature2"].mean())

# ✅ Fill missing labels with a default string
df["label"] = df["label"].fillna("Unknown")

print("\nAfter Filling Missing Values:\n", df)