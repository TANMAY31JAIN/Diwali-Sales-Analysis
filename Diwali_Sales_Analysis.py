#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries

import numpy as np # helps in working on arrays 
import pandas as pd # help in working on tables(dataframes)
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[29]:


# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[30]:


df.shape


# In[31]:


df.head()


# In[32]:


df.info()


# In[33]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
#inplace means after reomving these 2 colms , df will get updated


# In[35]:



#check for null values
pd.isnull(df).sum()
#df.isnull(df) gives false or true
#df.isnull(df).sum() gives sum of null values


# In[38]:


# drop null values
df.dropna(inplace=True)
df.shape


# In[39]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[40]:


df['Amount'].dtypes


# In[41]:


df.columns


# In[42]:


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})
#but it wont get saved because inplace not used


# In[43]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[44]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ### Gender

# In[15]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

#this for loop is for labels
for bars in ax.containers:
    ax.bar_label(bars)


# In[16]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# In[45]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# *From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men*

# ### Age

# In[47]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[48]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# In[49]:


# plotting a bar chart for gender vs total amount
df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[50]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*

# ### State

# In[53]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)}) # size of chart (width,hieght)
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[54]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# *From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*
# 

# ### Marital Status

# In[56]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(3,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# ### Occupation

# In[57]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[58]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# ### Product Category

# In[25]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[59]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# In[27]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[60]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## Conclusion:
# 
# ### 

# *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# Thank you!
