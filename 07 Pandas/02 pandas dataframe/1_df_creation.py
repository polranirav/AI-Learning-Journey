import pandas as pd

# ✅ Create DataFrame from dictionary
data = {
    "name": ["Nirav", "Alex", "Maya"],
    "age": [25, 30, 22],
    "score": [0.85, 0.90, 0.78]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 🎯 AI Use Case:
# - This could be a sample of user profiles or training samples
# - Columns = features, Rows = individual examples

# ✅ Create DataFrame from list of dictionaries
records = [
    {"image_id": "img1", "label": 1, "confidence": 0.95},
    {"image_id": "img2", "label": 0, "confidence": 0.45},
    {"image_id": "img3", "label": 1, "confidence": 0.87},
]

df2 = pd.DataFrame(records)
print("\nPrediction results:\n", df2)

# ✅ Check shape and info
print("\nShape:", df2.shape)
print("Column names:", df2.columns)