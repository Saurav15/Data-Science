# In Lec_13 we will see :
#          How do i explore pandas seris ? 

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head(2)

movies.dtypes

# Here we will deal with genre and duration 

movies.genre.describe() 
# The describe method shows much info but there is one another method which we can use 
# We can use value_count() method to count different geners

movies.genre.value_counts()

# Now what if we dont need these count .. what we need is the percentage ! i.e what is percentage of each genre type
movies.genre.value_counts(normalize=True)


# We can see that the output of the movies.genre.value_counts() is a seris ... so we can apply all the seris methods to it.
#eg: 
type(movies.genre.value_counts()) # type is seris
movies.genre.value_counts().head() # So we can use seris methods as head() etc..




# We can also see all the unique values by using:
movies.genre.unique() # gives all unique genre's

# We can also find the number of unique values in a column by:
movies.genre.nunique()



# One more important aspact to get the data is using: crosstab 
pd.crosstab(movies.genre,movies.content_rating)




# Now lets work on duration column for a bit
movies.duration.describe()

# we can also use value_count for the duration column 
movies.duration.value_counts()