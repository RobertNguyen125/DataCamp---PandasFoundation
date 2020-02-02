import pandas as pd

weather = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv', index_col='Date', parse_dates=True)
# NOTE: parse_dates will return the date format
print(weather.head())


# partial string index
# only print the 'Temperature' column in august
august = weather.loc['2010-08']['Temperature']
# print(august)

# downsample to get the daily highest temperature
august_high = weather.loc['2010-08']['Temperature'].resample('D').max()
print(august_high)
