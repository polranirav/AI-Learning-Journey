# Sort list of dicts by a custom field (accuracy)

models = [
    {"name": "ModelA", "accuracy": 0.85},
    {"name": "ModelB", "accuracy": 0.92},
    {"name": "ModelC", "accuracy": 0.78}
]

# Sort by accuracy in descending order using key lambda
sorted_models = sorted(models, key=lambda x: x["accuracy"], reverse=True)

# Print sorted result
for model in sorted_models:
    print(model["name"], "→", model["accuracy"])