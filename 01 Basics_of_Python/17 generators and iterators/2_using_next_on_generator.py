# Using next() to manually get generator values

def count_up():
    yield "one"
    yield "two"
    yield "three"

gen = count_up()

print(next(gen))
print(next(gen))
print(next(gen))

# next(gen)  # Uncommenting this would raise StopIteration