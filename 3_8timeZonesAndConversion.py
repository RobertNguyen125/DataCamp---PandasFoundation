import pandas as pd

austin = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/3_6austin.csv')

# print(austin.columns)

# boolean mask to filter for 'LAX' departure flight:
mask = austin['Destination Airport'] == 'LAX'

la = austin[mask]

# combine 2 columns of data to crate datetime series: time_tz_zone
time_tz_zone = pd.to_datetime(la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'])
time_tz_central = time_tz_zone.dt.tz.localize('US/Central')
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')
