import pandas  as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/iris.csv')
# print(iris['variety'].describe())
# print(iris['variety'].unique())

# filtering by variety
indices = iris['variety'] == 'setosa'
setosa = iris.loc[indices,:]
# print(setosa)

indices = iris['variety'] == 'versicolor'
versicolor = iris.loc[indices,:]
# print(versicolor)

indices = iris['variety']  == 'virginica'
virginica = iris.loc[indices, :]
# print(virginica)

# titanic dataset
titanic = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/titanic.csv')

#display the box plot on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# box plot for 1st, 2nd and 3rd class fare
titanic.loc[titanic['pclass']==1].plot(ax=axes[0], y='fare', kind='box')
titanic.loc[titanic['pclass']==2].plot(ax=axes[1], y='fare', kind='box')
titanic.loc[titanic['pclass']==3].plot(ax=axes[2], y='fare', kind='box')
plt.show()
plt.savefig('/Users/apple/desktop/pandasFoundation/2_6titanic.png')
