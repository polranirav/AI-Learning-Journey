import sys

# List comprehension (eager)
list_nums = [x * 2 for x in range(1000)]
print("List size (bytes):", sys.getsizeof(list_nums))

# Generator expression (lazy)
gen_nums = (x * 2 for x in range(1000))
print("Generator size (bytes):", sys.getsizeof(gen_nums))