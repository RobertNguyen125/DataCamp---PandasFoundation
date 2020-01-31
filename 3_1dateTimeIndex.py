import pandas as pd

weather = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv')

# extract temperature and date from dataframe to list
temperature_list = weather['Temperature'].tolist()
date_list = weather['Date'].tolist()
# print(temperature_list)
# print(date_list)

time_format = '%Y-%m-%d %H:%M'
my_datetimes = pd.to_datetime(date_list, format =time_format)
# print(my_datetimes)

time_series = pd.Series(temperature_list, date_list)
# print(time_series)

temperature = pd.Series(temperature_list)
ts1 = temperature.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']
print(ts1)
