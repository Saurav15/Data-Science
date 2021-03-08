#Lec_5 is all about :
# How to remove column from pandas dataframe

import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.columns = ufo.columns.str.replace(' ','_')
print( ufo.head() )

print( ufo.columns )

# Now here we can note that the Color Rported column is all NaN so we can get rid of it .
# we can do it by using drop method in pandas

ufo.drop('Colors_Reported' , axis=1 , inplace =True)
# Here axis=1 represents the columns 

print( ufo.columns )


# we can also drop multiple columns at the same time 
# Eg. we need to get rid of city and state both

ufo.drop(['City','State'],axis=1,inplace=True)
print( ufo.columns )




# What if we want to remove a row instead of column ? 
ufo.drop([0,2], axis=0 , inplace =True) # 0,2 represents the number of rows that are to be deleted
print( ufo.head() )