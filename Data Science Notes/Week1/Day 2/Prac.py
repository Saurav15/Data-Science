# Here are some examples : Run them individually and look at the output < Prefer to do it on Jupyter notebook , just looks better there>
# Also Do Do Do DO DO Do visit PAndas Documentation !!!!! Very GOOOODDD :)   https://pandas.pydata.org/docs/index.html


#When working with tabular data, such as data stored in spreadsheets or databases, Pandas is the right tool for you. Pandas will help you to explore, clean and process your data. In Pandas, a data table is called a DataFrame.


# what is the diff between numpy and pandas ?
# Numpy is uesd for basic data structures i.e by using numpy we can use arrays, matrixis and all very easily
# Pandas is made on top of numpy i.e by using pandas we can manipulate all the data very eaily , all of it done using basic Data Structures only but it is managed automatically as we import pandas Library







# Firstly import pandas and numpy libraries

import numpy as np
import pandas as pd


# EXAMPLE 1

# loading hard coded data in pandas dataframe
# Here all this tabular data is stores in arrays only but it will be too tedious to deal with all such arrays mannually so what we can do is directly import pandas and it will do all this for us
#  So the Data Structe in pandas that is used to enter the hard coded Data is called DataFrame()

df = pd.DataFrame(
    [
        ['Jan',58,42,74,22,2.95],
        ['Feb',61,45,78,26,3.02],
        ['Mar',65,48,84,25,2.34],
        ['Apr',67,50,92,28,1.02],
        ['May',71,53,98,35,0.48],
        ['Jun',75,56,107,41,0.11],
        ['Jul',77,58,105,44,0.0],
        ['Aug',77,59,102,43,0.03],
        ['Sep',77,57,103,40,0.17],
        ['Oct',73,54,96,34,0.81],
        ['Nov',64,48,84,30,1.7],
        ['Dec',58,42,73,21,2.56]
    ],
    index=[0,1,2,3,4,5,6,7,8,9,10,11],
    columns=['Month','avg_high','avg_low','record_high','record_low','avg_precipitation']
)
print(df)






# Example 2

#since we dont want to hard code our data everytime
# SO here we will look how to import Data File
filename = "File.txt"
qw = pd.read_csv(filename)
print(qw)




# Example 3

# Now as we have the data we need to manipulate it
# First step to play with Data is to print the needed data on the screen 
# we can print first or last rows of data using qw.head() , qw.tail()

print( qw.head(3) )
print( qw.tail(4) )



# Example 4
# Now we can also get data types , index , columns ,values 
# we use it to check whats all stuff is in our table

print(qw.index) # gives us no. of total index
print(qw.columns) # gives names of all the column
print(qw.dtypes) # gives datatypes of all the column
print(qw.values) # gives all the data present



# Example 5
# Now we know how to print the data that we want
# now comes extracting useful info from the data
#  using the describe() function we get sevral statistical data for each column and each field 

qw.describe()




# Example 6
# now in this example we will see how to sort data by any column

qw.sort_values('record_high',ascending=False) # doing this we have sorted whole table with all the record_high values in Decending order






# Example 7
# In this exaple we will see how to slice  the data i.e only giving output of particular column or row or data field

print( qw.avg_low )# it will output the avg_low column in the tabular form

print(qw['avg_low']) # same thing as above just another way

print(qw[2:3]) # used to slice the rows and getting particular rows as the data

print( qw[['avg_low','avg_high']] ) # used to print 2 given columns and same for any number of columns to print

# how to print n number of rows in given few columns ?
qw.loc[:,['avg_low','avg_high']] #here loc is used to locate ,, here loc method can have 3 parameters i.e loc( from_column:to_column , [ list of columns to print])
qw.loc[3:5,['avg_low','avg_high']] # only print from 3 to 5 rows from columns avg_low and avg_high
qw.loc[9,['avg_low','avg_high']] # we can also put particular row using scalar number
# writing these names of the column avg_high and all is too tedious in loc()
# so we can represent the using index number
qw.iloc[3:7,[2,3]] # use iloc() instead of loc()







# Example 8
# In this example we will see FILTERING data
# i.e eg. getting rows with people age > , = , < 10 etc.

print( qw[qw.avg_precipitation>1.0] ) # used to compare avg_per@#% above 1.0 and gives output all the columns 

qw[qw['month'].isin(['Jun','Jul'])]





# Example 9
# This is the asignment operrator , very similer to slicing 
# By using this , we can cahnge the value of any given field

qw.loc[9,['record_low']] = 106 # this will change the 9th row of record_low column to 106
print(qw[9:10]) # we can verify the changed value by printing it

qw.loc[:,['record_low']] =45 # turns all the row of record_low to 45

# Panda is very well with some missing data eg. in number column if u are missing any number then it will not show any error rather it will show nan 
# Where NAN means NOT A NUMBER ,,,,,,, We can also set it to any field
qw.loc[9,['record_low']] = np.nan

# What we can also do is add a column and add some manipulated data in it
# eg. here we created a new column named 'avg_day' which is avg of avg_low & avg_high
qw['avg_day'] = ( qw.avg_low + avg_high ) / 2
print(qw.avg_day) # we can check it by printing it 








# Example 10
# In this example we will see how to rename the column
qw.rename(columns = {'avg_precipitation' : 'avg_rain'} , inplace= True)
# qw.rename(columns = "Name of thr column to replace" : " By which name to replace")
# Here if we doesnt use inpalce this name will not be saved in file 
# and we have to do is qw= qw.rename(columns = 'avg_pwef#$' : 's#$%)
# so we can use inplace which directly saves it to the orignal file

# NOw if want to change all of the column names we can use this
qw.columns = ['saurav' , 'samyak' ......] # all the new names of the column




# Example 11
#NOw as we are done with manipulating and changing data  !!! 
# we can write to any other file by 
qw.to_csv('Foo.csv')
# we can also save it to another format like excel ,word etc...