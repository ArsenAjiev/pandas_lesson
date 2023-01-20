# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_18_DataFrames_Left_Right_Join_Where_NULL\\'

salary = pd.read_csv(path + 'EmployeeSalary.csv')
bonus = pd.read_csv(path + 'EmployeeBonus.csv')

salaryIDi = salary.set_index('ID')
bonusIDi = bonus.set_index('_ID')

# --------------------------------------
# Join instance method
# how - default is left
# res = salary.join(
#     bonusIDi,
#     on = 'ID',
#     lsuffix = '_l',
#     rsuffix = '_r'
# ).query('Name_r.isnull()')

# res = salary.join(
#     bonusIDi,
#     on = 'ID',
#     lsuffix = '_l',
#     rsuffix = '_r',
#     how = 'right'
# ).query('Name_l.isnull()')

# --------------------------------------
# Merge instance method
# how - default is inner

# res = salary.merge(
#     bonusIDi,
#     how='outer',
#     left_on='ID', right_on='_ID',
#     indicator='i'
# )

# res = salary.merge(
#     bonusIDi,
#     how='outer',
#     left_on='ID', right_on='_ID',
#     indicator='i'
# ).query('i == "right_only"')

# --------------------------------------
# Concat function
# join - default is outer
bIDi = bonusIDi.rename(
    columns={
        'Name':'NameB',
        'Value':'ValueB'
    }
)
res = pd.concat(
    [ salaryIDi, bIDi],
    axis = 1,
    join = 'outer'
)
# left join
# res = res.loc[res.Name.notnull(),:]
# left join where null
res = res.loc[res.NameB.isnull(),:]

print(res)