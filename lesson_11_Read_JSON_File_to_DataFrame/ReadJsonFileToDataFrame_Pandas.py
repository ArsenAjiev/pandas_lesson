# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_11_Read_JSON_File_to_DataFrame\\'

# read json 
# file = 'people1.json'
# df = pd.read_json(path + file)

# print(df)

# file = 'people2.json'
# df = pd.read_json(path + file, orient='split')

# print(df)






# read different json formats
# file = 'people_columns.json'
# file = 'people_split.json'
file = 'people_records.json'
#file = 'people_index.json' 
# file = 'people_values.json'
df = pd.read_json(path + file, orient='records')

print(df)





# Get json string from dataframe
json = df.to_json(orient='table')
print(json)