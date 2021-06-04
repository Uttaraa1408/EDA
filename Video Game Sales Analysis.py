#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# #### The dataset contains a list of video games with sales greater than 100,000 copies. 

# ## Importing Libraries
# 
# 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')
import squarify


# ### Read File

# In[2]:


game = pd.read_csv(r'G:\Edu Bridge\Python\DataSets\Video Game Sales\vgsales.csv')


# ### View Data

# In[3]:


game


# ### Size of Dataframe/Series

# In[4]:


game.shape


# ### Information of DataSet

# In[5]:


game.info()


# ### Data Types

# In[6]:


game.dtypes


# ### Column Names

# In[7]:


game.columns


# ### Basic Statistical Details

# In[8]:


game.describe()


# ### Checking for 'na' values

# In[9]:


game.isna()


# ### Sum of 'na' values in all columns

# In[10]:


game.isna().sum()


# ### Replacing 'na' Year with mean value of Year

# In[11]:


mean = game['Year'].mean()
game['Year'].fillna(mean, inplace=True)


# ### Changing Data Type of Year from Float to Int and rounding off

# In[12]:


game['Year'] = game['Year'].astype(int)
game['Year'] = game['Year'].round(decimals = 0)


# ### Top 5 Records

# In[13]:


game.head()


# ### Last 5 Records

# In[14]:


game.tail()


# ### Sorting By Year

# In[15]:


game.sort_values(by=['Year'])


# ###  Greater than Year 2016

# In[16]:


game[game['Year']>2016]


# ### Maximum Of Global_Sales

# In[17]:


game['Global_Sales'].max()


# ### Minimum Of Global_Sales

# In[18]:


game['Global_Sales'].min()


# ### Unique Year values

# In[19]:


game.Year.unique()


# ### Global_Sales by Year

# In[20]:


Year = game.groupby("Year").Global_Sales.sum().sort_values(ascending= False).head(20)
Year.head()


# ### Global_Sales by Name

# In[21]:


Name = game.groupby("Name").Global_Sales.sum().sort_values(ascending= False).head(20)
Name.head()


# ### Top 10 Games with Highest Sales

# In[22]:


plt.figure(figsize= (5,10))
sns.set_style("whitegrid")
a = sns.barplot(Name.values,Name.index)
a.set_xlabel("Global Sales(in million)")
a.set_ylabel("Name of the Game")
a.set_title("Top 20 Games with Highest Sales")


# ### Global_Sales by Publisher

# In[23]:


Publisher = game.groupby(['Publisher']) .agg({'Global_Sales' : 'mean'}).round(decimals = 2).sort_values(by = 'Global_Sales' , ascending= False).head(10)
Publisher


# ### Top 10 Publishers with Highest Sales

# In[24]:


plt.figure(figsize= (20,8))
sns.set_style("whitegrid")
sns.set(font_scale = 1.01)  
squarify.plot(sizes=Publisher['Global_Sales'], label=Publisher.index, alpha=0.8 )
plt.axis('off')
plt.show()


# ### Sales by Genre for North America(NA) , Europe(EU) , Japan(JP) and Others

# In[25]:


game1 = game.copy()
game1 = game1.pivot_table(['NA_Sales','EU_Sales','JP_Sales','Other_Sales'] , columns = 'Genre' ,  aggfunc = 'sum')
game1


# ### Maximum Sales by Genre for NA , EU , JP and Others

# In[26]:


game2 = game.copy()
game2 = game2.pivot_table(['NA_Sales','EU_Sales','JP_Sales','Other_Sales'] , columns = 'Genre' ,  aggfunc = 'max')
game2


# ### Global_Sales By Platform

# In[27]:


Platform = game.groupby("Platform").Global_Sales.sum().sort_values(ascending= False).head(10)
Platform


# ### Gaming platforms with most games

# In[28]:


game.Platform.value_counts().head(10)


# ### Top 10 Platform's with Highest Sales

# In[29]:


plt.figure(figsize= (5,10))
sns.set_style("whitegrid")
a = sns.barplot(Platform.values,Platform.index)
a.set_xlabel("Global Sales(in million)")
a.set_title("Top 10 Platform's with Highest Sales")


# ### Games Per Platform

# In[30]:


plt.figure(figsize= (15,5))
sns.countplot(x= "Platform",data= game)


# ### Global_Sales By Genre

# In[31]:


Genre = game.groupby("Genre").Global_Sales.sum().sort_values(ascending= False)
Genre


# ### Top 10 Genre's with Highest Sales

# In[32]:


plt.figure(figsize= (5,10))
sns.set_style("whitegrid")
a = sns.barplot(Genre.values,Genre.index)
a.set_xlabel("Global Sales(in million)")
a.set_title("Genre's with Sales")


# ### Games Per Genre

# In[33]:


