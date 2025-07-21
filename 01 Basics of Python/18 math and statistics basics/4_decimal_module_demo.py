from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 4

# Decimal keeps precision (better than float for financial calc)
a = Decimal('1.10')
b = Decimal('2.30')
print("Decimal sum:", a + b)  # Output will be precise

# With float, precision might be off
print("Float sum:", 1.10 + 2.30)