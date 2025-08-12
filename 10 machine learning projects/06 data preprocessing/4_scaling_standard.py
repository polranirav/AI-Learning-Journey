import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample dataset
data = {
    "Height": [150, 160, 165, 170, 175, 180],
    "Weight": [50, 60, 65, 70, 75, 80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize StandardScaler
scaler = StandardScaler()

# Apply standardization
# This transforms the data to have:
# mean = 0 and standard deviation = 1
scaled_values = scaler.fit_transform(df)

# Convert scaled result back to DataFrame
scaled_df = pd.DataFrame(scaled_values, columns=df.columns)

# Display results
print("Original Data:\n", df)
print("\nStandardized Data:\n", scaled_df)