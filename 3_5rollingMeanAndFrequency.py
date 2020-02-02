# rolling means (moving average) is used to smooth out fluctuation in short-term
# rolling() method need to use in chain:
'''hourly_data.rolling(window=24).mean(): would compute new value for each hourly point, based on a
24-hour window stretching out behind each point'''

import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv', index_col='Date', parse_dates=True)

unsmoothed = weather['Temperature']['2010-08-01':'2010-08-15']
print(unsmoothed.head())
smoothed = unsmoothed.rolling(window=24).mean()
print(smoothed.head())

# create new dataframe 'august' with smoothed and unsmoothed columns
august = pd.DataFrame({'smoothed': smoothed, 'unsmoothed': unsmoothed})
print(august)

# august.plot()
# plt.show()
# plt.savefig('/Users/apple/desktop/pandasFoundation/3_5smoothedUnsmoothed.png')
