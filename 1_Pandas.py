# Series is data type in pandas library

# Similar to numpy array 
# Based on Numpy Array
# Series Used axies lables in place of indices
# Series can hanve Objects as data


# #.........................................................................

# import numpy as np
# import pandas as pd 

# # numpy array or dicitionary => convert => series

# labels=['a','b','c']
# my_list=[10,20,30]
# arr=np.array([10,20,30])
# d={'a':10,'b':20,'c':30}

# pd.Series(data=my_list)
# print(pd.Series(data=my_list))
# print(pd.Series(my_list))
# print(pd.Series(my_list,labels))

# #...................................NumPy Array.........................
# arr=np.array([10,20,30])
# print(arr)

# print(pd.Series(arr))
# print(pd.Series(arr,labels))



# ###.................................Data is Series.........................................

# # A pandas libary can have data as object of variuors type

# print(pd.Series(data=labels))

##....................................Index Of Series.......................................

ser1=pd.Series([1,2,3,4],index=['Lucknow','Chennai','Delhi','kolkata'])
print(ser1)

ser2=pd.Series([1,2,5,4],index=['Lucknow','Chennai','Gorakhpur','kolkata'])
print(ser2)

print(ser1['Lucknow'])



# Operation on Series
# print(ser1+ser2)