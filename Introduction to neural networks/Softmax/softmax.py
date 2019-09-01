#!/usr/bin/env python
# coding: utf-8

# In[1]:


def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result


# In[ ]:




