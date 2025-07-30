import pandas as pd

# 🎯 Simulated timestamps as strings
df = pd.DataFrame({
    "event": ["Login", "Logout", "Crash", "Restart"],
    "timestamp": ["2025-07-01 10:15:00", "2025-07-01 10:45:00", "2025-07-01 11:00:00", "2025-07-01 11:30:00"]
})

# ✅ Convert timestamp column to datetime objects
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("🔍 After datetime conversion:\n", df)
print("\n📅 Date:", df["timestamp"].dt.date)
print("🕒 Hour:", df["timestamp"].dt.hour)
print("📆 Day of Week:", df["timestamp"].dt.day_name())