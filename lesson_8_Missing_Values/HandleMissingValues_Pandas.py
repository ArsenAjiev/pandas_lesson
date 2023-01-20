# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_8_Missing_Values\missingValues.csv'
df = pd.read_csv(path)

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

# How to spot missing values 
# print(df.isnull())
# print(df.notnull())
# print(df.isnull().sum())

# Filter missing values
# print(df.loc[df.Age.notnull(), :])

# cond = (df.Age.notnull()) & (df.Animal.notnull())
# print(df.loc[cond, :])

# Drop missing values
# print(df.dropna(how='any'))
# print(df.dropna(how='all'))
# print(df.dropna(how='any',subset=['Animal','Age']))

# Fill missing values
# df.Animal.fillna(value='Unknown', inplace=True)
# df.fillna(value='Unknown', inplace=True)

# print(df)