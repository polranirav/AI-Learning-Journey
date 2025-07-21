# Fibonacci using naive recursion and memoized recursion
# 🔸 Used in NLP decoders, time-series, recursive predictions

# Pure recursion (inefficient)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Memoization (Top-Down DP)
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print("Pure Recursion:", fib_recursive(5))  # 5
print("Memoized:", fib_memo(50))  # Very fast even for large n