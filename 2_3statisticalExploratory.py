import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/iris.csv')

# print(iris.describe().T)

# count, avg, min, max: all ignore the null entries, so need to clean the data before applying
# because their values can be diluted by null values
# print(iris['sepal.length'].count())
# print(iris[['sepal.length','sepal.width']].count()) # NOTE: applied to certain columns
# print(iris.count()) # NOTE: applied to the whole dataframe

# std(): calculate std of non-null values
# print(iris.std())

# median = 0.5 quantiles
q=0.5
# print(iris.quantile(q))
# print(iris.median())

# IQR: inter-quartile range (IQR): from quantile .25 to quantile .75
q=[.25, .75]
# print(iris.quantile(q))

#box Plot
iris.plot(kind='box')
plt.ylabel('[cm]')
plt.show()
