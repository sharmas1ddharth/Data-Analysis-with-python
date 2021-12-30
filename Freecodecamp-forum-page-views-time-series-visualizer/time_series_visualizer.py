import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(19, 8), dpi=90)
    plt.plot(df, c="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.show();

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # copy original dataset for modification specifically for barplot
    df_bar = df.copy()
    
    # index of the dataset is in datetime format. Extract year and month from index 
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    
    # group year and month and convert view to int
    df_bar = pd.DataFrame(df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int))
    df_bar = df_bar.reset_index()
    df_bar = df_bar.rename(columns={"value" : "Average Page Views"})
    
    # create a dictionary for missing month data for 2016
    missing_data = {'Years' : [2016, 2016, 2016, 2016],
               'Months' : ['January', 'February', 'March', 'April'],
               'Average Page Views': [0, 0, 0, 0]}
    
    # concatenate missing data dataframe to dataset
    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])
    
    # generate the barplot
    fig = plt.figure(figsize=(18, 14))
    sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10");
    plt.xticks(rotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(35, 10), dpi=100)
    sns.boxplot(x="year", y="value", ax=ax[0],data=df_box)
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_ylabel("Page Views")
    ax[0].set_xlabel("Year")

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x="month", y="value", order=month_order, ax=ax[1], data=df_box)
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_ylabel("Page Views")
    ax[0].set_xlabel("Month")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
