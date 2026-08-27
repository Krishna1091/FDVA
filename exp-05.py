#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Sales': [120, 150, 170, 160, 210, 240, 220, 280, 310, 350],
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'A']
}
df = pd.DataFrame(data)
np.random.seed(42)
df_customers = pd.DataFrame({
    'Customer_Age': np.random.normal(loc=35, scale=8, size=500).astype(int)
})


# In[3]:


plt.figure(figsize=(7, 4))
plt.plot(df['Day'], df['Sales'], color='blue', marker='o', linestyle='-', label='Sales')
plt.xlabel('Day')
plt.ylabel('Sales ($)')
plt.title('Line Plot: Daily Sales Over Time')
plt.grid(True)
plt.legend()
plt.show()


# In[4]:


category_counts = df['Category'].value_counts()
plt.figure(figsize=(7, 4))
plt.bar(category_counts.index, category_counts.values, color='orange', edgecolor='black')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.title('Bar Plot: Product Category Counts')
plt.show()


# In[5]:


plt.figure(figsize=(7, 4))
plt.hist(df_customers['Customer_Age'], bins=15, color='purple', edgecolor='black')
plt.xlabel('Customer Age')
plt.ylabel('Frequency')
plt.title('Histogram: Customer Age Distribution')
plt.show()


# In[ ]:




