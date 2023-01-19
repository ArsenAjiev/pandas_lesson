# To install pandas type in terminal:
# pip install pandas

import pandas as pd


df = pd.read_csv('D:\projects\pandas_tips\lesson_2_Rename_DataFrame\ProductsSold.csv')


print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df.head())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove 1 column

# df.drop(
#     # Remove what?
#     'star rank',
#     # Is a row or a column?
#     axis=1,
#     # Change original dataframe?
#     inplace=True
# )
#
# print()
# print('Remove 1 column')
# print(df.head())





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove 2 columns

df.drop(
    ['Available since', 'total_sells'],
    axis=1,
    inplace=True
)

print()
print('Remove 2 columns')
print(df.head())





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove rows

# df.drop(
#     [1,3],
#     axis = 0,
#     inplace = True
# )
#
# print()
# print('Remove rows')
# print(df.head())