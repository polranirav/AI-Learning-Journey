# Demonstrating formatted string output in Python

name = input("Enter your name: ")
age = input("Enter your age: ")

# Traditional method (comma)
print("Hello", name, "you are", age, "years old.")

# Formatted string (f-string) - preferred way
print(f"Hello {name}, you are {age} years old.")  # Introduced in Python 3.6+

# Why it's better:
# - Cleaner syntax
# - Supports inline expressions
print(f"In 5 years, you'll be {int(age) + 5} years old.")