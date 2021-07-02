#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import skfuzzy.membership
import numpy as np
from scipy.stats import norm


# # Generalized bell function

# In[11]:


x= np.arange(20)
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
mf=skfuzzy.gbellmf(x,a,b,c)
plt.plot(x,mf)
plt.show()
x=float(input("Enter the element:"))
mem = 1/(1+abs((x-c)/a)**(2 * b))
print("Membership: ", mem)


# # Sigmoid function

# In[9]:


a = float(input("Enter a :"))
c = float(input("Enter c :"))
x=np.arange(20)

sig = skfuzzy.membership.sigmf(x,a,c)
plt.plot(x,sig)
plt.show()
x=float(input("Enter the member : "))
mem= 1/(1+np.exp(-1*a*(x-c)))
print("Membership : ",mem)


# In[ ]:




