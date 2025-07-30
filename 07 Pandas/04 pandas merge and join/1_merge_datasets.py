import pandas as pd

# 🎯 Example 1: Prediction data
predictions = pd.DataFrame({
    "id": [101, 102, 103],
    "predicted_label": ["cat", "dog", "rabbit"]
})

# 🎯 Example 2: Ground truth labels
ground_truth = pd.DataFrame({
    "id": [101, 102, 104],
    "true_label": ["cat", "dog", "rabbit"]
})

# ✅ Perform an inner join on 'id' (common IDs only)
merged_inner = pd.merge(predictions, ground_truth, on="id", how="inner")
print("🔗 Inner Join:\n", merged_inner)

# ✅ Perform an outer join (all IDs from both sides)
merged_outer = pd.merge(predictions, ground_truth, on="id", how="outer")
print("\n🔄 Outer Join:\n", merged_outer)

# ✅ Perform a left join (all from predictions, matched labels if exist)
merged_left = pd.merge(predictions, ground_truth, on="id", how="left")
print("\n⬅️ Left Join:\n", merged_left)