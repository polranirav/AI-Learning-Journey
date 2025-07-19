import pandas as pd

data = {
    "department": ["AI", "ML", "AI", "ML"],
    "score": [85, 90, 88, 95]
}

df = pd.DataFrame(data)

# Series access
print("Scores:", df["score"])

# Group by
grouped = df.groupby("department")["score"].mean()
print("Avg score by dept:\n", grouped)