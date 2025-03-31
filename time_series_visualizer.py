import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.rename(columns={'value': 'pageviews'})
df['date'] = pd.to_datetime(df['date'])

# Clean data
df = df.loc[(df['pageviews'] >= df['pageviews'].quantile(0.025)) &
            (df['pageviews'] <= df['pageviews'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fontsizeelement = 20
    fontsizetitle = 24
    fig, ax = plt.subplots(figsize=(32, 10), )
    ax.plot(df['date'], df['pageviews'], color='red')
    ax.set_xlabel('Date', fontsize=fontsizeelement)
    ax.set_ylabel('Page Views', fontsize=fontsizeelement)
    ax.tick_params(labelsize=fontsizeelement)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=fontsizetitle, pad=10)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['date'] = (df_bar['date'].dt.strftime('%Y-%m-%d'))
    df_bar[['Year','Month','Day']]= df_bar['date'].str.split('-',expand=True)
    df_bar = round(df_bar.groupby(['Year','Month'])['pageviews'].mean().reset_index(),2)
    df_bar = df_bar.rename(columns={'pageviews':'averageviews'})
    df_bar = pd.pivot_table(data=df_bar,index='Year', columns='Month', values='averageviews')
    months_list = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    df_bar.columns = months_list

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(15.14, 13.3), )
    fontsizeelement = 20
    df_bar.plot(ax=ax, kind='bar')
    ax.set_xlabel('Years', fontsize=fontsizeelement)
    ax.set_ylabel('Average Page Views', fontsize=fontsizeelement)
    ax.legend(title='Months', title_fontsize=fontsizeelement, fontsize=fontsizeelement)
    ax.tick_params(labelsize=fontsizeelement)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

     # Draw box plots (using Seaborn)
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(28.8, 10.8))

    fontsizeelement = 18
    fontsizetitle = 23
    # The title of the first chart should be Year-wise Box Plot (Trend) and the title
    # of the second chart should be Month-wise Box Plot (Seasonality).
    sns.boxplot(ax=ax1, fliersize=3, palette=sns.color_palette(), data=df_box, x='year', y='pageviews')

    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=fontsizetitle, pad=10)
    ax1.set_xlabel('Year', fontsize=fontsizeelement)
    ax1.set_ylabel('Page Views', fontsize=fontsizeelement)
    ax1.tick_params(labelsize=fontsizeelement)

    sns.boxplot(ax=ax2, order=months_list, fliersize=3, palette=sns.color_palette("husl", 12),
                data=df_box, x='month', y='pageviews')
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=fontsizetitle, pad=10)
    ax2.set_xlabel('Month', fontsize=fontsizeelement)
    ax2.set_ylabel('Page Views', fontsize=fontsizeelement)
    ax2.tick_params(labelsize=fontsizeelement)
    ax1.set_ylim(0, 200000)
    ax1.set_yticks(range(0, 200001, 20000))
    ax2.set_yticks(range(0, 200001, 20000))
    ax2.set_ylim(0, 200000)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig