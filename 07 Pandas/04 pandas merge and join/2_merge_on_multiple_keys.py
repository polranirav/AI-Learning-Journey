import pandas as pd

# 🎯 Dataset A: Predictions by model version
preds = pd.DataFrame({
    "id": [101, 102, 103, 101],
    "version": ["v1", "v1", "v1", "v2"],
    "prediction": ["cat", "dog", "rabbit", "dog"]
})

# 🎯 Dataset B: Ground truth (with version info)
truth = pd.DataFrame({
    "id": [101, 102, 103, 101],
    "version": ["v1", "v1", "v1", "v2"],
    "label": ["cat", "dog", "rabbit", "dog"]
})

# ✅ Merge using two columns: 'id' and 'version'
merged = pd.merge(preds, truth, on=["id", "version"], how="inner")
print("🔗 Merged on id + version:\n", merged)