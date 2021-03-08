# Lec_15 we will learn about : 
#          The indexing in pandas .

import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.head()

# Index is the name of the rows . Lets have look at it :
drinks.index

# Lets also look at the column attribute :
drinks.columns

# the index and the columns are both by default the integers , if no index or columns are specified .
# Lets see by an example 

movies = pd.read_table("http://bit.ly/movieusers",header = None , sep='|')
movies.head()




# So why does the index exists ????
# 1.)  Identification 2.) Selection  3.)Alignment

# 1.) Identification !!

drinks.loc[drinks.continent=='South America',:]
# we can see here that the row labels stayed the same i.e it dident renumbered it !
# this is the reason why we say that the index is for the identification 


# 2.) Selection

# now suppose we need to get the beer servingg of Brazil !! 
drinks.loc[23,'beer_servings'] 
# But we are not going to search what number is brazil !!
# so what we can doo is make the COuntryas an index !

drinks.set_index('country',inplace=True)
drinks.head(2)

drinks.index
# now we can find the beer_servings in brazil easily
drinks.loc['Brazil','beer_servings']


# now we can see that the the name of the index , 'Country' is not looking good right there !
# we can clear the index name by:
drinks.index.name = None
drinks.head()

# we can even ive the index name :
drinks.index.name ='country'
drinks.head()

# we can also reset index back to integers :
drinks.reset_index(inplace=True)
drinks.head()


# lets see this :
drinks.describe()
# We can get the name of the column of the describe
drinks.describe().index # same for column 
# But many times we dont need all the column 
# so we can filter the describe column 

drinks.describe().loc['25%',:]

