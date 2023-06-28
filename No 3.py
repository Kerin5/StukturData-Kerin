#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    def dfs(self, vertex):
        visited = [vertex]
        path = [vertex]
        while path:
            popVertex = path.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    path.append(adjacentVertex)


# In[4]:


customDict = {"A":["C","D","B"],
              "B":["J"],
              "C":["G"],
              "D":[],
              "E":["F","A"],
              "F":["I"],
              "G":["D","H"],
              "H":[],
              "I":[],
              "J":[],
             }

g = Graph(customDict)
print("A", "J")


# In[ ]:




