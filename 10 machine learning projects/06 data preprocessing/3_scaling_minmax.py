import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample dataset with continuous features
data = {
    "Height": [150, 160, 165, 170, 175, 180],
    "Weight": [50, 60, 65, 70, 75, 80]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
# Scales values between 0 and 1 using the formula:
# (x - min) / (max - min)
scaled_values = scaler.fit_transform(df)

# Convert scaled values back to a DataFrame
scaled_df = pd.DataFrame(scaled_values, columns=df.columns)

# Show scaled data
print("Original Data:\n", df)
print("\nScaled Data (Min-Max):\n", scaled_df)