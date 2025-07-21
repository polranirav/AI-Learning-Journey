# Use lambda with filter() to keep even numbers

numbers = list(range(10))
even = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even)