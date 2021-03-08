# Lec_3 is about :
# Why does some pandaas commend ends with parentheses and others dont ??

import pandas as pd

# for this lecture we are going to use Dataset of IMDB rating

movies = pd.read_csv("http://bit.ly/imdbratings") # Contains comma seperated file

print( movies.head() )

print( movies.describe() ) # just trying out some commands

print( movies.shape ) # tells us that there are 979 rows and 6 columns

print( movies.dtypes ) # Tells us the data type of all the columns
 

# we can see here that certain operators end with ( )  while others dont !

# Because here movies is a dataframe object which obviously contains some methods and some variables
# So here the methods are like head and describe and the attribute are the ones without parenthesis

# The methods are action oriented while the attributes are just displaying stuff
# Methods are the one which have optional arguments

print( movies.describe(include=['object'])) # Gives describtion of all the column which are of type object

# Here top = things that came most of the time 
# Freq = How many times are they repeated 




# TIP :- while using jupyter notebook we can see what all argument can a method thake by hitting "shift+TAB" inside the brackets of the methods

    




