# In Lec_21 we will see : 
#          How to find and remove duplicate rows in pandas ?

import pandas as pd
users = pd.read_table('http://bit.ly/movieusers' , sep = '|' ,  header=None)

users.columns
user_cols = [ 'id' ,'age' , 'gender' ,'occupation' , 'u_id']
users.columns = user_cols

users.set_index( 'id' , inplace = True)
users.head()

# Now lets say we need to identify the duplicate u_id

users.u_id.duplicated() # this will give true if any u_id is present above the repeated row !
users[ users.u_id.duplicated() ]

# we can also count the number of true by using sum() method 
users.u_id.duplicated().sum()

# We can also check if all the columns of which rows are repeated 
users.duplicated().sum()


# we can even watch these duplicated rows by : 
users.loc[ users.duplicated() , : ]


# now lets see how to drop the duplicates from the table
# we use keep='First'  to keep first ones and delete other dupicates 
# keep='Last' to keep last duplicate and delete the first rows that are repeated

# we can drop duplicate by: 
users.drop_duplicates(keep='first')

# now the total number of rows has been deceased by 7



# now in certain case we use only tow columns to identify weather the row is unique or not!
# here for eg. we identify if a row is unique or not by age and u_id both !

users.duplicated( subset = ['age' , 'u_id']).sum()  #So there are 16 rows with same age and u_id

# we can also use drop_duplicates in the same way
users.drop_duplicates( subset = ['age' , 'u_id'])
