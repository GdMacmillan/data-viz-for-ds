import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import bokeh
import matplotlib.pyplot as plt


df = pd.read_csv('data/crime.csv')

# highest rates of crimes:
high_rates = {}
for crime, idx in zip(df.columns[1:], np.argmax(df.iloc[:, 1:].values, 0)):
    high_rates.update({crime:df.State[idx]})

# lowest rates of crimes:
low_rates = {}
for crime, idx in zip(df.columns[1:], np.argmin(df.iloc[:, 1:].values, 0)):
    low_rates.update({crime:df.State[idx]})

# accross the states, are any crime rates highly correlated

df.set_index('State').corr()

# Looks like robbery and murder might be correlated as well as possibly motor vehicle theft and robbery.

sns.heatmap(df.set_index('State').corr())


# create histograms by crime
fig, axs = plt.subplots(ncols=7)
for num, col in enumerate(df.columns[1:]):
    sns.distplot(df[col], ax= axs[num])

# plotting with kde shows distsribution better

# plot with box plots:

sns.boxplot(data=df.iloc[:, 1:], linewidth=1.0)

# plot with violin plots:

sns.violinplot(data=df.iloc[:, 1:], scale='count', inner='quartile', linewidth=1.0)

# The box plot provides us with the quartiles of each distribution better than the violinplot. The violin plot allows us to better see the shape of the distribution.

# create a bar chart of the aggregate (total) crime rates of each state:
