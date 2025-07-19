# Validate user input safely

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as e:
    print("Invalid input:", e)