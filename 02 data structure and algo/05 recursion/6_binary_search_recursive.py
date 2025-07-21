# Recursive binary search

def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [1, 3, 5, 7, 9, 11]
print("Index of 7:", binary_search(arr, 7, 0, len(arr) - 1))