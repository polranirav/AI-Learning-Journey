# Linear search: check each element one by one
# 🔸 Used when data is small or unsorted

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index where target is found
    return -1  # Return -1 if not found

# Sample usage
data = [4, 2, 9, 5, 1]
target = 5
result = linear_search(data, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in list")