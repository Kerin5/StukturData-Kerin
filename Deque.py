#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque


# In[4]:


customQueue = deque(maxlen=3)
print(customQueue)


# In[5]:


customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
print(customQueue.clear())
print(customQueue)


# In[ ]:




