# Intro to Big O: how fast code grows as input size increases

# O(1): constant time
def constant_example(arr):
    return arr[0]  # Always takes the same time

# O(n): linear time
def linear_example(arr):
    for item in arr:
        print(item)  # Time grows with input size

# O(n^2): quadratic time
def quadratic_example(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Nested loops: time grows with square of size

constant_example([1, 2, 3])
linear_example([1, 2, 3, 4, 5])
quadratic_example([100, 200, 300])