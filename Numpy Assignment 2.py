#!/usr/bin/env python
# coding: utf-8

# 1. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10

# In[1]:


#Importing Numpy Library
import numpy as np


# In[2]:


#Setting a random Seed of value 20 to ensure the random numbers are generated each time
np.random.seed(20)


# In[10]:


# Am using the np.random.randint function to generate a vector of length 5 filled with random integers from 0 to 10
myvector = np.random.randint(0, 11, size=5)


# In[11]:


print(myvector)


# 2. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

# In[12]:


# Since we have imported the Numpy library as np already, Create a vector with values ranging from 15 to 55 using the np.arange function
my_vector = np.arange(15, 56)


# In[13]:


# Print all values except the first and last
print(my_vector[1:-1])


# 3. Write a NumPy program to create a random array with 1000 elements and compute the average, variance, standard deviation of the array elements. 

# Since we have imported the Numpy library as np already, no need to import numpy library again

# In[21]:


# Let Create a random array with 1000 elements
myarray = np.random.rand(1000)


# In[22]:


# Let Compute the average, the variance, and the standard deviation and assign them to a variable
the_average = np.mean(arr)
the_variance = np.var(arr)
the_std = np.std(arr)


# In[23]:


# Let Print the results
print("Average:", the_average)
print("Variance:", the_variance)
print("Standard deviation:", the_std)


# 4. Write a NumPy program to calculate cumulative sum of the elements along a given axis, sum over rows for each of the 3 columns and sum over columns for each of the 2 rows of a given 3x3 array. 

# Since we have imported the Numpy library as np already, no need to import numpy library again
# 

# In[26]:


# Let Create a 3x3 array
my_array = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


# In[29]:


# Let Calculate the cumulative sum along the rows using the cumsum function
my_cumsum_rows = np.cumsum(my_array, axis=1)


# In[30]:


# Let Calculate the sum over rows for each column using the np.sum function
my_sum_columns = np.sum(my_array, axis=0)


# In[31]:


# Let Calculate the sum over columns for each row
my_sum_rows = np.sum(my_array, axis=1)


# In[33]:


# We Print the results
print("Array:\n", my_array)
print("Our Cumulative sum along rows:\n", my_cumsum_rows)
print("Our Sum over rows for each column:\n", my_sum_columns)
print("Our Sum over columns for each row:\n", my_sum_rows)


# 5. Write a NumPy program to compute the multiplication of two given matrixes. 
# 
# Sample Matrix: 
# 
# [[1, 0], [0, 1]] 
# 
# [[1, 2], [3, 4]] 

# Since we have imported the Numpy library as np already, no need to import numpy library again

# In[34]:


# Let Create the first matrix
matrix_1 = np.array([[1, 0],[0, 1]])


# In[36]:


# Let Create the second matrix
matrix_2 = np.array([[1, 2],[3, 4]])


# In[37]:


# Let Compute the matrix multiplication using the matmul function
the_result = np.matmul(matrix_1, matrix_2)


# In[38]:


# Let Print the result
print("Result:\n", the_result)


# In[ ]:




