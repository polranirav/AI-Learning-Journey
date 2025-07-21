# Compare sum using recursion vs iteration
import time


def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

def sum_iterative(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print("Recursive:", sum_recursive(100))
print("Iterative:", sum_iterative(100))
time_recursive = time.time()  # Measure time for recursive
print("Recursive:", time_recursive)
time_iterative = time.time()  # Measure time for iterative
print("Iterative:", time_iterative)
