# Sort list of tuples by a specific index
# 🔸 Use-case: sort (model_name, score) by score

results = [
    ("model_A", 0.85),
    ("model_B", 0.92),
    ("model_C", 0.78)
]

# Sort by score (index 1)
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

print("Sorted:", sorted_results)