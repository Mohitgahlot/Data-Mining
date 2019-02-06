
# coding: utf-8

# In[4]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
get_ipython().magic('matplotlib inline')


# In[ ]:




# In[ ]:




# In[9]:

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]


# In[36]:

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    c = 0
    for f in friendship:
        if user in f:
            c+=1
    s = str(users[user]["name"]) + " has "+ str(c) + " friends"
    return s
num_friends(4)


# In[40]:

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    d = dict()
    
    for f in friendship:
        if f[0] in d.keys():
            d[f[0]]=d[f[0]]+1
        else:
            d[f[0]]=1
        if f[1] in d.keys():
            d[f[1]]=d[f[1]]+1
        else:
            d[f[1]]=1
    d = sorted(d.items(),key= lambda x:x[1])
    print(d)
    print(str(users[d[0][0]]["name"])+" has Min friends")
    print(str(users[d[-1][0]]["name"])+" has Max friends")
sort_by_num_friends()


# In[ ]:



