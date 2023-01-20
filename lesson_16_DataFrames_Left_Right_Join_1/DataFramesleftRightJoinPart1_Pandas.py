# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_16_DataFrames_Left_Right_Join_1\\'

salary = pd.read_csv(path + 'EmployeeSalary.csv')
bonus = pd.read_csv(path + 'EmployeeBonus.csv')

salaryIDi = salary.set_index('ID')
bonusIDi = bonus.set_index('_ID')
# --------------------------
# Left join
# index on index join

res = salaryIDi.join(
    bonusIDi,
    lsuffix = '_fromSalary',
    rsuffix = '_fromBonus'
    )

res.loc[13,'Name_fromBonus'] = 'Octavia'
res.loc[
    res.Value_fromBonus.isnull(),
    'Value_fromBonus'
    ] = 100
# column on index join
# res = salary.join(
#     bonusIDi,
#     lsuffix = '_fromSalary',
#     rsuffix = '_fromBonus',
#     on = 'ID',
#     sort = True
#     )
# --------------------------
# Right join
# res = salaryIDi.join(
#     bonusIDi,
#     lsuffix = '_fromSalary',
#     rsuffix = '_fromBonus',
#     how = 'right'
#     )
#
print(res)