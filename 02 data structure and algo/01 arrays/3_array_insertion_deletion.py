import numpy as np

arr = np.array([1, 2, 3, 4])

# Insert value at position
new_arr = np.insert(arr, 2, 99)  # insert 99 at index 2
print("After insertion:", new_arr)

# Delete value
del_arr = np.delete(arr, 1)  # delete index 1
print("After deletion:", del_arr)