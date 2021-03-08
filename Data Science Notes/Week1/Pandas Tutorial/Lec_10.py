# In Lec_10 we are going to see :
#       How do i use string methods in pandas

import pandas as pd

# Once just see some basic string methods as upper() ... 

orders = pd.read_table("http://bit.ly/chiporders")
print( orders.head(2) )

# LEts say we need to make the item_name column in capital

# We cannot use String methods like : orders.item_name.upper()
# Instead we need to add the .str
orders.item_name.str.upper()


# Lets look at another method of string
orders.item_name.str.contains('Chicken') # This will give the list of True and False

# We can also print the whole table with rows containing item_name = Chicken
orders[ orders.item_name.str.contains('Chicken') ]


# we  have another string method : Replace
# Consider we need to remove [..dsad..] these "[]" from Choice_description 
orders.choice_description.str.replace('[','')

#Infact we can run two str "seris" method at the same time
orders.choice_description.str.replace('[','').str.replace(']','')