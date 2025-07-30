import pandas as pd

# 🎯 Series with custom labels — typical in AI pipelines
preds = pd.Series([0.91, 0.80, 0.33], index=["img1", "img2", "img3"])

# ✅ Label-based access (recommended for clarity)
print("Prediction for img1:", preds["img1"])  # Output: 0.91

# ✅ Position-based access (like a list)
print("First prediction:", preds.iloc[0])  # access by position (recommended)

# 🎯 AI Tip:
# - Use label-based access when possible for clarity and safety

# 🔁 Loop through Series
for img_id, score in preds.items():
    print(f"{img_id} → Confidence: {score}")

# 🧪 Bonus: Get top prediction
print("Top prediction:", preds.idxmax(), "->", preds.max())