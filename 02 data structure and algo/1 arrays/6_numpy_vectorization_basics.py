import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Vectorized math (faster than loops)
squared = arr ** 2
print("Squared:", squared)

# Normalizing a feature
norm = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print("Normalized:", norm)