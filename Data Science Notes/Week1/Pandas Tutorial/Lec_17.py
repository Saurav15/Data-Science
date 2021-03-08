# Lec_17 is about : 
#       How do i select different rows and columns from pandas dataset


import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head(2)

ufo.rename({'Colors Reported':'Colors_Reported' , 'Shape Reported':'Shape_Reported'} , axis=1,inplace = True)

ufo.columns

# loc is for selecting things by labels
# loc[ 'what rows i want' , 'what columns i want' ]
ufo.loc[0:3,:]

ufo.loc[: , ['City','State']]
ufo.loc[: , 'City':'State'] # all the columns from City to State 
# ALSO can do like this : 
ufo.head(6).drop('Time',axis=1)


# Another use of Loc
# how to select Oakland from City
ufo[ufo.City=='Oakland']
ufo.loc[ ufo.City=='Oakland'] # same result





# iloc : 
ufo.iloc[1:3 , 1:3] # Exclusive '3' here

ufo.iloc[0:2 , :]



# Couple of Shortcuts :
ufo[['City','State']]   # One way of representing multiple column
ufo.loc[:,['City','State']] # one another way to do the same thing 
# THE LOC IS THE MOST RECOMMANDED ONE TO USE!!

ufo[0:3] # NEVER USE THIS !! it gives first 3 rows



# ix  : used to mix labels and integers 
drinks= pd.read_csv("http://bit.ly/drinksbycountry" , index_col='country')
drinks.head(2)

drinks.ix['Albania',0] # here 0 refers to the 0th positioned column 
drinks.ix[1,'beer_servings'] # here 1 represents the row number
drinks.ix['Albania':'Andorra',0:3]
drinks.ix[0:2,0:2]


# NEVER USE ix ONLY USE LOC[] & ILOC[] ALWAYS !!!!!!

