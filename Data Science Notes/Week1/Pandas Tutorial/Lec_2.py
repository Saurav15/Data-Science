#Lec_2 is about :
# How do i select a pandas seris from a dataFrame

# What is seris in pandas ?? The columns in pandas is calles seris.

# SO lets see 

import pandas as pd

# Data set that we are gon=ing to use today is UFO siting from 1933 to 2000
#ufo = pd.read_table("http://bit.ly/uforeports") 
# as we can see that in the data the column are seperated by "," soo ..
ufo = pd.read_table("http://bit.ly/uforeports",sep=",")
print(ufo.head())

# We can alos use the method pd.read_csv("saf3@#") 
# The only difference between the read_csv & read_ table is csv by default seprates columns using "," while read_table uses TAB as default separator

# Now lets conform that the data we ahve is in the form of DataForm 
type(ufo)




# Now lets select a specific column or say seris
print( ufo['City'] )

# We can also confirm that this is the seris 
type(ufo['City']) # Here this lsit is case Sensitive  i.e city !=  City

# There is also a shortcut to this 
ufo.City  # this will give same output asa above line

# NOTE :- this "." notation doesnt work if theere is a space in the name of the attribute
# Eg. ufo.Colors Reported      ufo.Colors_Reported     All gives error here we have to use ufo['Color Reported']







# Q : How to add a new column in the existing dataframe ?? 

# eg. we need a column which displays both state and city and add it to the existing dataframe :
ufo['Location'] = ufo.City + "," + ufo.State # same as the string

# the new column is added to the ufo dataframe object
print( ufo.head() )




