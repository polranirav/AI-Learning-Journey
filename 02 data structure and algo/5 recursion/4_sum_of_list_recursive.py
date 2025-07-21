# Recursive sum of list elements

def sum_list(nums):
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15