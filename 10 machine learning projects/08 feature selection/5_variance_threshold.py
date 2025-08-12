# Removes features with very low variance (almost constant)
from sklearn.feature_selection import VarianceThreshold
import pandas as pd

df = pd.read_csv("data.csv")
X = df.drop("target", axis=1)

# Threshold = 0 means remove features with same value across all rows
selector = VarianceThreshold(threshold=0.01)
X_selected = selector.fit_transform(X)

print("Selected shape:", X_selected.shape)