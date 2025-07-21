# Subset Sum Problem: Is there a subset with given sum?
# 🔸 Similar logic used in feature selection and binary choice models

# Recursive version (explores all combinations)
def subset_sum_recursive(arr, target, index=0):
    if target == 0:
        return True
    if index >= len(arr) or target < 0:
        return False
    return (subset_sum_recursive(arr, target - arr[index], index + 1) or
            subset_sum_recursive(arr, target, index + 1))

# DP version
def subset_sum_dp(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True  # Zero sum is always possible

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]  # Can't include current number
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][target]

arr = [3, 34, 4, 12, 5, 2]
target = 9
print("Recursive:", subset_sum_recursive(arr, target))  # True
print("DP:", subset_sum_dp(arr, target))  # True