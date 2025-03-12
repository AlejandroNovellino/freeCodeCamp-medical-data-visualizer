import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
print(df.head())
print()

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

    print(df_cat)
    print()

    # 6
    """
    Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    """
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')

    print(df_cat)
    print()
    
    # 7 and 8
    fig = sns.catplot(data=df_cat, x='variable', y='count', hue='value', col='cardio', kind="bar")

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
