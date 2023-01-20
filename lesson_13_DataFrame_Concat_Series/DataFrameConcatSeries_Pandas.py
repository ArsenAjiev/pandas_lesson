# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_13_DataFrame_Concat_Series\\'

df = pd.read_csv(path + 'PeopleV2.csv')

print('-----------------------------')
print('PeopleV2')
print(df)

# concat series as rows
# row = pd.Series(['Chasity','29'])
#
# #df = pd.concat([df,row])
# row = row.to_frame().T
# row = row.rename(columns={0:'Name',1:'Age'})
#
# df = pd.concat([df,row], ignore_index=True)
# print(df)




# concat series as columns
col = pd.Series([4,9,4,10,1], name='Score')

df = pd.concat([df,col], axis=1)

print(df)