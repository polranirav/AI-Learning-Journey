# Examples of multiple Big O complexities

arr = list(range(1, 11))

# O(1): constant time access
print("First:", arr[0])

# O(log n): binary search style loop
n = len(arr)
low, high = 0, n - 1
while low <= high:
    mid = (low + high) // 2
    print("Mid:", arr[mid])
    break  # Just demo one step

# O(n): linear search
target = 9
for i in arr:
    if i == target:
        print("Found:", i)

# O(n^2): nested loop example
for i in arr:
    for j in arr:
        pass  # Time = n*n