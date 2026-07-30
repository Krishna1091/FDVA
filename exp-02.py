#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.DataFrame({
    "Serial No": [1, 2, 3, 4],
    "Register No": [341, 342, 343, 344],
    "Name": ["Alice", "Bob", "Charlie", "David"]
})

print(df)


# In[6]:


import pandas as pd
df = pd.read_csv(r"C:\Users\HDCO422154\Downloads\people-100.csv")
df.tail()


# In[7]:


df.head()


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


df = pd.read_excel(r"C:\Users\HDCO422154\Downloads\file_example_XLS_10.xls")
df.head()


# In[11]:


df.tail()


# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


import pandas as pd
import sqlite3
df = pd.read_csv(r"C:\Users\HDCO422154\Downloads\people-100.csv")
conn = sqlite3.connect("people.db")
df.to_sql("people", conn, if_exists="replace", index=False)


# In[15]:


result = pd.read_sql_query("SELECT * FROM people;", conn)
print(result.head())
conn.close()


# In[ ]:




