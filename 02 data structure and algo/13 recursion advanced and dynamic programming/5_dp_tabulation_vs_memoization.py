# Compare Tabulation (Bottom-Up) vs Memoization (Top-Down)
# 🔸 Learn which style works better for different ML tasks

# Memoization (Top-Down)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

print("Memoized:", fib_memo(10))  # 55
print("Tabulated:", fib_tab(10))  # 55