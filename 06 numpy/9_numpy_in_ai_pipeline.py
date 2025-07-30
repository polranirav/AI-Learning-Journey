import numpy as np

# 🎯 Step 1: Simulate raw input features (e.g. age, salary, hours studied)
raw_data = np.array([
    [25, 50000, 5],
    [30, 60000, 10],
    [22, 48000, 2],
    [28, 52000, 7]
])

print("Original Data:\n", raw_data)

# ✅ Step 2: Normalize features (Z-score normalization)
mean = np.mean(raw_data, axis=0)
std = np.std(raw_data, axis=0)

normalized_data = (raw_data - mean) / std
print("\nNormalized Data:\n", normalized_data)

# ✅ Step 3: Prepare for model input (e.g., flatten for simple model)
flattened = normalized_data.flatten()
print("\nFlattened Input Vector:\n", flattened)

# 🎯 This simulates preprocessing before feeding into an ML/DL model