plt.figure(figsize= (15,5))
sns.countplot(x = "Genre",data= game)


# ### Publishers who published most games

# In[34]:


a = game.Publisher.value_counts().head(20)
plt.figure(figsize= (5,10))
sns.barplot(a.values,a.index)


# ### North America vs Europe Sales by Genre

# In[35]:


plt.figure(figsize = (15,5))
sns.scatterplot(x = "NA_Sales",y = "EU_Sales",data = game ,hue = "Genre")


# ### North America vs Japan Sales by Genre

# In[36]:


plt.figure(figsize = (15,5))
sns.scatterplot(x = "NA_Sales",y = "JP_Sales",data = game ,hue = "Genre")


# ### Europe vs Japan Sales by Genre

# In[37]:


plt.figure(figsize = (15,5))
sns.scatterplot(x = "EU_Sales",y = "JP_Sales",data = game ,hue = "Genre")


# ### Line Plots for North America(NA) , Europe(EU) , Japan(JP) and Others Yearly Sales

# In[38]:


plt.figure(figsize= (15,5))
na = game.groupby("Year").NA_Sales.sum()
eu = game.groupby("Year").EU_Sales.sum()
jp = game.groupby("Year").JP_Sales.sum()
ot = game.groupby("Year").Other_Sales.sum()
ax = sns.lineplot(na.index,na.values,label= "NA")
ax = sns.lineplot(eu.index,eu.values,label= "EU")
ax = sns.lineplot(jp.index,jp.values,label= "JAPAN")
ax = sns.lineplot(ot.index,ot.values,label= "OTHERS")
ax.set_ylabel("Sales")
ax.set_title("Yearly Sales for all Regions")
plt.show()


# ### Games released per year

# In[39]:


year = game.Year.value_counts()
year.head(10)
plt.figure(figsize= (20,5))

sns.barplot(year.index,year.values)


# ### Top Publishers in North America

# In[40]:


game.groupby("Publisher").NA_Sales.sum().sort_values(ascending= False).head(10)


# ### Top Publishers in Europe

# In[41]:


game.groupby("Publisher").EU_Sales.sum().sort_values(ascending= False).head(10)


# ### Top Publishers in Japan

# In[42]:


game.groupby("Publisher").JP_Sales.sum().sort_values(ascending= False).head(10)


# ### Top Publishers in Other Countries

# In[43]:


game.groupby("Publisher").Other_Sales.sum().sort_values(ascending= False).head(10)


# ### Top Platforms with Highest Sales in North America

# In[44]:


NA_Platform = game.groupby("Platform").NA_Sales.sum().sort_values(ascending= False).head(10)
NA_Platform


# In[45]:


plt.figure(figsize= (18,8))
explode = (0,0,0.1,0,0,0.1,0,0.1,0,0)
labels = NA_Platform.index
colors = sns.color_palette("RdBu")
NA_Platform.plot.pie(autopct="%.1f%%", explode = explode, labels = labels , colors = colors, title = 'Top Platforms with Highest Sales in North America')
plt.show()


# ### Top Platforms with Highest Sales in Europe

# In[46]:


EU_Platform = game.groupby("Platform").EU_Sales.sum().sort_values(ascending= False).head(10)
EU_Platform


# In[47]:


plt.figure(figsize= (18,8))
explode = (0,0,0.1,0,0.1,0,0,0,0.1,0)
labels = EU_Platform.index
colors = sns.color_palette("Paired")
EU_Platform.plot.pie(autopct="%.1f%%", explode = explode, labels = labels , colors = colors , title = 'Top 10 Platforms with Highest Sales in Europe')
plt.show()


# ### Top Platforms with Highest Sales in Japan

# In[48]:


JP_Platform = game.groupby("Platform").JP_Sales.sum().sort_values(ascending= False).head(10)
JP_Platform


# In[49]:


plt.figure(figsize= (18,8))
explode = (0,0,0.1,0,0,0.1,0,0,0.1,0)
labels = JP_Platform.index
colors = sns.color_palette("Set3")
JP_Platform.plot.pie(autopct="%.1f%%", explode = explode, labels = labels , colors = colors , title = 'Top 10 Platforms with Highest Sales in Japan' )
plt.show()


# ### Top Platforms with Highest Sales in Other Regions

# In[50]:


Other_Platform = game.groupby("Platform").Other_Sales.sum().sort_values(ascending= False).head(10)
Other_Platform


# In[54]:


plt.figure(figsize= (18,8))
explode = (0,0,0.1,0,0,0.1,0,0,0.1,0)
labels = Other_Platform.index
colors = sns.color_palette("Paired")
Other_Platform.plot.pie(autopct="%.1f%%", explode = explode, labels = labels , colors = colors , title = 'Top 10 Platforms with Highest Sales in Other Regions' )
plt.show()

