import statistics

data = [1, 2, 3, 4, 5, 5, 6]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))       # Most common value
print("Standard Deviation:", statistics.stdev(data))  # Spread of values
print("Variance:", statistics.variance(data))         # Square of stdev