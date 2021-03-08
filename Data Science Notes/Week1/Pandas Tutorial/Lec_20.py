# In lec_20 we will see :
#       How to work with dates and times in pandas ? 

import pandas as pd
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.head()

# What if i want to analyze these sightings by year or by time of day 

# Lets chech the dtypes 
ufo.dtypes # We can see that time is object ! Which means its of type string 

# But what we will do is , we will convert this Time column to pandas special Date-Time column
# to_datetime is a top level function

ufo['Time'] = pd.to_datetime( ufo.Time ) # We will overwrite it with the orignal Time column 

ufo.dtypes # Dtype of the ufo.Time is datetime64

# So what are the advantages of using datetime ? 

ufo.Time.dt.hour # it gives us just the hours ! 

ufo.Time.dt.weekday_name # It gives us the names of days just by looking at the dates given !
ufo.Time.dt.weekday # same as above but just the number version of it

ufo.Time.dt.dayofyear # Gives us what day is it out of 365 days 

ufo.Time.dt.time
ufo.Time.dt.year
ufo.Time.dt.month
ufo.Time.dt.week
ufo.Time.dt.daysinmonth



# now lets pass a string instead of seris in the to_datetime() :
ts = pd.to_datetime('1/1/1999') # it gives us the time stamp 

# Now lets see a real usecase of this 
ufo.loc[ ufo.Time>=ts , : ] # so we can use it in comparision 

# We can also do math with datetime !

ufo.Time.max() # It will gives the latest timestamp im time seris

# We can also subtract two datetime object 

ufo.Time.max() - ufo.Time.min() # It will show us that how many days have been since first entry and the last entry
# Output is time delta objects . we can also pull more things like:
(ufo.Time.max() - ufo.Time.min() ).days # TIme delta object 




