import numpy as np

# 🎯 Create a 2D matrix — useful for tabular data, image patches, or tensor slices
arr = np.array([[10, 20, 30],
                [80, 60, 50],
                [90, 40, 70]])
unsorted = np.sort(arr,axis=1)
print("After sorting:\n", unsorted)

# 🔍 Access a single element using row and column index
print("arr[0, 1] =", arr[0, 1])  # Output: 20

# 📌 Access an entire row
print("First row:", arr[0])  # [10 20 30]

# 📌 Access an entire column
print("Second column:", arr[:, 1])  # [20 50 80]

# 🧩 Slice sub-matrix
print("Top-left 2x2 matrix:\n", arr[0:2, 0:2])
# Output:
# [[10 20]
#  [40 50]]

# 🔁 Modify a section of the array (e.g., for masking)
arr[1:, :] = 0
print("After masking bottom-right corner:\n", arr)

unsorted = np.sort(arr)
print("After sorting:\n", unsorted)
