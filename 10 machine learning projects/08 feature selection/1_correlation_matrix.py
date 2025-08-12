import pandas as pd
import numpy as np

# Sample dataset with correlated features
data = {
    "temperature": [20, 21, 22, 23, 24, 25, 26],
    "humidity": [30, 33, 36, 39, 42, 45, 48],
    "temp_celsius": [20, 21, 22, 23, 24, 25, 26],  # perfectly correlated with 'temperature'
    "sales": [200, 210, 215, 230, 240, 245, 255]
}

df = pd.DataFrame(data)

# Compute correlation matrix
corr_matrix = df.corr(numeric_only=True)

# Display high correlations (excluding self-correlation)
high_corr = []
threshold = 0.9  # often used in practice

for col in corr_matrix.columns:
    for row in corr_matrix.index:
        if col != row and abs(corr_matrix.loc[row, col]) > threshold:
            high_corr.append((row, col, corr_matrix.loc[row, col]))

print("📊 Correlation Matrix:\n", corr_matrix.round(2))
print("\n🔍 Highly Correlated Feature Pairs (>|0.9|):")
for a, b, score in high_corr:
    print(f"{a} ↔ {b}: correlation = {score:.2f}")