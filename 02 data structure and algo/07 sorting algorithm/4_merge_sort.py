# Merge sort: divide array into halves and merge them sorted

def merge_sort(arr):
    if len(arr) <= 1:  # Base case
        return arr

    mid = len(arr) // 2  # Find middle
    left = merge_sort(arr[:mid])  # Recursively sort left
    right = merge_sort(arr[mid:])  # Recursively sort right

    return merge(left, right)  # Merge two halves

def merge(left, right):
    merged = []  # New sorted list
    i = j = 0  # Pointers for left and right

    while i < len(left) and j < len(right):  # Compare both halves
        if left[i] <= right[j]:
            merged.append(left[i])  # Append smaller value
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])  # Add remaining left
    merged.extend(right[j:])  # Add remaining right
    return merged

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted:", sorted_arr)