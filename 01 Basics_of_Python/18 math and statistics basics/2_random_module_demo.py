import random

# Random integer between 1 and 100
print("Random integer:", random.randint(1, 100))

# Random float between 0 and 1
print("Random float:", random.random())

# Random choice from a list
items = ["cat", "dog", "bird"]
print("Random animal:", random.choice(items))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled:", numbers)

# Seed ensures same results every time (reproducibility)
random.seed(42)
print("Seeded value:", random.randint(1, 100))