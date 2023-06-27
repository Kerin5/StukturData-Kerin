#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)


# In[2]:


newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[3]:


print(len(twoDArray))


# In[4]:


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[5]:


print(len(newTwoDArray))


# In[6]:


print(len(newTwoDArray[0]))


# In[9]:


def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:traverseTDArray(twoDArray)
        print(array[rowIndex][colIndex])


# In[10]:


accessElements(newTwoDArray, 1, 2)


# In[11]:


def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# In[12]:


traverseTDArray(twoDArray)


# In[13]:


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'
print(twoDArray)


# In[14]:


print(searchTDArray(twoDArray, 12))


# In[15]:


newTDArray = np.delete(twoDArray, 2, axis=0)
print(newTDArray)


# In[16]:


print(twoDArray)


# In[ ]:




