# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_7_Datetime_Basics\CarAccidents.csv'
df = pd.read_csv(path)

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

print(df.dtypes)



#+++++++++++++++++++++++++++++++
# Convert to DateTime object
df['Date1'] = pd.to_datetime(df['Date1'])
# df['Date2'] = pd.to_datetime(df['Date2']) -- will be error format!!!
df['Date2'] = pd.to_datetime(
    df['Date2'], format='%d-%m-%Y')
print(df.dtypes)
print(df)

#+++++++++++++++++++++++++++++++
# datetime properties
# print(df.Date1.dt.month)
# print(df.Date1.dt.dayofyear)
# print(df.Date1.dt.weekday)

#https://pandas.pydata.org/pandas-docs/stable/reference/

#+++++++++++++++++++++++++++++++
# datetime operations
ts = pd.to_datetime('5/23/2002')
# print(df.loc[df.Date1 >= ts, :])
# print(df.Date1.max())
# print(df.Date1.min())
# days = (df.Date1.max() - df.Date1.min()).days
# print(days)
#+++++++++++++++++++++++++++++++
# Plot data

# add new column Year for sorting by years
df['Year'] = df.Date1.dt.year
print(df)
#
import matplotlib.pyplot as p
#
df.sort_values('Year',inplace=True)
#
df.plot(x='Year',y='Number')
p.show()