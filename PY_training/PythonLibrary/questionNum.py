import numpy as np


#Q1  Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

# arr = np.array([12.23, 13.32, 100, 36.32])
# temp = arr
# print("\n",temp)






#Q2 Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]

# arr = np.arange(2,11).reshape(3,3)
# print(arr)






#Q3 Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
# arr = np.array([ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.])

# arr= np.zeros(10)
# arr[5] = 11
# print(arr)








#Q4 Write a NumPy program to reverse an array (the first element becomes the last).
# Original array:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
# Reverse array:
# [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]

# arr = np.array([12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20, 21 ,22 ,23 ,24, 25 ,26, 27, 28, 29, 30, 
# 31, 32, 33, 34, 35, 36, 37])
# temp = arr[::-1]
# print("\n",temp)








#Q5 Write a NumPy program to convert an array to a floating type.
# Sample output:
# Original array
# [1, 2, 3, 4]

# Array converted to a float type:
# [ 1. 2. 3. 4.]
# arr = np.array([ 1, 2, 3, 4,])
# arr = np.array([1,2,3,4],dtype='float')
# print(arr)









#Q6 Write a NumPy program to create a 2D array with 1 on the border and 0 inside.
# Expected Output:
# Original array:
# [[ 1. 1. 1. 1. 1.]
# ...................
# [ 1. 1. 1. 1. 1.]]

# 1 on the border and 0 inside in the array
# [[ 1. 1. 1. 1. 1.]
# ...................
# [ 1. 1. 1. 1. 1.]]


# Define the size of the array
rows, cols = 5, 5  # You can adjust this size

# Create an array of ones
array = np.ones((rows, cols))

# Set the inner values to zero
array[1:-1, 1:-1] = 0

print("Original array:")
print(array)













#Q7 Write a NumPy program to add a border (filled with 0's) around an existing array.

# Expected Output:

# Original array:
# [[ 1. 1. 1.]
# [ 1. 1. 1.]
# [ 1. 1. 1.]]

# 1 on the border and 0 inside in the array
# [[ 0. 0. 0. 0. 0.]
# ...........
# [ 0. 0. 0. 0. 0.]]
row , col = 5,5
arr = np.zeros((row,col))
arr[1:-1,1:-1]=1
print("oroginal array")
print(arr)







#  .............................................  MORE QUESTION.........................................



# # Q1- Write a NumPy program to convert a list and tuple into arrays.
# # List to array:
# # [1 2 3 4 5 6 7 8]
# # Tuple to array:
# # [[8 4 6]
# # [1 2 3]]

# a = np.array([1, 2 ,3 ,4 ,5 ,6 ,7 ,8])
# b=np.array([[8,4,5],[1,2,3]])
# a = np.arange(1,9).reshape(2,3)
# print(a)
# print(b)










# # Q2- Write a NumPy program to create an empty and full array.
# # Expected Output:

# # [ 6.93270651e-310 1.59262180e-316 6.93270559e-310 6.93270665e-310]
# # [ 6.93270667e-310 6.93270671e-310 6.93270668e-310 6.93270483e-310]
# # [ 6.93270668e-310 6.93270671e-310 6.93270370e-310 6.93270488e-310]]
# # [[6 6 6]
# # [6 6 6]
# # [6 6 6]]

# arr = np.random.random((6,6))
# arr = np.empty(12)
# print(arr)
# c = np.full((3,3),6,dtype='int')
# print(c)










# # 3- Write a NumPy program to find the real and imaginary parts of an array of complex numbers.
# # Expected Output:
# # Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
# # Real part of the array:
# # [ 1. 0.70710678]
# # Imaginary part of the array:
# # [ 0. 0.70710678]

# arr = np.array([ 1.00000000+0.j, 0.70710678+0.70710678j])
# r = np.real(arr)
# print(r)
# i = np.imag(arr)
# print(i)

# second method
# x = np.sqrt([1+0j])
# y = np.sqrt([0+1j])
# print(x)
# print(y)
# print(np.real(x))
# print(np.imag(y))













# 4- Write a NumPy program to find the number of elements in an array. It also finds the length of one 
# array element in bytes and the total bytes consumed by the elements.
# Expected Output:
# Size of the array: 3
# Length of one array element in bytes: 8
# Total bytes consumed by the elements of the array: 24


# Creating a NumPy array
arr = np.array([10, 20, 30])

# Finding size, item size, and total bytes consumed
size = arr.size  # Number of elements
item_size = arr.itemsize  # Size of one element in bytes
total_size = arr.nbytes  # Total bytes consumed

# Displaying results
print("Size of the array:", size)
print("Length of one array element in bytes:", item_size)
print("Total bytes consumed by the elements of the array:", total_size)












# 5- Write a NumPy program to test whether each element of a 1-D array is also present in a second array.
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [0, 40]
# Compare each element of array1 and array2
# [ True False False True False]


# Define arrays
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])

# Check if elements of array1 are in array2
result = np.isin(array1, array2)

# Display results
print("Array1:", array1)
print("Array2:", array2)
print("Compare each element of array1 and array2:")
print(result)













# 6- Write a NumPy program to find common values between two arrays.
# Expected Output:
# Array1: [ 0 10 20 40 60]
# Array2: [10, 30, 40]
# Common values between two arrays:
# [10 40]



# Define arrays
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

# Find common values
common_values = np.intersect1d(array1, array2)

# Display results
print("Array1:", array1)
print("Array2:", array2)
print("Common values between two arrays:")
print(common_values)












# 7- Write a NumPy program to get the unique elements of an array.
# Expected Output:
# Original array:
# [10 10 20 20 30 30]
# Unique elements of the above array:
# [10 20 30]
# Original array:
# [[1 1]
# [2 3]]  
# Unique elements of the above array:
# [1 2 3]


# 1D Array
array1 = np.array([10, 10, 20, 20, 30, 30])
unique_elements1 = np.unique(array1)

# 2D Array
array2 = np.array([[1, 1], [2, 3]])
unique_elements2 = np.unique(array2)

# Display results
print("Original array:")
print(array1)
print("Unique elements of the above array:")
print(unique_elements1)

print("\nOriginal array:")
print(array2)
print("Unique elements of the above array:")
print(unique_elements2)
