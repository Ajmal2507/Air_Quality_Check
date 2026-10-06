import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Dataset/cleaned dataset.csv")
pm25 = df[df["pollutant_id"] == "PM2.5"]
pm10 = df[df["pollutant_id"] == "PM10"]

# 1. Number of readings per pollutant category (Category Analysis)
plt.figure(figsize=(7, 4))
df["pollutant_id"].value_counts().plot(kind="barh", color="seagreen")
plt.title("Readings per pollutant category")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("../Visualizations/category_analysis.png", dpi=150)
print("Saved category_analysis.png")
plt.close()

# 2. PM2.5 histogram (Distribution Analysis)
plt.figure(figsize=(7, 4))
plt.hist(pm25["pollutant_avg"].dropna(), bins=30, color="indianred", edgecolor="white")
plt.title("PM2.5 distribution")
plt.xlabel("Average reading")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../Visualizations/distribution_analysis.png", dpi=150)
print("Saved distribution_analysis.png")
plt.close()

# 3. Top 10 states bar chart for PM2.5 (Trend Analysis)
top_states = pm25.groupby("state")["pollutant_avg"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(9, 5))
top_states.plot(kind="bar", color="firebrick")
plt.title("Top 10 States with highest PM2.5")
plt.ylabel("Average PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../Visualizations/trend_analysis.png", dpi=150)
print("Saved trend_analysis.png")
plt.close()

# 4. Scatter plot PM2.5 vs PM10 (Correlation Analysis)
pm25_st = pm25.groupby("station")["pollutant_avg"].mean()
pm10_st = pm10.groupby("station")["pollutant_avg"].mean()
merged = pd.DataFrame({"PM2.5": pm25_st, "PM10": pm10_st}).dropna()

plt.figure(figsize=(7, 5))
plt.scatter(merged["PM10"], merged["PM2.5"], alpha=0.6, color="purple")
plt.title("PM10 vs PM2.5 Averages per Station")
plt.xlabel("PM10 Average")
plt.ylabel("PM2.5 Average")
plt.tight_layout()
plt.savefig("../Visualizations/correlation_analysis.png", dpi=150)
print("Saved correlation_analysis.png")
plt.close()
