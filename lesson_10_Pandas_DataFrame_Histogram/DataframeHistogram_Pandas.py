# To install pandas type in terminal:
# pip install pandas

import pandas as pd

path = 'D:\projects\pandas_lesson\lesson_10_Pandas_DataFrame_Histogram\People.csv'
df = pd.read_csv(path)

print('\n------------------------------------------')
print('+      >-|o Original DataFrame o|-<      +')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(df)
print()

# histogram for one column
# hist = df['Age'].hist(bins=2)

hist = df['Age'].hist(
    bins=2,
    orientation='horizontal'
    )
#
hist.set_title('My histogram')
hist.set_xlabel('Ages')
hist.set_ylabel('Frequency')


# histogram for all columns
# hist = df.hist(bins=10, grid=False)

# histogram for a subset of columns
hist = df.hist(bins=5, column=['Age'])

# show histogram
import matplotlib.pyplot as p
p.show()