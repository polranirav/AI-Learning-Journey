import pandas as pd

# 🎯 Sample predictions
df = pd.DataFrame({
    "score": [0.92, 0.65, 0.48, 0.81],
    "label": ["cat", "dog", "rabbit", "dog"]
})

# ✅ Apply lambda to classify risk
df["risk"] = df["score"].apply(lambda x: "safe" if x >= 0.7 else "risky")

# ✅ Tag label length using lambda
df["label_length"] = df["label"].apply(lambda x: len(x))

print(df)