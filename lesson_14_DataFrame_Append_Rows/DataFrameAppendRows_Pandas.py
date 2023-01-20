# To install pandas type in terminal:
# pip install pandas

# !!! FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version.
# Use pandas.concat instead!!!

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_14_DataFrame_Append_Rows\\'

df = pd.read_csv(path + 'PeopleV2_1.csv')


# -----------------------------------
# dataframe append dataframe
# df2 = pd.read_csv(path + 'PeopleV2_2.csv')

# df = df.append(df2, ignore_index=True)
# df = df.append([df2,df2], verify_integrity=True)



print(df)
# print(df2)
# -----------------------------------
# dataframe append dictionary
# dictionary = {'Name':'Peter','Age':'98'}

# df = df.append(dictionary, ignore_index=True)




# print(df)
# -----------------------------------
# dataframe append series
row = pd.Series(
    ['Chasity','29'],
    index=df.columns
    )

# df = df.append(row, ignore_index=True)
## compare with concat
row = row.to_frame().T
row = row.rename(columns={0:'Name',1:'Age'})
df = pd.concat([df,row], ignore_index=True)




print(df)

