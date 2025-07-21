# Build a set of unique squared values

data = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x ** 2 for x in data}

print("Unique squares (set):", unique_squares)