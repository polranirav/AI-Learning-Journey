# Flatten nested list using nested list comprehension

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]

print("Flattened list:", flattened)