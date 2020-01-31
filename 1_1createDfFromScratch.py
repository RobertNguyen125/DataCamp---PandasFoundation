# DataFrames from dict
import pandas as pd
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'visitors': [139, 237, 326, 456],
        'signups': [7, 12, 3, 5]}
print(data)
users = pd.DataFrame(data)
print(users)



import pandas as pd
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7,12,3,5]
visitors = [139, 237, 326, 456]
weekday = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekday] # NOTE: lists of lists above
zipped = list(zip(list_labels, list_cols)) # NOTE: zipped of tuples
# print(zip(list_labels,list_cols))
# print(zipped)

data = dict(zipped)
users = pd.DataFrame(data)
# print(users)

# broadcasting

users['fees'] = 0
print(users)


#broadcasting with a dict
heights = [59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1]
data = {'height': heights, 'sex': 'M'} # NOTE: the key 'height' refers, 'M' is broadcast to entire dataframe
results = pd.DataFrame(data)
print(results)

#
results.columns = ['height (in)', 'sex'] # NOTE: change columns name
results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # NOTE: add index
print(results)
