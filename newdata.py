#!/usr/bin/env python
# coding: utf-8

# ### Import data from public source and give the dataframe a name

# In[2]:


import pandas as pd
df = pd.read_csv('https://www.openml.org/data/get_csv/44')


# ### Import necessary modules

# In[3]:


from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


# ### Create pipeline

# In[4]:


X, y = make_classification(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    random_state=0)
pipe = Pipeline([('scaler', StandardScaler()), ('svc', LogisticRegression())])

pipe.fit(X_train, y_train)

pipe.score(X_test, y_test)


# ### Import pickle module and pickle the model

# In[5]:


import pickle

with open('df.pickle', 'wb') as f:
    pickle.dump(df, f, pickle.HIGHEST_PROTOCOL)
    
filename = 'model.pkl'
pickle.dump(pipe, open(filename, 'wb'))


# ### Part two seperate out two rows

# In[6]:


df2 = df.iloc[0:2, :]
newdata = df2.values.tolist()
newdata


# In[7]:


import json

with open('newdata.py', 'w') as f:
    json.dump(newdata, f)


# In[8]:


import json

with open('newdata.py', 'r') as f:
    newdata = json.load(f)

