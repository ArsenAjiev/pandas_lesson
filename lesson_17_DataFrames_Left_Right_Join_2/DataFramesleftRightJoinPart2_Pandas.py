# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_17_DataFrames_Left_Right_Join_2\\'

salary = pd.read_csv(path + 'EmployeeSalary.csv')
bonus = pd.read_csv(path + 'EmployeeBonus.csv')

salaryIDi = salary.set_index('ID')
bonusIDi = bonus.set_index('_ID')

# --------------------------
# Left join
# index on index join

# option 1
# bonusIDi.index.names = ['ID']
# # how - default is inner join
# res = salaryIDi.merge(
#     bonusIDi,
#     on='ID',
#     how='left'
# )
# print(res)


# option 2
# column on column
# res1 = salary.merge(
#     bonus,
#     how='left',
#     left_on = 'ID',
#     right_on = '_ID'
# )


# column on index
# res2 = salary.merge(
#     bonusIDi,
#     how='left',
#     left_on = 'ID',
#     right_on = '_ID'
# )

# index on column
res3 = salaryIDi.merge(
    bonus,
    how='left',
    left_on = 'ID',
    right_on = '_ID'
)

# print('column on column')
# print(res1)
# print('column on index')
# print(res2)
# print('index on column')
# print(res3)


# index on index - don't work!
# res4 = salaryIDi.merge(
#     bonusIDi,
#     how='left',
#     left_on = 'ID',
#     right_on = '_ID'
# )
# print(res4)








# index on index using 'left_index' parameter
res = salaryIDi.merge(
    bonusIDi,
    how='left'
    , left_index = True
    , right_on = '_ID'
     #, left_on = 'ID'
     #, right_index = True
)
print(res)





# suffixes
# res = salaryIDi.merge(
#     bonus,
#     how='right',
#     left_on = 'ID',
#     right_on = '_ID',
#     suffixes = ('_fromSalary', '_fromBonus')
# )
# print(res)