import pandas as pd

data = {
    "name": ["Nirav", "Alex", "Jane"],
    "age": [24, 28, 22]
}

df = pd.DataFrame(data)
print(df)

# Filtering
print("Age > 23:\n", df[df["age"] > 23])