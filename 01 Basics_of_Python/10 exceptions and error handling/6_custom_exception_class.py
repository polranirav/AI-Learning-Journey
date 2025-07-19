# Create a custom exception type

class NegativeNumberError(Exception):
    pass

def check_positive(x):
    if x < 0:
        raise NegativeNumberError("Negative number is not allowed.")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Custom Error:", e)