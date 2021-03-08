# Lec_8 is about :
# How to apply multiple filter criteria to pandas dataframe
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

print( movies.head(2) )

# In last lecture we have seen how to add a specific condition to our DataFrame by:
movies[ movies.duration>200 ]['genre']

# Now we can also add two or more condition by : 
movies[ (movies.duration >200) & (movies.genre == 'Adventure')] # Here the keep in mind the parenthesis
# Also here we use & instead of and

# we can also use or operator
movies[ (movies.duration >200) | (movies.genre == 'Adventure')]



# Now as we know from Lec_7 (movies.duration >200) | (movies.genre == 'Adventure')  returns the list of booleans 
(movies.duration >200) | (movies.genre == 'Adventure') # Will return the list of booleans




# Now we can also add multiple condition as :
movies[ (movies.genre == 'Crime') | (movies.genre == 'Adventure') | (movies.genre == 'Drama') ]

# We can do the same by this : 
movies.genre.isin( ['Crime' , 'Drama' , 'Adventure'] ) # It is same as multiple or statements
# Returns the list of Booleans
movies[(movies.duration >200) & (movies.genre == 'Adventure')]['duration'] 

movies.loc[ (movies.duration >200) & (movies.genre=='Drama'), 'genre']
