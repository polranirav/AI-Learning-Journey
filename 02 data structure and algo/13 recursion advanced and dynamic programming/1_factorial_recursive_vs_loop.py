# Calculate factorial using recursion and iteration
# 🔸 Useful to compare stack vs loop for performance understanding

# Recursive method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial_recursive(n - 1)

# Iterative method
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Recursive:", factorial_recursive(5))  # 120
print("Iterative:", factorial_iterative(5))  # 120