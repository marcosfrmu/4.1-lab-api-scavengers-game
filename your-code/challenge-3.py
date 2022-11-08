#!/usr/bin/env python
# coding: utf-8

# # Challenge 3: Hidden Cold Joke
# 
# Using Python, call Github API to find out the cold joke contained in the 24 secret files in the following repo:
# 
# https://github.com/ironhack-datalabs/scavenger
# 
# The filenames of the secret files contain .scavengerhunt and they are scattered in different directories of this repo. The secret files are named from .0001.scavengerhunt to .0024.scavengerhunt. They are scattered randomly throughout this repo. You need to search for these files by calling the Github API, not searching the local files on your computer.
# 
# 
# After you find out the secrete files:
# 
# Sort the filenames ascendingly.
# 
# Read the content of each secret files into an array of strings.
# 
# Concatenate the strings in the array separating each two with a whitespace.
# 
# Print out the joke.

# ⚠️ **Remember to limit your output before submission**.

# In[1]:


import os
import base64
from dotenv import load_dotenv
import re
load_dotenv()
import json
import requests


# In[2]:


url = 'https://api.github.com/repos/ironhack-datalabs/scavenger/contents?extension:scavengerhunt'


# In[3]:


asd = requests.get(url) 


# In[ ]:




