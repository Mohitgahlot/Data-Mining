
# coding: utf-8

# In[27]:

import math
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')


# In[28]:

def normal_pdf(x, mu=0, sigma=1):
    # TODO
    # hits: math.exp
    ans = (1/math.sqrt(2*3.14*(sigma*sigma))*math.exp((-1*((x-mu)*(x-mu))/(2*sigma*sigma))))
    return ans


# In[31]:

xs = [x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()
from pylab import rcParams
rcParams['figure.figsize'] = 10, 6


# In[ ]:




# In[ ]:



