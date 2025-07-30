import numpy as np

# 🎯 Raw input feature vector (e.g., pixel intensities, scores, token counts)
features = np.array([2, 4, 6, 8])

# 🧮 Step 1: Calculate mean and standard deviation
mean = np.mean(features)
std = np.std(features)

# 🔄 Step 2: Normalize using standard score (Z-score normalization)
normalized = (features - mean) / std

print("Original features:", features)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized features:", normalized)