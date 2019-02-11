
# coding: utf-8

# In[23]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
get_ipython().magic('matplotlib inline')


# In[42]:

def mean_num_friends(x):
    return str(np.mean(x))

def median_num_friends(x):
    return str(np.median(x))

num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
num_friends = np.array(num_friends)


print("mean="+mean_num_friends(num_friends))

print("median="+median_num_friends(num_friends))


# In[ ]:




# In[ ]:




# In[ ]:




# In[41]:




# In[ ]:




# In[ ]:



