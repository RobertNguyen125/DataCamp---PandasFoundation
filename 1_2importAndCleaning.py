import pandas as pd

col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv('/Users/apple/desktop/pandasFoundation/dataset/ISSN_D_tot.csv', header=None, names=col_names, na_values={'sunspots': [' -1']}, parse_dates=[[0,1,2]])
# NOTE: na_values='-1' to replace -1 with NaN, however because there is a space, we put ' -1'
# NOTE: na_values can be used with list or dict
# NOTE: na_values = {'column_name': ['values']}
# NOTE: parse_dates:
# boolean: if True: parse the the index
# list of ints or name [1,2,3]: try parsing columns 1,2,3 each as a separate date column
# list of lists: [[1,3]]: parse columns 1 and 3 and parse as a single date column

sunspots.index = sunspots['year_month_day'] #create index columns based on the 'year_month_day'
sunspots.index.name = 'date' # label the new index column as 'date' then get rid od 'year_month_day'
cols = ['sunspots', 'definite'] #define 2 columns to keep (excluding the index column)
sunspots = sunspots[cols]
print(sunspots.info())
print(sunspots.iloc[10:20, :])
# print(sunspots.columns)

out_csv = '/Users/apple/desktop/pandasFoundation/sunspots.csv'
sunspots.to_csv(out_csv)

out_tsv = '/Users/apple/desktop/pandasFoundation/sunspots.tsv'
sunspots.to_csv(out_tsv, sep = '\t')

out_xlsx = 'sunspot.xlsx'
sunspots.to_excel(out_xlsx)
