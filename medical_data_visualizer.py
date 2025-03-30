import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = [1 if x > 25 else 0 for x in (df['weight'] / ((df['height'] / 100) ** 2))]

# 3

df['cholesterol'] = [1 if x > 1 else 0 for x in (df['cholesterol'])]
df['gluc'] =        [1 if x > 1 else 0 for x in (df['gluc'])]


# 4 Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['variable', 'cardio', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    # 7
    cat_plot  = sns.catplot(data=df_cat, x=df_cat['variable'], y=df_cat['total'], col="cardio",
                kind='bar', hue="value", order=sorted(df_cat['variable'])
                )

    # 8
    fig = sns.catplot(data=df_cat, x=df_cat['variable'], y=df_cat['total'], col="cardio",
                kind='bar', hue="value", order=sorted(df_cat['variable'])
                )
    fig = fig.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) &
                     (df['height'] >= df['height'].quantile(0.025)) &
                     (df['height'] <= df['height'].quantile(0.975)) &
                     (df['weight'] >= df['weight'].quantile(0.025)) &
                     (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = corr.mask(np.triu(np.ones_like(corr, dtype=bool)))


    # 14
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15
    ax = sns.heatmap(data=mask, vmin=-0.08,
                vmax=0.24, annot=True, fmt=".1f", cbar_kws={"ticks": np.arange(-0.1, 0.3, 0.08), 'shrink': 0.55})


    # 16
    fig.savefig('heatmap.png')
    return fig

