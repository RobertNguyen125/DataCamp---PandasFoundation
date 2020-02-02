import pandas as pd
import matplotlib.pyplot as plt
sp500 = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/sp500.csv', parse_dates=True, index_col='Date')

print(sp500.tail())

# sp500['Close'].plot(title='SP500')
# plt.ylabel('Closing Price (US Dollars)')


# sp500.loc['2015-2', 'Close'].plot(style='k.-', title='SP500')
# plt.ylabel('Closing Price (US Dollars)')

# sp500.loc['2015', ['Close', 'Volume']].plot(title='SP500',subplots=True)
# plt.show()


#austin data: we will look at 'Temperature' and 'Date'
austin = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv')

df = austin[['Temperature', 'Date']]
print(df.head())

# df.plot()
# plt.show()
# df.Date = pd.to_datetime(df['Date'])
# df.set_index('Date', inplace=True)
# df.plot()
# plt.show()

# plotting dat ranges, partial indexing
austin = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv', parse_dates=True, index_col='Date')
print(austin.head())

austin.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()
