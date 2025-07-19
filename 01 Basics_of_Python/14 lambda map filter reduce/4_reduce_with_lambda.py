from functools import reduce

# Use lambda with reduce() to multiply all numbers

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print("Product of all numbers:", product)
# Output: Product of all numbers: 120
# 120 is the product of 1, 2, 3, 4, and 5