# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_6_Select_with _oc_loc_and_ix\duplicates.csv'
df = pd.read_csv(path)

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# loc 
# filter rows and select columns by label
# resLoc = df.loc[1, :]
# resLoc = df.loc[1, 'Count']
# resLoc = df.loc[[1,3], ['Count','Age']]
# resLoc = df.loc[0:2, 'Animal':'Age']
# resLoc = df.loc[df.Animal=='Cat', :]
# resLoc = df.loc[df['Animal']=='Cat', :]
# resLoc = df.loc[
#     (df.Animal=='Cat') & (df.Color=='white'), :]
#
# print(resLoc)

# df = pd.read_csv(path, index_col='Animal')
# print(df)

#resLoc = df.loc['Dog':'Cat', :]
# resLoc = df.loc['Dog':'Bird', :]

# print(resLoc)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# iloc 
# filter rows and select cols by integer position
# resIloc = df.iloc[ 0:3, : ]
# resIloc = df.iloc[ 0:3, 0:2 ]
# resIloc = df.iloc[df.Animal=='Cat', :]
# print(resIloc)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ix - is deprecated --- Удалено Series.ixи DataFrame.ix( GH26438 ) -- Jan 30, 2020
# allow to mix integers and labels
# df = pd.read_csv(path), index_col='Animal')
# print(df)
#
# resIX = df.ix[1:3, :]
# resIX = df.ix['Dog':'Bird', :]
# resIX = df.ix['Dog':'Bird', 1:2]
# resIX = df.ix['Dog':'Bird', 'Age':'Color']
# print(resIX)