# In this lecture we will see  : 
#           How to change the datatype of pandas seris?

import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry")
print(drinks.head(2))

# So now lets first look at the data types of present column 
drinks.dtypes

# Now lets say we need to convert this beer_servings column to float data type
# So what we do is use seris method : 
drinks.beer_servings.astype(float)

# Now we can also modify the dataframe as:
drinks['beer_servings'] = drinks.beer_servings.astype(float)


# We might wonder why we need this Function ? Is it even used much ?
# Answer is YES . Usually it will be helpful when we read a file and in that file the numbers are strings i.e object type
# There we need to change the data type of that seris in order to do the mathematical operations





# Q) How to define type of each column before actully reading the csv ?
# We have to do it at the time of reading the file

drinks = pd.read_csv('http://bit.ly/drinksbycountry' , dtype={'beer_servings':float})




# Lets understand it better with another example

orders = pd.read_table('http://bit.ly/chiporder')
print( orders.head(2) )

# Now here the item_price column has $2.45 and all .... So what datatype is it an int or a specical char ?
# Lets see
orders.dtype
# So item_name has a object data type 
# So  we cannot perform any maths operation on it !

orders.mean() # Will give an  error

# SO what we can do is :
orders.item_price.str.replace('$' , '')
# Now convert the data type to int
orders.item_price = orders.item_price.astype({'item_price':float})

# Now we can do math
orders.item_price.mean()


