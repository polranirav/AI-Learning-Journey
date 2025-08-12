import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset with categorical features
data = {
    "Gender": ["Male", "Female", "Female", "Male", "Other", "Female"],
    "Target": ["Yes", "No", "Yes", "Yes", "No", "No"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a LabelEncoder instance
le = LabelEncoder()

# Encode 'Gender' and 'Target' columns
df["Gender_encoded"] = le.fit_transform(df["Gender"])
df["Target_encoded"] = le.fit_transform(df["Target"])

# Show the transformation
print("Original Data:\n", df[["Gender", "Target"]])
print("\nEncoded Data:\n", df[["Gender_encoded", "Target_encoded"]])