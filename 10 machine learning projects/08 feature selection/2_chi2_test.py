import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder

# Sample categorical dataset
data = {
    "gender": ["male", "female", "female", "male", "female", "male"],
    "smoker": ["yes", "no", "yes", "no", "yes", "no"],
    "bought_insurance": [1, 0, 1, 0, 1, 0]  # Target variable
}

df = pd.DataFrame(data)

# Encode categorical features to numeric
le_gender = LabelEncoder()
le_smoker = LabelEncoder()

df["gender_encoded"] = le_gender.fit_transform(df["gender"])
df["smoker_encoded"] = le_smoker.fit_transform(df["smoker"])

X = df[["gender_encoded", "smoker_encoded"]]
y = df["bought_insurance"]

# Apply chi-squared test
chi2_selector = SelectKBest(score_func=chi2, k="all")
chi2_selector.fit(X, y)

# Print chi2 scores
scores = chi2_selector.scores_
for feature, score in zip(X.columns, scores):
    print(f"{feature}: Chi² score = {score:.2f}")