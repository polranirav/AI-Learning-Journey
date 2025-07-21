# Binary search: works only on sorted arrays
# 🔸 Fastest way to search in sorted data (O(log n))

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Get middle index
        if arr[mid] == target:
            return mid  # Found
        elif target < arr[mid]:
            high = mid - 1  # Search left half
        else:
            low = mid + 1  # Search right half

    return -1  # Not found

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Test both methods
data = [1, 3, 5, 7, 9, 11]
print("Iterative:", binary_search_iterative(data, 7))
print("Recursive:", binary_search_recursive(data, 7, 0, len(data) - 1))