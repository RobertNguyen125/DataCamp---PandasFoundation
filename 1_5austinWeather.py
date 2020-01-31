import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/weather_data_austin_2010.csv')
print(df.head())

# df.plot(color='red')
# plt.title('Temperature in Austin')
# plt.xlabel('Temperature (degree F)')
# plt.show()

# df.plot(subplots=True)
# plt.show()

# plot 'DewPoint' only
# column1 =['DewPoint']
# df[column1].plot()
# plt.show()

#plot 'DewPoint' and 'Temperature'

column2 = ['DewPoint', 'Temperature']
df[column2].plot()
plt.show()
