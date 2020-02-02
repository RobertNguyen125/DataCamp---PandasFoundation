import pandas as pd

sales = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/sales-feb-2015.csv', parse_dates=['Date'])
# print(sales.head())

# work with string column as a whole, using str. attribute
# print(sales['Company'].str.upper())

# substring matching using contain() method
# print(sales['Product'].str.contains('ware').sum())

# datetime method
# dt. attribute to access datetime method

# NOTE: since the there is error that dt can only work with datetime column, force date column to be datatime
# sales["Date"] =  pd.to_datetime(sales["Date"], errors='coerce')
# print(sales['Date'].dt.hour)

# set timezone
central = sales['Date'].dt.tz_centralize('US/Central')
print(central)

method chaining and filtering
austin = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/3_6austin.csv')
# print(austin.shape)

#strip blank space
austin.columns = austin.columns.str.strip()
# find destination as Dallas
dallas = austin['Destination Airport'].str.contains('DAL')
# print(dallas)

# sum of total departure daily
dallas_daily = dallas.resample('D').sum()
print(dallas_daily)
