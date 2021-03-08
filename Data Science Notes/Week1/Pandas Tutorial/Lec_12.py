# In Lec_12 we will see :
#           When to use Groupby in pandas

import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.head(2)

# Q.) What is the average beer servings across all countries ?

# Here the answer is quite simple :
drinks.beer_servings.mean()

# Q.) What is the avg beer servings per  continent

# We can do it very easily by using groupby method
drinks.groupby('continent').beer_servings.mean()



# WE can also phrase group by as : For each continent do mean of beer_servings



# The mean is not only math function . others are : min() , max() , mean() , count

#WE can do it all at oc=nce by : 
drinks.groupby('continent').beer_servings.agg(['min','max','count','mean'])