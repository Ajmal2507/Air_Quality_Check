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

## Project Breakdown

I split the project into 6 simple notebooks to keep the work organized:

1. **01 Data Collection:** Just loading the raw CSV file to check the shape, columns, and see how many missing values we have.
2. **02 Data Cleaning:** Fixing messy text (like removing underscores in state names), dropping rows that don't have average readings, and saving a clean version of the data into the processed folder.
3. **03 Exploratory Data Analysis:** Getting basic stats, making histograms, and grouping the data to find the highest PM2.5 readings.
4. **04 Statistical Analysis:** Using scipy to run a Pearson correlation (checking if PM2.5 and PM10 are related) and doing a Mann-Whitney U test to compare the most and least polluted states.
5. **05 Visualization:** Making bar charts and scatter plots with matplotlib and seaborn to show the findings visually.
6. **06 Final Analysis:** Building a final scorecard table showing the average pollution for each state and writing down the conclusion.

## How to run my code

1. Open your terminal in the main project folder.
2. Install the required libraries by running: `pip install -r requirements.txt`
3. Make sure the raw data is inside `data/raw/air_quality_raw.csv`
4. Type `jupyter notebook` in your terminal to open it up.
5. Go into the `notebooks/` folder and run the files in order from 01 to 06.

Note: Since this is just a single snapshot of data from one day, we can't look at trends over time, but it still gives a good idea of which areas are highly polluted!
