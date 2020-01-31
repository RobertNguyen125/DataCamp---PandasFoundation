import pandas as pd

ts1 = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/ts1.csv')
ts2 = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/ts2.csv')

print(ts1.head())
print(ts2.head())

# create ts3:
ts3 = ts2.reindex(ts1.index)
print(ts3)

ts4 = ts2.reindex(ts1.index, method='ffill')
print(ts4)
