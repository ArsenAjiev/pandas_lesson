# To install pandas type in terminal:
# pip install pandas

# https://stackoverflow.com/questions/48409128/what-is-the-difference-between-using-loc-and-using-just-square-brackets-to-filte

import pandas as pd

df = pd.read_csv(
    'D:\projects\pandas_lesson\lesson_4_Filter_DataFrame_Rows\ProductsSold.csv')

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Filter by one column
# print('Filter by one column ###########################')

# cond = df['star rank'] > 4.5
# print([i for i in cond])
# print(df[cond])

# same code !!!
# cond = []
# for each element in column star rank
# for rank in df['star rank']:
#     # check if the value is higher than 4.5
#     # and add the result to cond list
#     cond.append(rank > 4.5)

# cond = df['star rank'] > 4.5

# with str using 2 queries
# cond = df['Name of Product'].isin(["A", "E"])


# 1 - brackets notation
# print(df[cond])
# print(df[cond]['Name of Product'])
# print(df[cond][['Name of Product', 'star rank']])

# 2 - loc function
# print(df.loc[cond])
# print(df.loc[cond, 'Name of Product'])
# print(df.loc[cond, ['Name of Product', 'star rank']])

# 2 - isin function
# print(
#     df[df.department.isin(['Art', 'Fashion'])]
# )
#
# print()
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Filter by two or more columns
# print('Filter by two or more columns ###########################')

# & - and
# | - or
# ^ - xor
print(
    df[
        (df['star rank'] > 1) &
        (df['total_sells'] > 10) &
        (df['department'].isin(["Art", "Fashion"]))
        # (df['Name of Product'].isin(["F", "E"]))
    ]
)
