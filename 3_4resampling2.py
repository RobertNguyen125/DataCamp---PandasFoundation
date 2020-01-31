import pandas as pd

weather = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv', index_col='Date')
print(weather.head())


weather.to_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/weather_data_austin_2010.csv')
weather2 = pd.read_csv
# time_format = '%Y-%m-%d %H:%M'
# new_datetimes = pd.to_datetime(date, format=time_format)
# print(new_datetimes)

# weather['Date'] = weather['Date'].astype('datetime64[ns]')
# print(weather.head())

# partial string index
# august = weather.loc['2010-08']
