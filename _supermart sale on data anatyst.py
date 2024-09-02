#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[20]:


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 


# In[2]:


df=pd.read_csv("archive (3).zip")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


df.isnull().sum()


# In[10]:


df.duplicated()


# In[11]:


df.describe()


# In[12]:


df1=df.groupby("Product line")["Quantity"].count().reset_index()
df1


# In[18]:


df2=df.groupby("Branch")["Total"].sum().reset_index()
df2


# In[21]:


sns.barplot(y="Quantity",x="Product line",data=df1)
plt.show()


# In[43]:


co=df[["Rating","Total","Tax 5%","cogs","Unit price"]]
co2=co.corr()
print(co2)


# In[44]:


sns.heatmap(co2,annot=True,cmap="winter_r")
plt.show()


# In[ ]:




