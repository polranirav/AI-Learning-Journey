# Validate internal logic using assert

def divide(x, y):
    assert y != 0, "Denominator cannot be zero"
    return x / y

print("Result:", divide(10, 2))
# print(divide(10, 0))  # Uncomment to see AssertionError