#!/usr/bin/env python
# coding: utf-8

# In[15]:


# test_pickled_model.py
import json

with open('newdata.py', 'r') as f:
         newdata = json.load(f)

import pickle

with open('df.pickle', 'rb') as f:
    data = pickle.load(f) # unpickle the pipe...
    
# `model.predict` and friends expect a 2-d array of data. If your newdata is
# one-dimensional, make it two-dimensional by wrapping it in a list.
# numpy can be used to check the number of dimensions of a list.
#    
#    import numpy as np
#    newdata = np.array(newdata)
#    if newdata.ndim == 1:
#        newdata = [newdata]

predictions = data.predict_proba(newdata)
print(predictions)

