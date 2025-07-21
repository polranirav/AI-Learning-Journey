# A simple generator that yields numbers 1 to 3

def number_gen():
    yield 1
    yield 2
    yield 3

gen = number_gen()

for val in gen:
    print("Generated:", val)