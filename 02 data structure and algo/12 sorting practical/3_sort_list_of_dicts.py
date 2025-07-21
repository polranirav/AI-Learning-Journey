# Sort list of dictionaries by a specific key
# 🔸 Use-case: sort models by accuracy from evaluation logs

models = [
    {"name": "A", "acc": 0.85},
    {"name": "B", "acc": 0.92},
    {"name": "C", "acc": 0.78}
]

# Sort by 'acc'
sorted_models = sorted(models, key=lambda x: x["acc"], reverse=True)

for model in sorted_models:
    print(f"{model['name']} → Accuracy: {model['acc']}")