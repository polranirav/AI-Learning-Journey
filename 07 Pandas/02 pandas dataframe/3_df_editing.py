import pandas as pd

# Sample data — imagine these are model predictions
df = pd.DataFrame({
    "id": ["img1", "img2", "img3"],
    "label": [1, 0, 1],
    "confidence": [0.95, 0.45, 0.87]
})

print("Original DF:\n", df)

# ✅ Add a new column — auto-filled using logic
df["predicted"] = df["confidence"].apply(lambda x: 1 if x >= 0.5 else 0)
print("\nAfter adding predicted column:\n", df)

# ✅ Update specific row/column value
df.loc[1, "label"] = 1
print("\nUpdated img2 label:\n", df)

# ✅ Add a new row
new_row = {"id": "img4", "label": 0, "confidence": 0.3, "predicted": 0}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\nAfter adding new row:\n", df)

# ✅ Drop a column
df = df.drop("confidence", axis=1)
print("\nAfter dropping 'confidence':\n", df)