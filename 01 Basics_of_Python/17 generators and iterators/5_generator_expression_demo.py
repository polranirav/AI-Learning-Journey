# Generator expression example (like lazy list comp)

squares = (x * x for x in range(5))

for val in squares:
    print("Square:", val)