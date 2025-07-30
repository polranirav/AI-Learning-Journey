# 🕒 Pandas Date and Time – Time-Aware Data Analysis

This folder covers how to **work with datetime data in Pandas** — a common need in AI/ML when handling logs, time-series data, IoT sensors, or sequential datasets.

---

## 📌 Programs in This Folder

### 1. `1_datetime_conversion.py`

Covers:
- Convert string to datetime using `pd.to_datetime()`
- Extract `.dt.date`, `.dt.hour`, `.dt.day_name()`, etc.

Used in:
- Timestamp parsing in logs or JSONs
- Extracting day/week/hour for time-based features
- Preparing features for forecasting models

---

### 2. `2_datetime_filtering.py`

Covers:
- Filter by exact date, hour, or time range
- Use conditions like `>=`, `==`, `&` for time filtering
- `.dt` accessor for granular control

Used in:
- Preprocessing time-sensitive logs
- Windowed training/test splits in time-series
- Cleaning irrelevant rows in ML datasets

---

## 🧠 Real-World Relevance in AI/ML

| Task                          | Method |
|-------------------------------|--------|
| Parse timestamp fields        | `pd.to_datetime()` |
| Slice logs by time            | `df[df["timestamp"] > ...]` |
| Extract time-based features   | `.dt.hour`, `.dt.day_name()` |
| Build hourly/daily models     | Group or filter by time chunks |

---

## 💬 Interview Questions

1. How do you convert a string column to datetime in Pandas?
2. What’s the difference between `.dt.date` and `.dt.strftime()`?
3. How do you filter DataFrame rows within a date range?

---

## ✅ Tip

> Always convert datetime strings before filtering or extracting features — otherwise comparisons will silently fail!

---

📁 **Next Topic:** [07 pandas apply and map →](../07 pandas apply and map/)