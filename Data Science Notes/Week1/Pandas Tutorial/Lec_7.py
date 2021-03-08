# Lec_7 is all about :
# How to filter rows of a pandas dataFrame Library

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

#print( movies.head() )

# Now we can even filter the data by : Like i only need the rows which have duration of play greater then 2hrs i.e 120 min

# First lets see how we can do it with a for loop using boolen list 
booleans =[]
for values in movies.duration :
    if values > 200:
        booleans.append(True)
        print()
    else:
        booleans.append(False)

p=0
for i in booleans:
    if p < 10:
        if i == True:
            print( movies[p:p+1])
    
    p+=1

print('Done!!')


# This was using the basic for loop !

# we can bit ease the above method by using this method :
# Here step one is similar i.e get a list which satisfy the condition
# Step 2 : WE can directly print the movies list in which the dduration is > 200 min by :

print( movies[booleans])  # The output us same !!

# Because it only print the values whose values are True




# This was the long method to get the result that we wanted !
# But of course we are not going to use all these for loops in the real world

# We can just do it in 2 Simple lines by :

booleans = movies.duration > 200
movies[booleans]
# IN python 5>=4    OUT: True
# Similarly in movies.duration>200 Python knows that duration is a seris and returns a list of true and false whic we store in booleans


# We can also reduce a step in this by directly passing our requirement in movies
movies[movies.duration > 200]




# Now what if we dont wanna display all the columns of the table but instead we just wanna display a single column e.g genre
movies[movies.duration > 200].genre
# OR
movies[ movies.duration > 200 ]['genre']

# we can even add the columns 
movies[ movies.duration > 200 ]['genre']



# We can also do this by loc()
movies.loc([movies.dutarion > 200] , 'genre' )

# Also we can add multiple columns 
movies.loc([movies.dutarion > 200] , ['genre' , 'title'] )

# The loc method is the most used then others .