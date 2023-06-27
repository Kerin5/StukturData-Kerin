#!/usr/bin/env python
# coding: utf-8

# In[1]:


newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')
print(newTuple)


# In[2]:


print(newTuple)


# In[4]:


# Access Tuple elements

print(newTuple[0])


# In[5]:


# Traverse through tuple

for i in newTuple:
    print(i)


# In[6]:


for index in range(len(newTuple)):
    print(newTuple[index])


# In[7]:


# How to search for an element in Tuple?

print('a' in newTuple)


# In[8]:


def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newTuple, 'a'))


# In[9]:


# Tuple Operstion / Funcitions
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

print(myTuple + myTuple1)


# In[10]:


print(myTuple * 4)


# In[11]:


print(2 in myTuple1)


# In[12]:


myTuple1.count(2)


# In[13]:


myTuple1.index(2)


# In[14]:


x, y, z = (10,15,20,25,30,35,40)[1::2]
print(x,y,z)


# In[15]:


x = 3
y = -6

x, y = (y, x)[::-1]
print(x, y)


# In[ ]:




