# Sort a dictionary by value
# 🔸 Use-case: sort models by accuracy, loss, confidence

model_scores = {
    "model_A": 0.85,
    "model_B": 0.92,
    "model_C": 0.78
}

# Sort by value (ascending)
sorted_asc = dict(sorted(model_scores.items(), key=lambda x: x[1]))

# Sort by value (descending)
sorted_desc = dict(sorted(model_scores.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", sorted_asc)
print("Descending:", sorted_desc)