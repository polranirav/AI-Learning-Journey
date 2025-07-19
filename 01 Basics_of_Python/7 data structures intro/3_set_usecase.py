# Sets store unique, unordered values

data = [1, 2, 2, 3, 4, 4, 5]
unique = set(data)

print("Original list:", data)
print("Set with unique values:", unique)

# Common operations
unique.add(6)
unique.discard(2)

print("After operations:", unique)