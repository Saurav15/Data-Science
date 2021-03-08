# Lec_16 is about:
#      How to make Pandas DataFrame smaller and faster ?

import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.head()

# lets use info method to get some information about the DataFrame object
drinks.info() 
# We can see here that last line gives us the memory of our data set (9.1+ KB)
# But we can see that there is the + sign at the end and it means that pandas doesnt count how much memory does the objects take they just check how much memory does the reference variable takes

# we can actully force pandas to count the actual memory occupied by the objects
drinks.info(memory_usage='deep') # 30.4 KB which is more then the double shown in drinks.info()

# We can even figure out how much does each column occupies the space
# We can do this by memory_usage ()  method

drinks.memory_usage() # In bytes 
# these arent the real numbers as pandas doesnt inspect each of the column 
# if we want the real columns we can use deep =True

drinks.memory_usage(deep = True) # Now these are the exact numbers 

# The thing here is the object column can take up lot of space !
# So if there is a large data set then the data frame needs hell lot of space !
# So what we can think of doing is converting this Strings or objects to integer as we know integer occupies lot less space then Strings

# we can see in here continent takes very high amount of space 
# also the total no. of unique values in the continent column is :
drinks.continent.nunique() # Only 6 unique values 

# So waht can we do here is set an int for all the 6 continents eg. 1 means Europe and so onn 
drinks.continent.head()  

# We dont need to do all the stuff by ourself thankfully ! pandas already have a function to do that 
# There is a datatype called category to do it for us 

drinks.continent = drinks.continent.astype('category')
drinks.dtypes 

drinks.continent
# Under the hood these strings are stored as the int 

drinks.continent.memory_usage(deep=True)  # The memory has been reduced from 1255 to 824 Bytes



# We can also see the codes by using cat ( Categorical ) 
drinks.continent.cat.codes # will show us the codes instead of whole strings 
# There are other functions under ".cat" which is same as .str 



# Lets try to repeat it for other object column country
drinks.dtypes
drinks.memory_usage(deep=True) # Country = 12588 BYTES

drinks.country.nunique()
drinks.shape 
# Here we can see that there are 193 different countries for 193 different rows all unique

drinks.country = drinks.country.astype('category')
drinks.country.dtype
drinks.memory_usage(deep=True) # Country = 18094 BYTES

# The memory has been increase as all the countries were unique 
# and now we have a list of all the cuntries and also the list of integers pointing to each country 
# so we must only use the datatype category if there are less unique obejects in the column 




# NOTE : Lets take another example 

df = pd.DataFrame({'ID':[100,101,102,103],'quality':['good','very good' , 'good' , 'excellent']})

df.head()

# What happens if we sort the quality column ?
df.quality.sort_values() # It sorts alphabatically !! 

# But the sorting here that must happen is good then very good then excellent !
# we can do this using catagory !

df.quality = df.quality.astype('category', categories=['good', 'very good','excellent'] , ordered = True)

# Here the magic happens !
df.quality # we have the data type as category and the sorted order too ! 
# So now if we sort the quality column :
df.quality.sort_values() 

# The collest thing of all is : 
# We can now use boolean conditions with these strings
df.loc[ df.quality > 'good']  # :)
