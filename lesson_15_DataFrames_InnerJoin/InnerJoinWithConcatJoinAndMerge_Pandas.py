# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_15_DataFrames_InnerJoin\\'

df_a = pd.read_csv(path + 'PeopleAge.csv')
df_s = pd.read_csv(path + 'PeopleScore.csv')

print(df_a)
print(df_s)

df_a.set_index('Name', inplace=True)
df_s.set_index('Name', inplace=True)
# -----------------------
# Inner Join - Concat
# join default value is 'outer'
# res = pd.concat(
#     [df_a, df_s],
#     axis = 1,
#     join = 'inner'
# )
# res = res.reset_index()
#
# print(res)





# -----------------------
# Inner Join - Join
# how default is left join
# res = df_a.join(df_s, how='inner')
# res = res.reset_index()
# print(res)

# Parameter 'on':
# Column or index level name(s) in the caller 
# to join on the index in other, 
# otherwise joins index-on-index.
# df_a = df_a.reset_index()
# res = df_a.join(df_s, how='inner', on='Name')
# print(res)



# -----------------------
# Inner Join - Merge
# how - default is inner join
# res = df_a.merge(df_s, on='Name')

# print(res)

df_a = df_a.reset_index()
df_s = df_s.reset_index()
res = df_a.merge(df_s, on='Name')

print(res)
