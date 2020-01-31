# hist: histogram
# PDF: probability Density Functions
# CDF: cumulative Density Functions

import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/tips.csv')
# print(tips.head())
# print(tips.info())

#format the plot that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# plot PDF
tips.fraction.plot(ax=axes[0], kind='hist', bins=30, density=True, range=(0,0.3))
plt.show()

tips.fraction.plot(ax=axes[0], kind='hist', bins=30, density=True, cumulative=True, range=(0,0.3))
plt.show()
