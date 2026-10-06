# Air Quality Analysis in India (EDA Project)

This is my exploratory data analysis (EDA) project for class. I'm analyzing air quality data from different monitoring stations across India to see which states and cities are the most polluted.

**Author:** Ajmal  
**Libraries used:** pandas, numpy, scipy, matplotlib, seaborn

## About the Data
I got the dataset from the open government data portal (data.gov.in). It's a snapshot of air quality readings taken on Jan 30, 2024. 

The most important columns in the dataset are:
* `state`, `city`, `station` - Where the reading was taken
* `pollutant_id` - The type of pollution being measured (like PM2.5, PM10, SO2, etc.)
* `pollutant_avg` - The average reading for that pollutant
* `latitude` and `longitude` - The exact location of the station

## Project Structure

I have organized the project into the following folder structure:

```text
Data-Analysis-Python-Project/
│
├── README.md
│
├── Dataset/
│   ├── dataset.csv                  (Raw data)
│   └── cleaned dataset.csv          (Cleaned data)
│
├── Notebook/
│   └── Data_Analysis_EDA.ipynb      (All-in-one Jupyter notebook)
│
├── Python/
│   ├── data_loading.py              (Script to load data)
│   ├── data_cleaning.py             (Script to clean data)
│   ├── exploratory_analysis.py      (Script for EDA & stats)
│   └── data_visualization.py        (Script to generate charts)
│
├── Visualizations/
│   ├── distribution_analysis.png
│   ├── trend_analysis.png
│   ├── category_analysis.png
│   └── correlation_analysis.png
│
├── Screenshots/                     (Place screenshots of your output here)
│
└── Documentation/                   (Any extra docs)
```

## How to run my code

**Running the Notebook:**
1. Open your terminal in the main project folder.
2. Type `jupyter notebook` and press enter.
3. Open `Notebook/Data_Analysis_EDA.ipynb` and run all cells.

**Running the Python Scripts:**
You can also run the individual python scripts from the terminal:
1. `cd Python`
2. `python data_loading.py` (Loads and checks the raw data)
3. `python data_cleaning.py` (Cleans data and saves it to the Dataset folder)
4. `python exploratory_analysis.py` (Prints out the statistical findings)
5. `python data_visualization.py` (Saves all the charts into the Visualizations folder)
