import pandas as pd

# Sample messy categorical data
data = {
    "gender": ["Male", "male", "FEMALE", "female", "MALE", "Female"],
    "response": ["Yes", "yes", "NO", "No", "Y", "n"]
}
df = pd.DataFrame(data)

print("🧪 Before cleanup:")
print(df["gender"].value_counts())
print(df["response"].value_counts())

# 1. Standardize gender values
df["gender"] = df["gender"].str.lower().str.strip()
df["gender"] = df["gender"].replace({"female": "f", "male": "m"})

# 2. Standardize response values
df["response"] = df["response"].str.lower().str.strip()
df["response"] = df["response"].replace({"yes": "y", "no": "n"})

print("\n✅ After cleanup:")
print(df["gender"].value_counts())
print(df["response"].value_counts())
print(df)