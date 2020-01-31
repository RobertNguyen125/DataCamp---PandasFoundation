import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/titanic.csv')
print(titanic.fare.describe().T)
titanic.fare.plot(kind='box')
plt.show()
