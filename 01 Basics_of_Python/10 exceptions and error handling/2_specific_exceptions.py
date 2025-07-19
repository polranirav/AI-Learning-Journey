# Catch specific known errors

try:
    x = int("hello")  # ValueError
except ValueError:
    print("Only numbers are allowed.")

try:
    y = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")