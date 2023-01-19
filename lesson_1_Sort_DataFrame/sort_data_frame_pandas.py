# To install pandas type in terminal:
# pip install pandas
# To install numpy:
# pip install numpy
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'A': [50, 70, 9, 70, 100, 8],
        'B': [70, 67, 100, 88, 4, np.nan]
    }
)

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)

# -----------------------------------------------------------------
# Sort Rows by Index

# df = df.sort_index(axis=0, ascending=False)
# df = df.sort_index(ascending=False)
#
# print('\n------------------------------------------')
# print('+    >-|o     Sort Rows by Index   o|-<    +')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(df)


# -----------------------------------------------------------------
# Sort Rows by Values

#df = df.sort_values('A', axis=0)
# df = df.sort_values(['A', 'B'], ascending=[False, True])
#
# print('\n------------------------------------------')
# print('+    >-|o   Sort Rows by Values  o|-<    +')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(df)


# -----------------------------------------------------------------
# Sort Columns by Values

# error because str, needs int
# df = df.sort_values('1', axis=1)
# df = df.sort_values(1, axis=1)
#
# print('\n------------------------------------------')
# print('+   >-|o  Sort Columns by Values  o|-<   +')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(df)


# -----------------------------------------------------------------
# Transpose and Sort Columns by Values


# print('\n------------------------------------------')
# print('+   >-|o   DataFrame Transpose    o|-<   +')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# dft = df.T

# print(dft)

# dft = dft.sort_values('A', axis=1)
# try this :)
# dft = dft.sort_values('B', axis=1, na_position='first')
# dft = dft.sort_values('B', axis=1, na_position='last')

# print('\n------------------------------------------')
# print('+   >-|o  Sort Columns by Values  o|-<   +')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(dft)


# -----------------------------------------------------------------
# Sort Columns by Values - Pretty
# dft = dft.fillna(value=0).astype(int)
#
# print('\n   -----------------------------------------------')
# print('   + >-|o  Sort Columns by Values - Pretty  o|-< +')
# print('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print(dft)


# -----------------------------------------------------------------
# Sort Columns by Index

df = df.sort_index(axis=1, ascending=False)

print('\n------------------------------------------')
print('+  >-|o   Sort Columns by Index   o|-<   +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
