import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/yahooFinance.csv', index_col=0)
print(df.head())

y_columns = ['AAPL', 'IBM']
df.plot(x='Month', y=y_columns)
plt.title('Monthly stock prices')
plt.ylabel('Price (US)')
plt.show()

# plt.savefig('/Users/apple/desktop/pandasFoundation/2_1yahooFinance.png')
