import pandas as pd

# 🎯 Simulated dataset: Model outputs
df = pd.DataFrame({
    "id": ["img1", "img2", "img3", "img4", "img5"],
    "confidence": [0.91, 0.45, 0.88, 0.30, 0.79],
    "label": [1, 0, 1, 0, 1],
    "predicted": [1, 1, 1, 0, 1]
})

print("Original DataFrame:\n", df)

# ✅ AND Condition: label is 1 AND confidence > 0.85
strong_pos = df[(df["label"] == 1) & (df["confidence"] > 0.85)]
print("\nStrong positive predictions:\n", strong_pos)

# ✅ OR Condition: either confidence < 0.5 OR prediction is incorrect
risky = df[(df["confidence"] < 0.5) | (df["label"] != df["predicted"])]
print("\nLow-confidence or incorrect predictions:\n", risky)

# ✅ NOT Condition: filter out correct predictions
only_wrong = df[~(df["label"] == df["predicted"])]
print("\nWrong predictions only:\n", only_wrong)


something = df[(df["nothin"] >= 5) & (df["confidence"] < 0.5)]
