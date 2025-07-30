import pandas as pd

# 🎯 Example: Simulated prediction dataset
df = pd.DataFrame({
    "id": ["img1", "img2", "img3", "img4", "img5"],
    "confidence": [0.91, 0.45, 0.88, 0.30, 0.79],
    "label": [1, 0, 1, 0, 1],
    "predicted": [1, 1, 1, 0, 1]
})

print("Original DataFrame:\n", df)

# ✅ Filter: Confidence > 0.8
high_conf = df[df["confidence"] > 0.8]
print("\nHigh confidence predictions:\n", high_conf)

# ✅ Filter: Mismatched predictions (incorrect labels)
wrong_preds = df[df["label"] != df["predicted"]]
print("\nIncorrect predictions:\n", wrong_preds)

# ✅ Filter: True positives with confidence > 0.75
strong_tp = df[(df["label"] == 1) & (df["confidence"] > 0.75)]
print("\nHigh-confidence true positives:\n", strong_tp)