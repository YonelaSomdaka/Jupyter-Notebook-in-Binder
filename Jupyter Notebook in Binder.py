#!/usr/bin/env python
# coding: utf-8

# # Top Two Large Continents
# **Africa)** Known for rich minerals
# 
# **Asia)** Known for best innovations
# 
# # Some Countries to visit
# **South Africa** Visit Cape Town and Mpumalanga for the best of the country both worlds
# 
# **Greece** Athens is better than santorini for things to do 
# 
# **Ghana** Best dishes in Africa
# 

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[32]:


x=[1,2,3,4,5,6,7,8,9]
y=[1,2,4,5,6,4,6,7,3]
y2=[2,3,2,3,5,7,3,2,7]


# In[33]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_title('plot graph',fontsize=24)

ax.set_xlabel('-----------x axis----------')
ax.set_ylabel('-----------y axis----------')


plt.plot(x,y,label='curve1')
plt.plot(x,y2,label='curve1')

ax.legend()


# In[31]:


99*2


# In[35]:


print("Hello World")


# In[ ]:




