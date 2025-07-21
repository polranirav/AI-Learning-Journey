# Selection sort: Find the minimum element and place it at the front

def selection_sort(arr):
    for i in range(len(arr)):  # Loop through the entire list
        min_idx = i  # Assume current index is the minimum
        for j in range(i + 1, len(arr)):  # Check rest of list
            if arr[j] < arr[min_idx]:  # If smaller element found
                min_idx = j  # Update index of min
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap current with min

nums = [29, 10, 14, 37, 13]
selection_sort(nums)
print("Sorted:", nums)