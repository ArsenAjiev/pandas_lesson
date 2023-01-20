# To install pandas type in terminal:
# pip install pandas

import pandas as pd

df = pd.read_csv(
    'D:\projects\pandas_lesson\lesson_5_Remove_DataFrame_Duplicates\duplicates.csv')

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# remove duplicates in column

#code ex1
# ex1 = df.Color.duplicated()

# OR

# ex11 = df['Color'].duplicated()

# print(ex1)
# print(df.loc[ex1])
# print(df.loc[~ex1])

# code ex2
# ex2 = df.drop_duplicates('Color')
# print(ex2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# remove duplicated rows

# code ex3
# ex3 = df.drop_duplicates()
# print(ex3)

# code ex4
# ex4 = df.drop_duplicates(keep=False)
# print(ex4)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# remove duplicated column combination

# code ex5
# ex5 = df.drop_duplicates(subset=['Age','Color'])
# print(ex5)

# keep = 'first'(default), 'last' and False
# code ex6
# ex6 = df.drop_duplicates(
#     subset=['Age','Color'], keep='last')
# print(ex6)