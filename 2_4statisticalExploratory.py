import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/percent-bachelors-degrees-women-usa.csv')

# print(df.head())

print(df['Engineering'].min())
print(df['Engineering'].max())

mean=df.mean(axis='columns')
print(mean)
mean.plot()
plt.show()
