#!/usr/bin/env python
# coding: utf-8

# In[1]:


myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)


# In[2]:


def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(myDict)


# In[3]:


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))


# In[4]:


myDict.pop('name')


# In[5]:


print(myDict)


# In[6]:


myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))


# In[7]:


print(myDict)


# In[8]:


myDict.clear()


# In[9]:


print(myDict)


# In[14]:


myDict = {'name': 'Edy', 'age': 26}


# In[13]:


print(myDict)


# In[15]:


dict = myDict.copy()


# In[16]:


print(dict)


# In[17]:


newDict = {}.fromkeys([1,2,3], 0)
print(newDict)


# In[18]:


print(myDict.get('name', 26))


# In[19]:


print(myDict.get('city', 27))


# In[20]:


print(myDict.get('city'))


# In[21]:


print(myDict.items())


# In[22]:


print(myDict.keys())


# In[23]:


print(myDict.values())


# In[24]:


print(myDict.popitem())


# In[25]:


print(myDict)


# In[26]:


print(myDict.setdefault('name', 'added'))


# In[27]:


print(myDict)


# In[28]:


print(myDict.setdefault('name1', 'added'))


# In[29]:


print(myDict)


# In[30]:


print(myDict.pop('name1', 'not'))


# In[31]:


print(myDict)


# In[32]:


newDict = {'a':1, 'b':2,'c':3}
myDict.update(newDict)
print(myDict)


# In[ ]:




