# Bubble sort: Compare adjacent elements and swap if out of order

def bubble_sort(arr):
    n = len(arr)  # Length of the list
    for i in range(n):  # Outer loop for number of passes
        for j in range(0, n - 1 - i):  # Inner loop for comparisons
            if arr[j] > arr[j + 1]:  # If left > right, swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swapping in Python

data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print("Sorted:", data)