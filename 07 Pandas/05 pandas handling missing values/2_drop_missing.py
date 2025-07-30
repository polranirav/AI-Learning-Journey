import pandas as pd
import numpy as np

# 🎯 Simulated data with missing values
df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "age": [25, np.nan, 30, 22],
    "score": [88, 92, np.nan, 79],
    "label": ["A", "B", "B", None]
})

print("Original DataFrame:\n", df)

# ✅ Drop rows with ANY missing value
cleaned_rows = df.dropna()
print("\nRows with NO missing values:\n", cleaned_rows)

# ✅ Drop rows with ALL columns missing (less common)
df_all_nan = df.dropna(how="all")
print("\nDropped rows where ALL values were missing:\n", df_all_nan)

# ✅ Drop columns with ANY missing value
cleaned_cols = df.dropna(axis=1)
print("\nColumns without missing values:\n", cleaned_cols)