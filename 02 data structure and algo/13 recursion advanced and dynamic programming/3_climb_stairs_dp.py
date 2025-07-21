# Count ways to climb stairs (1 or 2 steps at a time)
# 🔸 Same logic used in sequence decoding (step-based decisions)

def climb_stairs(n):
    if n <= 2:
        return n  # Base cases: 1→1 way, 2→2 ways

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2  # Initial known values

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Transition relation

    return dp[n]

print("Ways to climb 5 steps:", climb_stairs(5))  # Output: 8