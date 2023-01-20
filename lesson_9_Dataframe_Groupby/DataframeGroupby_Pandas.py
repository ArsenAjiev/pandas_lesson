# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_9_Dataframe_Groupby\ProductsSold2.csv'
df = pd.read_csv(path)

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

# group by 1 column
# gb = df.groupby('year')

# group by 2 columns
# gb = df.groupby(['year','gender'])

# print

# for name, group in gb:
#     print(name)
#     print(group)


# operations
# gb2 = df.groupby(['year','gender']).movies.sum()
# gb2 = df.groupby(['year','gender']).sum()
# gb2 = df.groupby(['year','gender']).mean()
# gb2 = df.groupby(['year','gender']).count()
# gb2 = df.groupby(['year','gender']).agg(
#     ['sum','mean','std']
# )
# print(gb2)

# plot
# gb3 = df.groupby(['year']).agg(
#     ['sum','mean','std']
# )
#
df2 = df.drop('year', axis=1)
gb3 = df2.groupby(['gender']).agg(
    ['sum','mean','std']
)
#
#
import matplotlib.pyplot as p
gb3.plot(kind='bar')
p.show()