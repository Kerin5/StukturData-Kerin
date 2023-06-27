#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mod(number, cellNumber):
    return number % cellNumber

def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber


# In[2]:


print(modASCII("ABC", 24))


# In[ ]:




