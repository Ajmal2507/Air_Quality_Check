import pandas as pd

# Load the raw dataset
df = pd.read_csv("../Dataset/dataset.csv")
print("Raw shape:", df.shape)

# Display first 10 rows
print(df.head(10))

# Display info about the dataset
df.info()

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Basic counts
print("States  :", df["state"].nunique())
print("Cities  :", df["city"].nunique())
print("Stations:", df["station"].nunique())

# Check pollutant types
print("Pollutant value counts:")
print(df["pollutant_id"].value_counts())

# Check states
print("State value counts:")
print(df["state"].value_counts())

# Basic descriptive statistics
print("Summary stats for min, max, avg:")
print(df[["pollutant_min", "pollutant_max", "pollutant_avg"]].describe())

# Check for duplicates
print("Duplicate rows:", df.duplicated().sum())
