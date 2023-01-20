# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_12_Concat_DataFrames\\'

people1 = pd.read_csv(path + 'People1.csv')
people2 = pd.read_csv(path + 'People2.csv')
people3 = pd.read_csv(path + 'People3.csv')

print('-----------------------------')
print('People1')
print(people1)
print()
print('-----------------------------')
print('People2')
print(people2)
print()
print('-----------------------------')
print('People3')
print(people3)
print()
print('-----------------------------')
print('Exercises')

# Concat people1 + people2
# concat1 = pd.concat([people1, people2])
concat1 = pd.concat(
    [people1, people2],
    ignore_index=True
)
#
print(concat1)

# Concat rows - add keys and names
# concat2 = pd.concat(
#     [people1, people2],
#     keys=['people1','people2']
# )
#
# print(concat2)
# print(concat2.loc['people2'])

# Concat (people1 + people2) + people3
# solution 1
# idx = pd.Index([1,0,2,3,4])
# people3 = people3.set_index(idx)
# #
concat3 = pd.concat([concat1, people3], axis=1)
print(concat3)


# solution 2
# p3 = people3.set_index('Name')
# c1 = concat1.set_index('Name')

# concat4 = pd.concat([c1, p3], axis=1, sort=False)
# concat4 = concat4.reset_index()
# concat4.rename(
#     columns={'index':'Name'},
#     inplace=True
# )
# print(concat4)