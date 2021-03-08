# What is numpy ?
# NumPy is a general-purpose array-processing package. 
# It provides a high-performance multidimensional array object, and tools for working with these arrays. 
# It is the fundamental package for scientific computing with Python.

import numpy as np

# creating 1-D array 
a = np.array([10,20,34]) # array created with 3 elements with index 0,1,2

# accessing 1-D array 
print(a[0]) 
print(a[1]) 
print(a[2])


# Creating 2-D array 
b = np.array([[2,3,5,7],[23,65,32,12]])

 # Accessing 2-D array
print(b[0][1])
print(b[1][2])



# We can also know what is the dimention of the given array
print( b.ndim ) # gives the dimention of b
print( a.ndim ) # gives the dimention of a

# In order to check the data type of the given array
print( b.dtype )

# Itemsize tells us about the size of the given array data type
print( b.itemsize )



# How to get the total number of elements in the array ?
# To know the total number of elements in the array we use size
print( a.size )
print(b.size) # gives the total number of elements 


# While using multidimentional arrays we can also get the no. of rows and column of an array 
#eg. 
a = np.array([[2,43,5,6],[2,5,45],[453,54,2,1,6]])
print(a.shape) # here as columns are not same for all the rows it will not show column

a = np.array([[2,3,4],[2,34,54],[7,6,5],[34,65,1]])
# Here no. of rows are 4 and columns are same foe every row i.e 3
print(a.shape)
print(a)




# If we need to initialize an array with a specific datatype irrespect to the
# Elements present in it ... It can be done as followes

a=np.array([[1,2,3],[2,3,4],[34,65,56]],dtype=float)
print(a)
# we can alslo initialize it to complex numbers
a=np.array([[1,2,3],[2,3,4],[34,65,56]],dtype=complex)
print(a)



# Sometimes we need to initialize array with ones or zeros 
np.zeros( (3,4) ) # it creates an array of 3 rows and 4 column 
# but inorder to use it we have to save it in some variable
p = np.zeros( (3,4))
print(p)

# Same thing can be done with ones
p = np.ones((3,4))
print(p)


c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #    







# We use range() function in order to create list of continious numbers
# We use range() in python
l = range(2,6)
print(l[0])
print(l[1])

# Alos we can use range() not only to print seris of numbers but can also use it to print numbers with uniform gap
# Eg. i need to print the seris of numbers with the interval of 3
p = range(0,10,3)
print(p[0] , p[1] , p[2] , p[3])




#We can also use similar function in numpy using arange
q = np.arange(0,5)
print(q) 

# We can also have the numbers with specific interval
q = np.arange(0,9,4) # numbers from 0 to 9 in interval of 4
print(q)





# We can also generate linearly spaced numbers between the given numbers
q = np.linspace(0,20,10)  # This means create linearly spaces 10 numbers within 0 to 19
print(q)




# Before we have seen how we can get the shape of the array
p = np.array([[2,3,4,2],[2,67,45,12],[5,8,12,9]])
print(p.shape) # to get the rows and column of the array

# We can also change the shape of the array using np.reshape

print( p.reshape(3,4) )

# we can also flattern th array using ravel function

print( p.ravel() ) # only one tuple ! i.e 1-D array conversion











# Some MATHAMATICAL FUNCTIONS in NUMPY
p = np.array([[2,3,4,2],[2,67,45,12],[5,8,12,9]])

# Finding minimum and maximum in the array
print( p.min() )
print( p.max() )

# Finding SUM of all the numbers
print( p.sum() )

# AXIS : axis0 represent column & axis1 represent rows
# Tis is used when we need sum of rows and columns
print( p.sum(axis=0) ) # gives a list with sum of all the columns ... Has size 4 as there are 4 columns
print( p.sum(axis=1) ) # gives a list with sum of all the number in rows ... Has size 3 as there are 3 rows


# we can also find square root of all the numbers using numpy sqrt method
w = np.sqrt(p)
print(w)



# STANDARD DEVIATION 
# we can also find standard deviation using numpy
print( np.std(p) ) # Gives the standard deviation of array p







# Now lets see some operation between arrays
a = np.array([[2,3,4],[1,2,3]])
b = np.array([[1,2,3],[5,6,7]])

# Here basically these 2-D arays are matrices , so we are doing all these matrix operations !

# Adding 2 arrays
sum = a + b
print(sum) 
# WE CANNOT DO ALL SUCH OPERATIONS ON LIST ... THEY CAN ONLY BE DONE IN ARRAYS

# Multiplying 2 arrays
mul = a*b
print(mul)

#Dividing 2 arrays
div = a/b
print(div)

# we can also do dot product 
dot_p= a.dot(b)
print(dot_p)


# Taking transpose 
x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"




# Broadcasting
# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.

#For example, suppose that we want to add a constant vector to each row of a matrix. 

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)


