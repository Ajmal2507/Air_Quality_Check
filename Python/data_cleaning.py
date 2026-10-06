import pandas as pd

df = pd.read_csv("../Dataset/dataset.csv")
print("Raw shape:", df.shape)

# Drop country column - it's just 'India' everywhere
if "country" in df.columns:
    df = df.drop(columns=["country"])
print("Columns after dropping country:", df.columns.tolist())

# Fix state and city names - remove underscores, apply title case
df["state"] = df["state"].str.replace("_", " ").str.strip().str.title()
df["city"]  = df["city"].str.strip().str.title()
df["station"] = df["station"].str.strip()

print("Cleaned states list:")
print(sorted(df["state"].unique()))

# Convert last_update to datetime
df["last_update"] = pd.to_datetime(df["last_update"], dayfirst=True)
print("last_update type:", df["last_update"].dtype)

# Rows where min > max (data entry issues)
bad = df[df["pollutant_min"] > df["pollutant_max"]]
print("Bad rows (min > max):", len(bad))

# Drop rows where pollutant_avg is missing
before = len(df)
df = df.dropna(subset=["pollutant_avg"])
print("Rows removed with missing avg:", before - len(df))
print("Shape after cleaning:", df.shape)

df = df.reset_index(drop=True)

# Save the cleaned dataset
df.to_csv("../Dataset/cleaned dataset.csv", index=False)
print("Saved to '../Dataset/cleaned dataset.csv'")
