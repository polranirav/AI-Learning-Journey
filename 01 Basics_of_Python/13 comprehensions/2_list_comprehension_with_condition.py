# Filter even numbers using list comprehension

numbers = list(range(100))
even = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even)