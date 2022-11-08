#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import numpy as np
import pandas as pd
import requests


# Only if you're using your environmental variable eith the `.env` file, import/install the following modules. Otherwise it is not necessary:
# 
# https://pypi.org/project/python-dotenv/

# In[2]:


get_ipython().run_line_magic('pip', 'install python-dotenv')


# In[3]:


from dotenv import load_dotenv


# In[4]:


#pip install python-dotenv


# In[5]:


load_dotenv()


# In[6]:


github = os.getenv("token")


# # Challenge 1: Fork Languages
# 
# You will find out how many programming languages are used among all the forks created from the main lab repo of your bootcamp. Assuming the main lab repo is ironhack-datalabs/datamad1020-rev, you will:
# 
# 1. Obtain the full list of forks created from the main lab repo via Github API.
# 
# 2. Loop the JSON response to find out the language attribute of each fork. Use an array to store the language attributes of each fork.
# 
# Hint: Each language should appear only once in your array.
# 
# 3. Print the language array. It should be something like:
# 
# ["Python", "Jupyter Notebook", "HTML"]
# 

# **HINT:**: Create a list with every **language_url** you find in every fork 

# ⚠️ **Remember to limit your output before submission**.

# In[7]:



import requests as req

url="https://api.github.com/repos/Ironhack-Data-Madrid-Agosto-2022/3.4-lab-mongo/forks"

req.get(url)


# In[8]:


api_data=req.get(url).json()


# In[9]:


req.get(url).text[:500]


# 

# In[10]:


import pandas as pd

asd = pd.DataFrame(api_data)


# In[11]:


asd.head().T


# In[12]:


langua=[]
for i in range(len(api_data)):
    ap=api_data[i]['language']
    if ap not in langua:
        langua.append(ap)
print(langua)


# In[ ]:




