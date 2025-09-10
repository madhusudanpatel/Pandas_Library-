# Pandas_Data_Frames.............................................................

# Collection of Multiple series object put togather to share same index.........

import pandas as pd
import numpy as np

# genratiinf data in main memory
from numpy.random import randn
np.random.seed(101)

print(randn(5,4))

df=pd.DataFrame(randn(5,4),index=' A B C D E'.split(),columns='W X Y Z'.split())
print(df)


#................................Selection and Indexing...................................

# #varius method to grab data DataFrames

# print(df['W'])
# print(df[['W','Z']])


# #...............................Creatign a new Column.......................................
# df['New']=df['W']+df['Y']
# print(df)

# #..............................Removing Columns
# print(df.drop('New',axis=1))
# print(df)

# print(df.W)
# print(type(df['W']))

# #.......................................
# print(df.drop('New',axis=1,inplace=True))
# print(df)


#..............................Selecting Row..................................................
# print(df.loc['A'])
# print(type(df.loc['A']))

# print(df.iloc[2])

# print(df.loc['B','Y'])

# print(df.loc[['A','B'],['W','Y']])




#...............................Conditional Selection ...................................

# print(df>0)
# print(df[df>0])

# print(df[df['W']>0])

# print(df[df['W']>0]['Y'])

# print(df[(df['W']>0) & (df['Y']>1)])


#...............................Resetting Indexing...........................


print(df.reset_index())

newind='CA NY WT OR VO'.split()
print(newind)

df['states']=newind
print(df['states'])

print(df.set_index('states'))