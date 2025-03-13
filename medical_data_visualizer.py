import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = bmi.map(lambda x: 1 if x > 25 else 0)

# 3
# normalize cholesterol
df['cholesterol'] = df['cholesterol'].map(lambda x: 0 if x <= 1 else 1)

# normalize glucose
df['gluc'] = df['gluc'].map(lambda x: 0 if x <= 1 else 1)

# 4
def draw_cat_plot():
    # 5
    """
    Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    """
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    """
    Group and reformat the data in df_cat to split it by cardio. Show the counts (total) of each feature. You will have to rename one of the columns for the catplot to work correctly.
    """
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7 and 8
    facet_grid = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind="bar")
    fig = facet_grid.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    """
    Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
        - diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
        - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
        - height is more than the 97.5th percentile
        - weight is less than the 2.5th percentile
        - weight is more than the 97.5th percentile
    """
    df_heat = df[
        # diastolic pressure is higher than systolic
        (df['ap_lo'] <= df['ap_hi']) & 
        # height is less than the 2.5th percentile 
        (df['height'] >= df['height'].quantile(0.025)) & 
        # height is more than the 97.5th percentile
        (df['height'] <= df['height'].quantile(0.975)) &
        # weight is less than the 2.5th percentile
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        # weight is more than the 97.5th percentile
        (df['weight'] <= df['weight'].quantile(0.975)) 
    ]

    # 12
    # create the corr matrix and round the values
    corr = df_heat.corr()

    # 13
    # create the DataFrame mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 and 15
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f", vmin=0.25, vmax=-0.08)

    # 16
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()
