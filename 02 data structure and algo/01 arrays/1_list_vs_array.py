# Native Python list
py_list = [1, 2, 3]

# NumPy array
import numpy as np
np_array = np.array([1, 2, 3])

print("Python list:", py_list)
print("NumPy array:", np_array)

# Difference: list stores mixed types
mixed_list = [1, "AI", True]
print("Mixed list:", mixed_list)

# NumPy is better for numerical operations
print("Numpy + 1:", np_array + 1)  # Broadcasts over array
# print(py_list + 1)  # ❌ Error: list doesn't support this