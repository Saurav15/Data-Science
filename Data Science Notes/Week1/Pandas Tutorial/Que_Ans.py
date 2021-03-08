# In Que_Ans we will see answers of some questions: 

import pandas as pd


# Q1.) How can we only import only given columns when we are reading the data ? 
#       Also how can we only import limited rows ? 

# We will use UFO data as example

ufo = pd.read_csv('http://bit.ly/uforeports') 
ufo.columns

# USing bove syntex we imported all the columns and rows but we need only few columns and rows
ufo = pd.read_csv('http://bit.ly/uforeports' , usecols= ['City' , 'State'])
ufo.columns
ufo.shape

# we can also import the limited number of rows :
ufo = pd.read_csv("http://bit.ly/uforeports" , nrows=4)
ufo.shape



# Q2.) What is the best way to drop all non-numeric columns ?

# We will use Drinks data set for this 

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.dtypes


import numpy as np
drinks = drinks.select_dtypes(include=[np.number])
drinks.dtypes