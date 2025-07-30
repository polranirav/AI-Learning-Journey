import numpy as np

# 📌 Create a 1D array (vector) — used for predictions, features, etc.
a = np.array([1, 2, 3])
print("1D Array:", a)

# 📌 Create a 2D array (matrix) — useful for images, tabular data, weight matrices
b = np.array([[1, 2], [3, 4]])
print("2D Array:\n", b)

c= np.full((2,4),8)
print("2D full Array:\n", c)

# 📌 Create an array of all zeros — common for initializing weights or feature masks
zeros = np.zeros((2, 6))  # shape: 2 rows, 3 columns
print("Zeros:\n", zeros)

# 📌 Create an array of all ones — used for bias terms or padding
ones = np.ones((3, 2))  # shape: 3 rows, 2 columns
print("Ones:\n", ones)

# 📌 Create an array with random values (between 0 and 1) — simulate untrained weights or features
rand = np.random.rand(2, 4)
print("Random values:\n", rand)

# 📌 Create an integer range — useful for synthetic label generation
r = np.arange(0, 10, 2)
print("Range array:", r)