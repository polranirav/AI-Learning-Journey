import pandas as pd

# Sample dataset with a nominal categorical feature
data = {
    "Region": ["North", "South", "East", "West", "South", "East"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Apply One-Hot Encoding to the 'Region' column
# This will create separate binary columns for each unique value
one_hot_df = pd.get_dummies(df, columns=["Region"])

# Show original and encoded data
print("Original Data:\n", df)
print("\nOne-Hot Encoded Data:\n", one_hot_df)