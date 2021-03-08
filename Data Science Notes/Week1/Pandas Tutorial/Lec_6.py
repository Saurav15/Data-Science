# Lec_6 is all about:
# How do i sort a pandas DataFrame or seris ?

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
print( movies.head() )


# there are 2 ways of Sorting one is new other is old 

# New one is : 
movies.title.sort_values()
print(movies.title)

# For the spaced names we cannot use . 
movies['title'].sort_values()
print(movies.title)

# The sorting method returns the values in ascending order by default 
# But we can change it to decending order by :
movies['title'].sort_values(ascending =False)
print(movies)

# The above mentioned syntex sort the title and only displays the title column 
# But what if we need to sort the data by title and display all the columns 
# movies.sort_values('title')
print(movies.sort_values('title'))



# What if we want to sort by 2 values 
#  SOrting by 2 values means First it will sort by the 1 Value passed and now if there is a tie then we will osrt by the 2nd value

movies.sort_values(['duration', 'title' ])
