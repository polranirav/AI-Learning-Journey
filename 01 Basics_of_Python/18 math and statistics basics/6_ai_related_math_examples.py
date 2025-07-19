import math
import random
import statistics

# Normalizing a feature
raw_value = 75
min_val = 50
max_val = 100

normalized = (raw_value - min_val) / (max_val - min_val)
print("Normalized feature (0–1):", round(normalized, 2))

# Rounding probabilities for softmax output
probs = [0.754321, 0.123456, 0.122223]
rounded_probs = [round(p, 2) for p in probs]
print("Rounded probs:", rounded_probs)

# Simulate sampling random batch
dataset = list(range(100))
batch = random.sample(dataset, 5)
print("Random batch of 5:", batch)

# Calculate spread of prediction errors
errors = [-1, 0, 1, 2, -2]
print("Std deviation of error:", round(statistics.stdev(errors), 2))