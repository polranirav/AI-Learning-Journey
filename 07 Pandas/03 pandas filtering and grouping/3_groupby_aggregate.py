import pandas as pd

# 🎯 Simulated dataset: ML model predictions and labels
df = pd.DataFrame({
    "label": ["cat", "dog", "cat", "dog", "cat", "rabbit", "rabbit"],
    "confidence": [0.9, 0.6, 0.88, 0.72, 0.83, 0.95, 0.52],
    "correct": [1, 1, 1, 0, 0, 1, 0]
})

print("Original Data:\n", df)

# ✅ Group by label, get average confidence
avg_conf = df.groupby("label")["confidence"].mean()
print("\nAverage confidence per label:\n", avg_conf)

# ✅ Count number of predictions per label
label_counts = df["label"].value_counts()
print("\nPrediction counts per label:\n", label_counts)

# ✅ Group by label, calculate accuracy (mean of 'correct' flag)
label_accuracy = df.groupby("label")["correct"].mean()
print("\nAccuracy per label:\n", label_accuracy)