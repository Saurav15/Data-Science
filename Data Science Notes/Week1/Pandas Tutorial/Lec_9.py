# Lec_9 is about : 
#       How do i use axis parameter in Pandas

import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head(2))

# Lets remove the continent column  !

drinks.drop(['contient'],axis=1) # Dropping columns

drinks.drop( 1 , axis=0) # Drooping rows


# Now lets see the use of axis parameter in different method

# Lets finad the mean

drinks.mean()
#This method does the column mean !  By default . 

#  But waht if we need mean of rows ? 
#Axis = 0 means moving down 
# Axis = 1 means moving side ways! 

drinks.mean(axis=1) # Gives mean of all rows
drinks.mean(axis=0) # Gives mean of all columns



# NOTE : We can replace the axis = 0 with axis ='index'
# and axis=1 with axis='columns'

drinks.mean(axis='columns')
drinks.mean(axis = 'index')