# Built-in Python sort functions

nums = [5, 2, 9, 1]

# sorted() returns new sorted list
sorted_nums = sorted(nums)
print("Sorted (new):", sorted_nums)

# list.sort() sorts in-place (changes original list)
nums.sort()
print("Sorted (in-place):", nums)