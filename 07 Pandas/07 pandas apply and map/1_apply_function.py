import pandas as pd

# 🎯 Sample DataFrame: model outputs
df = pd.DataFrame({
    "score": [0.91, 0.45, 0.83, 0.60],
    "label": ["cat", "dog", "rabbit", "cat"]
})

# ✅ Define custom function to classify confidence
def classify_conf(score):
    if score >= 0.8:
        return "High"
    elif score >= 0.6:
        return "Medium"
    else:
        return "Low"

# ✅ Apply function to score column
df["confidence_level"] = df["score"].apply(classify_conf)

print(df)