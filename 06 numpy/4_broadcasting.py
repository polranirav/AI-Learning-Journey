import numpy as np

# 🎯 Scalar Broadcasting — apply scalar to all elements
a = np.array([1, 2, 3])
print("a + 5 =", a + 5)  # [6 7 8]

# ✅ Useful to shift feature vectors or apply constant offset

# 🔁 Broadcasting row + column matrix
m = np.array([[1], [2], [3]])       # shape (3, 1)
v = np.array([10, 20, 30])          # shape (3,)

# This adds v across all rows of m → NumPy auto-expands
print("Broadcasted sum:\n", m + v)
# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# 🎯 Common in NLP attention weights, transformer score adjustment

# ⚠️ Shapes must align per broadcasting rules:
# 1D → (n,)
# Column vector → (n, 1)
# Row vector → (1, m)