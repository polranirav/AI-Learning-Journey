import pandas as pd

# 🎯 Simulated prediction summary
df = pd.DataFrame({
    "model": ["A", "A", "B", "B", "A", "B"],
    "score": [0.91, 0.87, 0.65, 0.72, 0.89, 0.78],
    "duration": [5, 4, 6, 3, 4, 7]  # time in seconds
})

# ✅ Group by model and apply multiple aggregations
summary = df.groupby("model").agg({
    "score": ["mean", "max", "count"],
    "duration": "sum"
})

print("📊 Aggregated Stats by Model:\n", summary)