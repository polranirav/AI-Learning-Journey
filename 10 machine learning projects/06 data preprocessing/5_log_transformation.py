import pandas as pd
import numpy as np

# Sample data with skewed values (e.g., income or prices)
data = {
    "Price": [100, 200, 300, 400, 500, 10000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Apply log transformation to reduce skewness
# Use np.log1p to handle 0 safely (log1p(x) = log(1 + x))
df["Log_Price"] = np.log1p(df["Price"])

# Show before and after
print("Original Prices:\n", df["Price"])
print("\nLog Transformed Prices:\n", df["Log_Price"])