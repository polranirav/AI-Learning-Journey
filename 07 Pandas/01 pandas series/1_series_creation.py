import pandas as pd

# ✅ Creating a simple Series from a list
s1 = pd.Series([0.9, 0.8, 0.3])
print("Basic Series:\n", s1)

# 🎯 AI Use Case:
# - These could represent confidence scores from a classifier.

# ✅ Series with custom index labels
s2 = pd.Series([1, 0, 1], index=['img1', 'img2', 'img3'])
print("\nLabeled Series:\n", s2)

# 🎯 AI Use Case:
# - These could be true class labels (ground truth) for image IDs.

# ✅ Create Series from a dictionary
s3 = pd.Series({'cat': 0.7, 'dog': 0.2, 'frog': 0.1})
print("\nSeries from dict:\n", s3)

# 🎯 AI Use Case:
# - Output of a softmax prediction (multi-class model)

# ✅ Check data type and index
print("Data type:", s3.dtype)
print("Index labels:", s3.index)