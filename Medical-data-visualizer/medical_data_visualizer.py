import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
height_in_meters = df["height"] / 100
BMI = df["weight"] / (height_in_meters) ** 2

def is_overweight(bmi):
    if bmi > 25:
        return 1
    else:
        return 0

overweight = BMI.apply(lambda x: is_overweight(x))
df['overweight'] = overweight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize_col(col):
    df[col] = df[col].apply(lambda x: 1 if x > 1 else 0)
	
normalize_col('cholesterol')
normalize_col('gluc')

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=['active', 'alco', 'cholesterol','gluc', 'overweight', 'smoke'])


    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, x="variable", hue="value", col="cardio", kind="count").set_axis_labels("variable", "total")
    fig = fig.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
            & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(20, 15))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", vmax=.3, linewidths=.5, square=True, cbar_kws = {'shrink':0.5}, center=0);



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
