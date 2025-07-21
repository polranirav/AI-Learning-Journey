# Factorial using recursion vs iteration

# Recursive version (stack used for each call)
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)  # O(n)

# Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result  # O(n)

print("Recursive:", factorial_recursive(5))
print("Iterative:", factorial_iterative(5))