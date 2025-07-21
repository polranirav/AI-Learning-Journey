# Demonstrates type conversion between string, integer, and float

a = int("10")       # string to integer
b = float("5.5")    # string to float
c = str(100)        # integer to string
print(type(c))  # Output: <class 'str'>


print(a + b)        # Output: 15.5
print("Your score is " + c)  # Output: Your score is 100
