# In Lec_16 we will see :
#          Indexing part 2 

import pandas as pd
drinks = pd.read_table('http://bit.ly/drinksbycountry',sep=',')
drinks.head()

drinks.set_index('country',inplace=True)
drinks.head()

# Now what if we select the continent seris ?

drinks.continent.head()
# we can see that the index comes from the dataframe 


drinks.continent.value_counts() # It ives the number of rows having same continent column 

# We can actully use index to select values from the seris
drinks.continent.value_counts()['Africa']

# we can also sort the continent by:
drinks.continent.value_counts().sort_values()

# Similerly we can sort the index by :
drinks.continent.value_counts().sort_index()




# Continued from last video :

# 3.) Alignment
# for showing alignment lets make our own Series 
people = pd.Series([3000000,85000],index=['Albania','Andorra'],name = 'population')

# Now we can e=do the math between two tables as:
drinks.beer_servings*people
# Here we can see that many rows shows NaN as they dont have numbers .
# So here the people seris has matched the index and then did the multiplication 
# this is what we call Alignment



# We can even take this people seris and add it inoto the dataframe
pd.concat([drinks,people],axis=1) 

