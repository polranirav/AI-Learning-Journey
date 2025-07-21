# Tradeoff: naive vs optimized loop for preprocessing

data = list(range(1, 1001))  # Simulated dataset

# Naive: loop over and build squared values
squared_naive = []
for x in data:
    squared_naive.append(x ** 2)  # O(n)

# Optimized: use list comprehension
squared_fast = [x ** 2 for x in data]  # Also O(n), but runs faster in Python
print(squared_fast)
print("Squared Done")
