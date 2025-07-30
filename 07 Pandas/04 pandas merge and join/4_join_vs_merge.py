import pandas as pd

# 🎯 DataFrame A: Feature info
features = pd.DataFrame({
    "id": [1, 2, 3],
    "input": ["img1", "img2", "img3"]
}).set_index("id")

# 🎯 DataFrame B: Model output
predictions = pd.DataFrame({
    "id": [1, 2, 3],
    "score": [0.91, 0.85, 0.72]
}).set_index("id")

# ✅ Method 1: Using .join()
joined = features.join(predictions)
print("🔗 Using .join():\n", joined)

# ✅ Method 2: Using pd.merge() (requires resetting index)
merged = pd.merge(features.reset_index(), predictions.reset_index(), on="id", how="inner")
print("\n🔗 Using pd.merge():\n", merged)