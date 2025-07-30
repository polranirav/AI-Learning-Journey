import numpy as np
import time

# 🎯 Goal: Compare lists and NumPy for speed

# Generate a list and NumPy array of 1 million elements
size = 10**6
py_list = list(range(size))
np_array = np.arange(size)

# ✅ Multiply each element by 2 using list comprehension
start_list = time.time()
list_result = [x * 2 for x in py_list]
end_list = time.time()

# ✅ Multiply using NumPy vectorization
start_np = time.time()
np_result = np_array * 2
end_np = time.time()

print("List Time:", round(end_list - start_list, 5), "seconds")
print("NumPy Time:", round(end_np - start_np, 5), "seconds")