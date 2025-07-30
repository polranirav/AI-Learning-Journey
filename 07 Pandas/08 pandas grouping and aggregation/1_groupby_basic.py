import pandas as pd

# 🎯 Simulated prediction results
df = pd.DataFrame({
    "model": ["A", "A", "B", "B", "A", "B"],
    "label": ["cat", "dog", "dog", "cat", "cat", "rabbit"],
    "score": [0.91, 0.87, 0.65, 0.72, 0.89, 0.78]
})

# ✅ Group by model → calculate average score
avg_score = df.groupby("model")["score"].mean()
print("📊 Average score per model:\n", avg_score)

# ✅ Group by label → count number of predictions
label_count = df.groupby("label")["model"].count()
print("\n🔢 Prediction count per label:\n", label_count)