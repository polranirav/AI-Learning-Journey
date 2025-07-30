import pandas as pd

# 🎯 Example A: Prediction batch 1
batch_1 = pd.DataFrame({
    "id": [1, 2],
    "prediction": ["cat", "dog"]
})

# 🎯 Example B: Prediction batch 2
batch_2 = pd.DataFrame({
    "id": [3, 4],
    "prediction": ["rabbit", "dog"]
})

# ✅ Vertical concat (stack rows)
full_batch = pd.concat([batch_1, batch_2], ignore_index=True)
print("⬇️ Combined Predictions (Rows):\n", full_batch)

# 🎯 Example C: Model 1 outputs
model_1 = pd.DataFrame({
    "id": [1, 2],
    "pred_1": [0.9, 0.7]
})

# 🎯 Example D: Model 2 outputs
model_2 = pd.DataFrame({
    "id": [1, 2],
    "pred_2": [0.8, 0.6]
})

# ✅ Horizontal concat (merge columns)
merged_models = pd.concat([model_1.set_index("id"), model_2.set_index("id")], axis=1)
print("\n➡️ Combined Models (Columns):\n", merged_models.reset_index())