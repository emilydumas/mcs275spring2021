#!/usr/bin/env python
# coding: utf-8

# # urllib examples
# 
# ## MCS 275 Spring 2021 - Instructor Emily Dumas
# 
# ### Lecture 39

# Some APIs to try:
# ```
# http://roll.diceapi.com/json/d6
# http://roll.diceapi.com/json/3d12
# https://cat-fact.herokuapp.com/facts/random?amount=2
# https://api.fda.gov/drug/label.json?search=_exists_:boxed_warning+AND+effective_time:20210101+TO+20210419
# https://api.exchangerate-api.com/v4/latest/USD
# ```
# 
# Some URLs to scrape (always taking care to limit request volume and follow terms of service!)
# 
# ```
# https://catalog.uic.edu/ucat/academic-calendar/
# https://www.dumas.io/teaching/2020/fall/mcs260/
# https://mathoverflow.net/
# ```

# ## API request example

# In[3]:


import json
from urllib.request import urlopen

with urlopen("https://www.boredapi.com/api/activity") as response:
    data_bytes = response.read() # returns the body
    data = json.loads(data_bytes)
print("Maybe you could... ",data["activity"])


# In[4]:


data


# ## Web page example

# In[10]:


from urllib.request import urlopen

with urlopen("https://example.com/") as response:
    html = response.read()
    charset = response.headers.get_content_charset()
    htmlstr = html.decode(charset)


# In[12]:


print(htmlstr)


# Note: HTML documents often reference other resources needed to display them properly (e.g. CSS stylesheets, images, ...).  This request only gives the HTML.
