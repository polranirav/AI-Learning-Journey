# Sort by multiple criteria
# 🔸 Use-case: sort by (accuracy DESC, then name ASC)

models = [
    {"name": "model_C", "acc": 0.92},
    {"name": "model_A", "acc": 0.92},
    {"name": "model_B", "acc": 0.85}
]

# Sort by acc DESC, then name ASC
sorted_multi = sorted(models, key=lambda x: (-x["acc"], x["name"]))

for model in sorted_multi:
    print(model)