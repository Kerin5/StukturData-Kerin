#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value =value
        self.ratio = value / weight


# In[7]:


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse = True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        if usedCapacity == capacity:
            break
    print("Total value obtained: "+str(totalValue))


# In[8]:


item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]


# In[9]:


knapsackMethod(cList, 50)


# In[ ]:




