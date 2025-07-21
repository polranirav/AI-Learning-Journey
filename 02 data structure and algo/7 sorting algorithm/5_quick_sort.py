# Quick sort: Choose pivot, partition, and sort both sides

def quick_sort(arr):
    if len(arr) <= 1:  # Base case: single or empty
        return arr

    pivot = arr[0]  # Choose first element as pivot
    left = [x for x in arr[1:] if x < pivot]  # Elements less than pivot
    right = [x for x in arr[1:] if x >= pivot]  # Elements greater or equal

    return quick_sort(left) + [pivot] + quick_sort(right)  # Recursive sort and combine

arr = [10, 7, 8, 9, 1, 5]
print("Sorted:", quick_sort(arr))