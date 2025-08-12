import pandas as pd

# Sample datetime data
data = {
    "user_id": [1, 2, 3],
    "last_login": ["2024-07-15", "2024-08-01", "2024-08-12"]
}
df = pd.DataFrame(data)

# Convert to datetime format
df["last_login"] = pd.to_datetime(df["last_login"])

# Extract time-based features
df["login_month"] = df["last_login"].dt.month
df["login_dayofweek"] = df["last_login"].dt.dayofweek
df["is_weekend_login"] = df["login_dayofweek"] >= 5

print("🕒 Time-based features extracted:")
print(df)