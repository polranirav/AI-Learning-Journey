# Assigning multiple values in one line

a, b, c = 10, 20.5, "Python"
print("a =", a)
print("b =", b)
print("c =", c)

a, b = b, a
print("After swap → a =", a, ", b =", b)