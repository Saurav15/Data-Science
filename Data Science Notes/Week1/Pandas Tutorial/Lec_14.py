# In Lec_14 we will see:
#       How to handle missing values in pandas ?

import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")
print( ufo.tail() )


# Here we see in the Reported Shape taht there is a frequent NaN which means Not a Number
# Which conceptually means there is a missing value in that column 

# Lets look at some methods for working with missing values !

# 1. isnull() method 
ufo.isnull()  # It gives trues if any values is missing 

# 2. There is another method which is opposite of isnull() i.e notnull()
ufo.notnull()


# What can we do with these methods ?
ufo.isnull().sum()  # It gives us the total no. of empty values in each columns !

# Here what actully sum() is doing is it takes true =1 and false=0 so in sum() it adds all the 1's in the list
# We can also write it as
ufo.isnull().sum(axis=0)



# The isnull() is not only dataframe method as shown above 
# It can also be used as seris method
ufo[ ufo.City.isnull() ] 
# This will return the All 25 rows where City is NUll 





# Until now we have only answered how to see where the null values are or count them 
# But we havent see what to do with those null values ? 
# So lets see !



# There are certain option that we use when we have no values

# OPTION 1 : Drop all the missing values 
ufo.shape

ufo.dropna(how='any').shape   # This simpply meansdrop all the rows where any value of column is NaN
ufo.shape # Because we didnt put inplace =True here

ufo.dropna(how='any',inplace=True)
ufo.shape

ufo.dropna(how='all').shape # Here all means drop the row in which all the values are false

# We can also pass multiple columns 
ufo.dropna(subset=['City','Shape Reported'] , how='any')
# this means drop all the rows where any of the City or Shape Reported is NaN 
ufo.dropna(subset=['City','Shape Reported'] ,how='all')
# This means drop the row where both City and Shape Reported are NaN




# OPTION 2: filling the NaN values : Using fillna()
ufo['Shape Reported'].value_counts() # Gives frequency of various Shapes
# What we can do is , we can replace all the NaN by a specific Shape !
ufo['Shape Reported'].fillna(value='VARIOUS',inplace=True)

ufo['Shape Reported'] .value_counts() 