# Dictionary from two lists using comprehension

keys = ['a', 'b', 'c']
values = [1, 2, 3]

mapped = {k: v for k, v in zip(keys, values)}
print("Mapped dictionary:", mapped)

# Create square mapping
squares = {x: x ** 2 for x in range(5)}
print("Number to square:", squares)