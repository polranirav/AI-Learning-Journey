import numpy as np

# 🎯 Original matrix: 2 rows × 3 columns
x = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Original shape:", x.shape)  # (2, 3)

# 🔁 Reshape to 3x2 — used to change input shape for models
reshaped = x.reshape((3, 2))
print("Reshaped (3x2):\n", reshaped)

# ⚠️ Total number of elements must stay same (2*3 = 6 = 3*2)

# 📦 Flatten — used to turn matrix into 1D input vector (e.g., image → vector)
flat = x.flatten()
print("Flattened array:", flat)  # [1 2 3 4 5 6]

# 🔧 Reshape to 1 row or 1 column
x_row = x.reshape((1, -1))  # shape: (1, 6)
x_col = x.reshape((-1, 1))  # shape: (6, 1)

print("Row vector shape:", x_row.shape)
print(x_row)
print("Column vector shape:", x_col.shape)
print(x_col)

revale = x.ravel()
print(revale)

#transpose
transpose = x.transpose()
print(transpose)