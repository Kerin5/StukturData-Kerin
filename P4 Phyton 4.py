#!/usr/bin/env python
# coding: utf-8

# In[1]:


myDict = {'name':'Edy','age': 26}
myDict['address'] = 'London'
print(myDict)


# In[2]:


# Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
        
traverseDict(myDict)


# In[4]:


# Searching a dictionary


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'The value does not exist'
print(searchDict(myDict, 26))


# In[5]:


# Sorted method
myDict = {'eoooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))


# In[6]:


print(myDict)


# In[7]:


myDict.clear()


# In[8]:


print(myDict)


# In[10]:


myDict = {'name': 'Edy', 'age': 26}


# In[11]:


print(myDict)


# In[13]:


dict = myDict.copy()


# In[14]:


print(dict)


# In[15]:


newDict = {}.fromkeys([1,2,3], 0)
print(newDict)


# In[16]:


print(myDict.get('city', 26))


# In[18]:


print(myDict.get('city', 27))


# In[19]:


print(myDict.get('city'))


# In[20]:


print(myDict.items())


# In[21]:


print(myDict.keys())


# In[22]:


print(myDict.values())


# In[23]:


print(myDict.popitem())


# In[24]:


print(myDict)


# In[25]:


print(myDict.setdefault('name', 'added'))


# In[26]:


print(myDict)


# In[27]:


print(myDict.setdefault('name1', 'added'))


# In[28]:


print(myDict)


# In[29]:


print(myDict.pop('name1', 'not'))


# In[30]:


print(myDict)


# In[31]:


newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)

