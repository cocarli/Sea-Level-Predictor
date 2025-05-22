# Sea Level Predictor

This project analyzes historical sea level data and uses linear regression to project future trends. Built as part of the freeCodeCamp Data Analysis with Python certification.

## Overview

Using data from the U.S. Environmental Protection Agency (EPA), this project creates a visual representation of sea level rise over time and predicts future sea levels through the year 2050 using linear regression models.

## Features

- Scatter plot of historical sea level measurements (1880–2013)
- Linear regression line for all data (1880–2050)
- Second linear regression line using only data from the year 2000 onward (2000–2050)
- Visualization generated with Matplotlib

## Skills Demonstrated

- Linear regression modeling with `scipy.stats.linregress`
- Time series data visualization
- Data filtering with pandas
- Clean and professional plot generation

## Files Included

- `sea_level_predictor.py`: Main script
- `epa-sea-level.csv`: Dataset used for analysis
- `sea_level_plot.png`: Final output image showing sea level predictions

## How to Run

1. Install required libraries:
```bash
pip install pandas matplotlib scipy
```

2. Run the script:
```bash
python sea_level_predictor.py
```

3. The output will be saved as:
- `sea_level_plot.png`

## Dataset Source

Data provided by the [U.S. Environmental Protection Agency (EPA)](https://www.epa.gov/climate-indicators/climate-change-indicators-sea-level), accessed via freeCodeCamp.

---

Created by Carlos Ortiz
