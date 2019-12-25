import pandas as pd
df = pd.read_csv('NanDataset.csv')
##----cleaning rows with nans----#
sumofnan = df.isnull().sum()
print(sumofnan)

#---replaceing NaN with the mean of the column--#
#df.B = df.B.fillna(df.B.mean())
print(df)

#--removing rows---#
df = df.dropna()
#--reset the index--#
df = df.reset_index(drop = True)
print(df)
##--Removing Duplicate Rows--#
dup = pd.read_csv('Duplicaterows.csv')
print(dup.duplicated(keep=False))
#--See all duplicate rows--#
print(dup[dup.duplicated(keep=False)])
#--Drop duplicate rows--#
dup.drop_duplicates(keep='first', inplace=True)
print(dup.reset_index(drop = True))
#--remove duplicates in certain columns by specifying
#subset parameter
dup.drop_duplicates(subset=['A','C'],keep='last',inplace=True)
print(dup)