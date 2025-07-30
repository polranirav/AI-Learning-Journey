import pandas as pd
import numpy as np

# 🎯 Simulated data with missing values
data = {
    "feature1": [1.2, 2.4, None, 3.3],
    "feature2": [np.nan, 5.5, 6.1, 7.0],
    "label": ["A", None, "B", "A"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# ✅ Detect missing values
print("\nIs Null:\n", df.isnull())

# ✅ Count missing values per column
print("\nMissing values count:\n", df.isnull().sum())

# ✅ Check if any row has missing values
print("\nRows with any missing value:\n", df[df.isnull().any(axis=1)])