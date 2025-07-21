import numpy as np

arr = np.array([5, 10, 15, 20])

# Basic iteration
for i in arr:
    print("Element:", i)

# Vectorized loop alternative
print("Each element x2:", arr * 2)

# Loop with index
for idx, val in enumerate(arr):
    print(f"Index {idx} → {val}")