#!/usr/bin/env python
# coding: utf-8

# # Challenge 2: Count Commits
# 
# Count how many commits were made in the past week.
# 
# Obtain all the commits made in the past week via API, which is a JSON array that contains multiple commit objects.
# 
# Count how many commit objects are contained in the array.

# ⚠️ **Remember to limit your output before submission**.

# In[1]:


import os
from dotenv import load_dotenv
import re
import pandas as pd
load_dotenv()
import json
import requests as req


# In[2]:


commits = 'https://api.github.com/repos/Ironhack-Data-Madrid-Agosto-2022/3.4-lab-mongo/commits'


# In[3]:


req.get(commits)


# In[4]:


com=req.get(commits).json()


# In[5]:


pdcom=pd.DataFrame(com)


# In[6]:


com


# In[7]:


com = requestGithub(commits)


# In[8]:


num_com = 0
com_lst = []
for i in range(len(com)):
    if com[i]['commit']['author']['date'] > '2022-08-22T00:00:00Z':
        com_lst.append(com[i]['commit']['author']['date'])
        num_com += 1

num_com, com_lst


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




