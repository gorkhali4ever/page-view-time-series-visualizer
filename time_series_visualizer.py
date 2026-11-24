import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#from pandas.plotting import register_matplotlib_converters
#register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'])


# Clean data
df = df[df['value'].between(df['value'].quantile(0.025), df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    ax = df.plot(kind='line', x='date', y='value', color='red', figsize=(15, 5), legend = False)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig = ax.get_figure()
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    plt.close()
    return fig



def draw_bar_plot():

    # Copy and modify data
    df_bar = df.copy()

    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month

    # Group by year and month, calculate average
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()

    # Convert months into columns
    df_bar = df_bar.unstack()

    # Rename month columns
    df_bar.columns = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]

    # Draw bar plot
    ax = df_bar.plot(
        kind='bar',
        figsize=(10, 10),
        title='Average Daily Page Views per Month Grouped by Year',
        xlabel='Years',
        ylabel='Average Page Views'
    )

    ax.legend(title='Month')
    fig = ax.get_figure()

    fig.tight_layout()
    fig.savefig('bar_plot.png')

    plt.close()

    return fig




def draw_box_plot():

    df_box = df.copy()

    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    month_order = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Year-wise box plot
    sns.boxplot(
        data=df_box,
        x='year',
        y='value',
        hue = 'year',
        palette='deep',
        ax=axes[0]
    )

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(
        data=df_box,
        x='month',
        y='value',
        hue = 'month',
        palette='husl',
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.tight_layout()
    fig.savefig('box_plot.png')

    return fig
