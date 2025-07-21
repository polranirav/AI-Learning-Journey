import numpy as np

arr = np.array([10, 20, 30, 40])

# Find index where value is 30
idx = np.where(arr == 30)
print("Index of 30:", idx[0])

# Check if a value exists
exists = 25 in arr
print("Does 25 exist?", exists)