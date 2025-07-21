# Simulate ML result sorting by accuracy and F1-score
# 🔸 Often needed in experiment tracking, leaderboard building

results = [
    {"name": "baseline", "accuracy": 0.82, "f1": 0.70},
    {"name": "v1", "accuracy": 0.88, "f1": 0.75},
    {"name": "v2", "accuracy": 0.88, "f1": 0.79},
    {"name": "v3", "accuracy": 0.92, "f1": 0.78}
]

# Sort by accuracy DESC, then F1 DESC
top_models = sorted(results, key=lambda x: (-x["accuracy"], -x["f1"]))

for model in top_models:
    print(f"{model['name']} → Acc: {model['accuracy']}, F1: {model['f1']}")