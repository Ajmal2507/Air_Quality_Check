import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("../Dataset/cleaned dataset.csv")
print("Dataset shape:", df.shape)

print("=== Summary Statistics ===")
print(df.describe())

print("\n=== Average Pollutant Values ===")
print(df.groupby("pollutant_id")["pollutant_avg"].mean().round(2))

pm25 = df[df["pollutant_id"] == "PM2.5"]
pm10 = df[df["pollutant_id"] == "PM10"]
print("PM2.5 rows:", len(pm25))
print("PM10  rows:", len(pm10))

print("\n=== Top 10 States by PM2.5 ===")
state_pm25 = pm25.groupby("state")["pollutant_avg"].mean().sort_values(ascending=False)
print(state_pm25.head(10))

print("\n=== Top 10 Cities by PM2.5 ===")
city_pm25 = pm25.groupby("city")["pollutant_avg"].mean().sort_values(ascending=False)
print(city_pm25.head(10))

# How many PM2.5 readings are above 90 (Poor category)
above_90 = pm25[pm25["pollutant_avg"] > 90]
print("\nReadings above 90 :", len(above_90))
pct = len(above_90) / len(pm25) * 100
print("Percentage        : {:.1f}%".format(pct))

# Statistical Analysis
print("\n=== Statistics for PM2.5 and PM10 ===")
pm25_vals = pm25["pollutant_avg"].dropna()
pm10_vals = pm10["pollutant_avg"].dropna()

print("PM2.5 - mean:", round(pm25_vals.mean(), 2), "median:", round(pm25_vals.median(), 2), "std:", round(pm25_vals.std(), 2))
print("PM10  - mean:", round(pm10_vals.mean(),  2), "median:", round(pm10_vals.median(),  2), "std:", round(pm10_vals.std(),  2))
print("PM2.5 skewness:", round(pm25_vals.skew(), 2))
print("PM10  skewness:", round(pm10_vals.skew(),  2))

# Pearson correlation
pm25_df = df[df["pollutant_id"] == "PM2.5"][["station", "pollutant_avg"]].rename(columns={"pollutant_avg": "PM2.5"})
pm10_df = df[df["pollutant_id"] == "PM10"][["station",  "pollutant_avg"]].rename(columns={"pollutant_avg": "PM10"})
merged = pm25_df.merge(pm10_df, on="station")

print("\nStations with both readings:", len(merged))
r, p = stats.pearsonr(merged["PM2.5"], merged["PM10"])
print("Pearson r:", round(r, 3), "  p-value:", round(p, 4))
