# To install pandas type in terminal:
# pip install pandas
import pandas as pd

filePath = 'D:\projects\pandas_tips\lesson_2_Rename_DataFrame\ProductsSold.csv'
df = pd.read_csv(filePath)

# options to list the columnss
# columns = df.columns
# columns = list(df)
columns = df.columns.values

# options to format string
#print('Columns: ', columns)
#print('Columns: {cols}'.format(cols=columns))
print(f'Columns: {columns}') # string interpolation


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# option 1 - use rename functions
df = pd.read_csv(filePath)

df.rename(
    # Rename what?
    columns={
        'Name of Product':'Product Name',
        'total_sells':'Total Sells'},
    # Change original data?
    inplace=True
)

print(f'option 1: {df.columns.values}')




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# option 2 - override column names
# df = pd.read_csv(filePath)
#
# newNames = [
#     'Product3 Name',
#     'Available3 Since',
#     'Total3  Sells',
#     'Star3 Rank'
# ]
#
# df.columns = newNames
#
# print(f'option 2: {df.columns.values}')




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# option 3 - using csv parameter
# df = pd.read_csv(
#     # Load from where?
#     filePath,
#     # What are the column names?
#     # with this argument...
#     # pandas 'think' that source file has no headers!
#     # i.e. header=None
#     names=newNames,
#     # Which row has the names to be replaced? header exists it is row 0!
#     header=0)
#
# print(df.head())
#
# print(f'option 3: {df.columns.values}')




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# option 4
# df = pd.read_csv(filePath)
#
# df.columns = (
#     df.columns
#     .str.replace('_', ' ')
#     .str.replace('Name of Product', 'Product Name')
#     .str.title()
# )
#
# print(f'option 4: {df.columns.values}')