# Binary search using recursion

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

arr = [5, 10, 15, 20, 25]
print("Index of 20:", binary_search_recursive(arr, 20, 0, len(arr) - 1))  # 3