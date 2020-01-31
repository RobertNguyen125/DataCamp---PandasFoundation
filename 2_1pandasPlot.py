import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/iris.csv')
# print(iris.info())

# iris.plot(x='sepal.length',y='sepal.width')
# plt.show() # NOTE: the result is not useful

iris.plot(kind='scatter', x='sepal.length',y='sepal.width')
plt.xlabel('sepal_length (cm)')
plt.ylabel('sepal_width (cm)')
# plt.show()
# plt.savefig('/Users/apple/desktop/pandasFoundation/2_1iris.png')

# box plot:
iris.plot(y='sepal.length', kind='box')
plt.ylabel('sepal width (cm)')
# plt.show()
# plt.savefig('/Users/apple/desktop/pandasFoundation/2_1box.png')

# histogram:
iris.plot(kind='hist', y='sepal.length', bins=30, range=(4,8), normed=True)
plt.xlabel('sepal length (cm)')
# plt.show()
# plt.savefig('/Users/apple/desktop/pandasFoundation/2_1customisedHist.png')

# Cumulative Distribution
iris.plot(kind='hist', y='sepal.length', bins=30, range=(4,8), density=True, cumulative=True)
plt.xlabel('sepal length (cm)')
plt.title('Cumulative Distribution Function (CDF)')
# plt.show()
# plt.savefig('/Users/apple/desktop/pandasFoundation/2_1CDF.png')


df = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/auto-mpg.csv')

print(df.head())

df.plot(kind='scatter', x='hp', y='mpg' )

plt.title('Fuel efficiency vs Horse-power')
plt.xlabel('Horse-power')
plt.ylabel('Fuel efficiency (mpg)')
plt.show()
