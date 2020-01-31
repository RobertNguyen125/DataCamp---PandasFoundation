# downsampling: reduce datetime rows to slower frequency (from daily to weekly)
# upsampling: increase datetime rows to faster frequency (from weekly to dail)

import pandas as pd

sales = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/sales-feb-2015.csv', index_col='Date', parse_dates=True)
print(sales.head())


#aggregate means
daily_mean = sales.resample('D').mean()
# NOTE: resample() method need a string argument for frequency. 'D' is daily, 'W': weekly
# NOTE: resample() method is best followed by statistical method, e.g:mean,count,std
# NOTE: columns arent numerical will be ignored

# check for the mean sales on 2ndFeb2015
# print(daily_mean.loc['2015-2-2'])

# check the actual sales
# print(sales.loc['2015-2-2', 'Units'])

# long chain method
# print(sales.resample('D').sum().max()) # the maximum sales in Feb

# multi-frequency
# print(sales.loc[:,'Units'].resample('2W').sum()) #fortnightly

# upsampling
two_day = sales.loc['2015-2-4':'2015-2-5', 'Units']
print(two_day)

print(two_day.resample('4H').ffill())
