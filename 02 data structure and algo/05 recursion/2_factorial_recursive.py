# Recursive factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))  # 120