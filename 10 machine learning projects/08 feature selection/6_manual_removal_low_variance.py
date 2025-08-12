# Manually remove features based on domain knowledge or inspection
import pandas as pd

df = pd.read_csv("data.csv")

# Say we know 'user_id' and 'signup_flag' have no ML value
df_clean = df.drop(columns=["user_id", "signup_flag"])

print("Columns after manual removal:", df_clean.columns.tolist())