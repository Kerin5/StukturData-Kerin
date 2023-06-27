#!/usr/bin/env python
# coding: utf-8

# In[1]:


from multiprocessing import Queue


# In[2]:


customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())

