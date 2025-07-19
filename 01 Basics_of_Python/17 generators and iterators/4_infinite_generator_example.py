# Infinite generator using while loop and yield

def infinite_ones():
    while True:
        yield 1

gen = infinite_ones()
for i in range(5):
    print("Value:", next(gen))