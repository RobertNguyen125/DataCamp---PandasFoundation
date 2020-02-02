import pandas as pd

#example 1: world_population
data_file1 = '/Users/apple/desktop/pandasFoundation/dataset/world_population.csv'
df1 = pd.read_csv(data_file1)
new_labels = ['year', 'population']

df2 = pd.read_csv(data_file1, header=0 , names=new_labels)

# print(df1.head())
# print(df2.head())

#example 2: messy_stock_data
file_messy = '/Users/apple/desktop/pandasFoundation/dataset/messy_stock_data.tsv'
df1 = pd.read_csv(file_messy)

# print(df1.head())

# Issues:
# multiple header lines,
# comment records (rows) interleaved throughout the data rows,
# and space delimiters instead of commas.

df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
print(df2.head())

df2.to_csv('/Users/apple/desktop/pandasFoundation/cleanedDataset/file_clean.csv', index=False)

df2.to_excel('/Users/apple/desktop/pandasFoundation/cleanedDataset/file_clean.xlsx', index=False)
