import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], color = 'blue', label='data points')

    # Create first line of best fit
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(list(range(1880, 2051, 1)), fit1.intercept + fit1.slope * range(1880, 2051, 1), 'r',
            label='rate since 1880')

    # Create second line of best fit
    fit2 = linregress(df.loc[df['Year'] >= 2000]['Year'], df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    ax.plot(list(range(2000, 2051, 1)), fit2.intercept + fit2.slope * range(2000, 2051, 1), 'black',
            label='rate since 2000')

    # Add labels and title
    fontsizeelement = 18
    fontsizetitle = 22
    ax.set_title('Rise in Sea Level', fontsize=fontsizetitle)
    ax.set_xlabel('Year', fontsize=fontsizeelement)
    ax.set_ylabel('Sea Level (inches)', fontsize=fontsizeelement)
    ax.tick_params(labelsize=fontsizeelement)
    ax.legend(title='', title_fontsize=fontsizeelement, fontsize=fontsizeelement)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()