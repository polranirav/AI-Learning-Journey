import pandas as pd

# 🎯 Imagine these are prediction confidence scores
probs = pd.Series([0.91, 0.45, 0.33, 0.78], index=["img1", "img2", "img3", "img4"])

# ✅ Round values using lambda inside .apply()
rounded = probs.apply(lambda x: round(x, 1))
print("Rounded values:\n", rounded)

# 🎯 AI Use Case:
# - Round probabilities for reporting or thresholding

# ✅ Create binary label using threshold
labels = probs.apply(lambda x: 1 if x >= 0.5 else 0)
print("\nBinary labels (threshold=0.5):\n", labels)

# ✅ You can define a custom function too
def grade(x):
    if x >= 0.8:
        return "High"
    elif x >= 0.5:
        return "Medium"
    else:
        return "Low"

grades = probs.apply(grade)
print("\nCustom grading:\n", grades)