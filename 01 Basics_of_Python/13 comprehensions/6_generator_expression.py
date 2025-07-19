# Generator expression (memory efficient)

gen = (x * 2 for x in range(1000))

print("First 5 doubled numbers:")
for _ in range(20):
    print(next(gen))