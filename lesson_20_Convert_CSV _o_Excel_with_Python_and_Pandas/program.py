# 0) install pandas: pip install pandas

# 1) import pandas
import pandas as pd

# 2) read csv file
csv = pd.read_csv('test.csv')

# 3) create excel writer
excelWriter = pd.ExcelWriter('new.xlsx')

# 4) convert csv to excel
csv.to_excel(
    excelWriter,
    index_label= 'ABC',
    index = False,
    float_format = '%.2f',
    #header = False,
    freeze_panes= (3, 1),
    sheet_name= 'my data from csv'
    )

# 5) save excel file
excelWriter.save()