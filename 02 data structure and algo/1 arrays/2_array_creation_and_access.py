import numpy as np

# Create 1D, 2D arrays
a = np.array([10, 20, 30])
b = np.array([[1, 2, 3], [4, 5, 6]])

# Accessing elements
print("a[1]:", a[1])
print("b[0][2]:", b[0][2])  # or b[0, 2]

# Slicing
print("a[0:2]:", a[0:2])    # [10 20]
print("b[:, 1]:", b[:, 1])  # second column