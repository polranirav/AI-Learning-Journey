import pandas as pd

# 🎯 Simulated results: multiple models and classes
df = pd.DataFrame({
    "model": ["A", "A", "B", "B", "A", "B"],
    "label": ["cat", "dog", "dog", "cat", "cat", "rabbit"],
    "score": [0.91, 0.87, 0.65, 0.72, 0.89, 0.78]
})

# ✅ Group by model AND label → average score
avg_score_combo = df.groupby(["model", "label"])["score"].mean()

print("🔄 Average score per model-label combo:\n", avg_score_combo)