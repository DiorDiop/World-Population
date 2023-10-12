#!/usr/bin/env python
# coding: utf-8

# In[29]:


# import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[30]:


data = pd.read_csv(r"D:\Dior\000_Code\000_Portfolio\11_World Population\world_population.csv")
data


# In[31]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[32]:


# Data type information
data.info()


# In[33]:


# Brief description to have the Count, Mean, std, percentile(min, 25%, 50%, 75%) and max
data.describe()


# In[34]:


# See if we have any missing values
data.isnull().sum()


# In[35]:


# See how many unique values do we have
data.nunique()


# In[36]:


# Sort values by="2022 Population"
data.sort_values(by="2022 Population", ascending=False).head(10)


# In[37]:


# See the correlations(how closelly correlated they are)
data.corr()


# In[64]:


# Visualize a heatmap
sns.heatmap(data.corr(), annot = True)

# Change the parameter
plt.rcParams['figure.figsize'] = (15,5)

plt.show()


# In[42]:


# Output the mean of any Continent
data.groupby('Continent').mean().sort_values(by="2022 Population", ascending=False)


# In[27]:


# Search a specific value(Oceania)
data[data['Continent'].str.contains('Oceania')]


# In[68]:


# Sort by Continent sort by "2022 Population" and only output the populations
df = data.groupby('Continent')[['1970 Population', '1980 Population', '1990 Population',
       '2000 Population', '2010 Population', '2015 Population',
       '2020 Population', '2022 Population']].mean().sort_values(by="2022 Population", ascending=False)
# Another version
# df = data.groupby('Continent')[data.columns[5:13]].mean().sort_values(by="2022 Population", ascending=False)
df


# In[69]:


# Transpose the Columns and thr Rows titles
df = df.transpose()
df


# In[70]:


# Output the names of the new Columns
df.columns


# In[71]:


df.plot()


# In[73]:


df.boxplot(figsize=(20,10))


# In[ ]:





# In[ ]:




