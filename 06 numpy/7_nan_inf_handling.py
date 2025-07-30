import numpy as np

# 🎯 Example: Raw output from some broken pipeline
data = np.array([0.9, np.nan, 0.7, np.inf, -np.inf, 0.3])
print("Raw values:\n", data)

# ✅ Detect NaN (missing value)
print("Is NaN:", np.isnan(data))

# ✅ Detect infinity values
print("Is Inf:", np.isinf(data))

# ✅ Replace NaN with 0
data_clean = np.nan_to_num(data, nan=0.0)
print("\nReplace NaN with 0:\n", data_clean)

# ✅ Replace +inf with 1, -inf with -1
data_final = np.nan_to_num(data_clean, posinf=1.0, neginf=-1.0)
print("\nFinal cleaned data:\n", data_final)