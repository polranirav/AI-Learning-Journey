import pandas as pd

# 🎯 Categorical predictions
df = pd.DataFrame({
    "label": ["cat", "dog", "rabbit", "dog"],
    "score": [0.91, 0.45, 0.83, 0.60]
})

# ✅ Use map() with a dictionary to relabel
label_map = {"cat": "🐱", "dog": "🐶", "rabbit": "🐰"}
df["emoji_label"] = df["label"].map(label_map)

# ✅ Use apply() for conditional transformation
df["score_bucket"] = df["score"].apply(lambda x: "high" if x > 0.8 else "low")

print(df)