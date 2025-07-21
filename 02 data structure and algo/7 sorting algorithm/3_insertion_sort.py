# Insertion sort: Take one element and insert into sorted portion

def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from second element
        key = arr[i]  # Element to insert
        j = i - 1  # Compare with sorted part (left of key)

        while j >= 0 and arr[j] > key:  # Shift greater values to the right
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Place key in correct location

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted:", arr)