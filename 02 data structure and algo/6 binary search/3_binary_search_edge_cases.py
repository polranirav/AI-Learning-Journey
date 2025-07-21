# Binary search with edge handling: first/last occurrence in duplicates

def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # keep searching left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def find_last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1  # keep searching right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

arr = [1, 2, 4, 4, 4, 5, 6]
print("First 4:", find_first_occurrence(arr, 4))  # 2
print("Last 4:", find_last_occurrence(arr, 4))    # 4