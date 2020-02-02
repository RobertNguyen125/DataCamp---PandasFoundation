import pandas as pd
import numpy as np
ts1 = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/ts1.csv')
ts2 = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/ts2.csv')

# df.interpolate
# https://www.geeksforgeeks.org/python-pandas-dataframe-interpolate/
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

#compute absolute difference between ts1 and ts2_interp
# differences = np.abs(ts1-ts2_interp)
# print(differences)
# print(differences.describe())
