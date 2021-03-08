# Lec_4 is about :
# How do i rename columns in pandas dataframe ?

import pandas as pd

# we are using UFO dataset

ufo = pd.read_csv("http://bit.ly/uforeports")
print( ufo.head() )

# NOW if we only want to look at column names we dont need head method !! 
# We can do it by using columns attribute

print( ufo.columns )


# now how can i change the name of the column ?
# Consider we need to change the name of the Colors Reproted and Shape Reported such that they dont contain space in between

ufo.rename( columns = {'Colors Reported':'Colors_Reported','Shape Reported':'Shape_Reported'} , inplace = True)
# here inplace means we need to effectively make changes in ufo object 

# Lets check : 
print( ufo.head() ) 



# What if we need to change all of the column names ? Here column.rename will be too long
# we can do it by : 
ufo_cols = ['city' , 'colors_reported','shape_reported','state','time']
ufo.columns = ufo_cols
print(ufo.columns)


# we can also change the names of the column while importing the data 
ufo_cols = ['city' , 'colors_reported','shape_reported','state','time']
ufo = pd.read_csv("http://bit.ly/uforeports" , names=ufo_cols , header=0) 
# Here the header = 0 means that the row no.0 has the name of all columns and we need to replace new names with header= 0  



# NOTE :- (Bonus_Tip) Now suppoes we have many columns in our data set and many of them have spaces in between then !
          # we cannot replace all columns spaces by _ one by one !!

# we can do it all at once by this method : 
print( ufo.columns )

ufo.columns = ufo.columns.str.replace(' ','_')
print( ufo.columns )