import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Actual Data')

    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = intercept1 + slope1 * x_pred1
    plt.plot(x_pred1, y_pred1, 'r', label='Fit: 1880–2050')

    recent_df = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = intercept2 + slope2 * x_pred2
    plt.plot(x_pred2, y_pred2, 'green', label='Fit: 2000–2050')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
