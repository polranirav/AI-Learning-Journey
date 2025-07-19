# Without comprehension
squares = []
for x in range(5):
    squares.append(x ** 2)

print("With loop:", squares)

# With list comprehension
squares_comp = [x ** 2 for x in range(5)]
print("With comprehension:", squares_comp)