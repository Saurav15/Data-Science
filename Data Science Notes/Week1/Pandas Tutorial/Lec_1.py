# Lec_1 is about : 
# How to read tabular data files in pandas ?


import pandas as pd

#Now we need to read some real data we can do it by :
pd.read_table("http://bit.ly/chiporders") # read_table() can directly read from the URL 
# Here we have only seen the data from the URL 
#  We havent saved it yet in any variable ... so first we will save it in a variable in order to use it

orders = pd.read_table("http://bit.ly/chiporders")

# Now We can  just look at first 5 elements to check !
print( orders.head() )





# in pandas default character that separates the columns is the TAB character .
# als0 the first row is present in the file is by default taken as the column name

# CASE 2
# importing another file 
pd.read_table("http://bit.ly/movieusers")

# as we run this we can cleraly say that something is wrong !!
# Because the file put every thing in one column 
# In this file each column is seperated by a pipe(|) character not the default TAB character
# So we can change this default tab character to any character by :
pd.read_table("http://bit.ly/movieusers" , sep="|")  # here "sep" stands for separator !!

# Now the output is much better


# There is also one more problem with this table  
# the first row present here is not the name of the column .. it is part of the data
# so we have to tell pandas that there is no header !!
pd.read_table("http://bit.ly/movieusers", sep="|" , header = None)

# Now the column name has become 0,1,2,3,4
# we we can deal with the data with these column names 
#  so we will change the names of the columns 
# we can do this by passing a Python list .. which contains all the name of the column

user_col = ['user_id','age','gender','occupation','zip_code'] # This list contains the column is the correct order
pd.read_table("http://bit.ly/movieusers",sep="|", header=None , names = user_col) # name is the attributethat assigns the names of the column


# COOL this table now looks perfect !! 
# NOw we will save this table as a DataFrame object

users = pd.read_table("http://bit.ly/movieusers",sep="|", header=None , names = user_col) 

# lets check 
print(users.head())
