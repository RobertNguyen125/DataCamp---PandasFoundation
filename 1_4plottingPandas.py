import pandas as pd
import matplotlib.pyplot as plt

aapl = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/aapl.csv', index_col='Date', parse_dates=True)

# print(aapl.head())

# plotting array
close_arr = aapl['Close'].values # assign APPLE's stock close value to an array
print(type(close_arr))

# plt.plot(close_arr)
# plt.show()

#plotting series
close_series = aapl['Close']
print(type(close_series))
# close_series.plot() # NOTE: this works but plt.plot(close_series) didnt
# plt.show()

# plotting dataframe
aapl.plot()
plt.yscale('log') #logarithmic scale on vertical axis
plt.show()
