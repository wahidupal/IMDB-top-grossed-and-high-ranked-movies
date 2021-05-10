#!/usr/bin/env python
# coding: utf-8

# # What type of movies are getting good rating and gross amount?

# In[67]:


import pandas as pd
import numpy as np


# In[110]:


df = pd.read_csv(r'D:\Upal\Python\imdb_top_1000.csv')


# In[111]:


df


# In[112]:


del df['Certificate']


# In[113]:


df


# In[114]:


df=df.drop(['Star3','Star4'], axis=1)


# In[115]:


df


# In[116]:


df.sort_values(by=['Gross'], ascending=False)


# In[117]:


df=df.drop(['Poster_Link'], axis=1)


# In[118]:


df.describe()


# In[119]:


df.info()


# In[120]:


df.isnull().sum()


# In[121]:


df[df['Series_Title'].str.contains('Hamilton')]


# In[122]:


df['Gross'] = df['Gross'].replace('NaN', '0')


# In[123]:


df


# In[124]:


df.dropna(subset=["Gross"], axis = 0 , inplace= True)


# In[125]:


df['Gross'].fillna(0, inplace=True)


# In[126]:


df


# In[127]:


df.isnull().sum()


# In[128]:


df.info()


# In[129]:


df[df['Series_Title'].str.contains('Anand')]


# In[130]:


df['Meta_score'].fillna(0, inplace=True)


# In[131]:


df


# In[132]:


df.isnull().sum()


# In[133]:


df.sort_values(by=['Released_Year'], ascending=True)


# In[91]:


df


# In[134]:


df['Gross'].dtypes


# In[135]:


type(df)


# In[136]:


df


# In[139]:


df['Gross'] = df['Gross'].str.replace(',','')


# In[140]:


df


# In[142]:


df.sort_values(by=['Gross'], ascending=False)


# In[147]:


df.info()


# In[145]:


df['Gross'] = df['Gross'].astype(np.int64)


# In[148]:


df.sort_values(by=['Gross'], ascending=False)


# In[151]:


df['Genre'].nunique()


# In[153]:


df.sort_values(by=['IMDB_Rating'], ascending=True)


# In[154]:


dfir=df[df['IMDB_Rating']>=8]


# In[155]:


dfir


# In[167]:


dfvc=df[df['No_of_Votes']>=700000]


# In[168]:


dfvc


# In[169]:


df['IMDB_Rating'].unique()


# In[170]:


dfir=dfvc[dfvc['IMDB_Rating']>=8]


# In[171]:


dfir


# In[173]:


dfir.sort_values(by=['Gross'], ascending=False)


# In[182]:


dfg=dfir[dfir['Gross']>=100000000]


# In[184]:


dfg


# In[185]:


dfg.info()


# In[205]:


dfg['Genre'].nunique()


# In[187]:


import matplotlib.pyplot as plt


# In[188]:


dfg.rename(columns={'Series_Title':'Movie_Title'}, inplace=True)


# In[189]:


dfg


# In[206]:


dfg.corr()
#relation among the datas, such as IMDB rating has a 70% of relation due to we took the data according to the votes and IMDB ratings


# In[207]:


numerical_attributes = ['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Gross']
dfg[numerical_attributes].hist(figsize = (15, 6), color = 'blue', edgecolor = 'red', layout = (2, 2));


# In[222]:


fig,axs=plt.subplots(figsize=(25,5))
g=sns.barplot(x=dfg['Movie_Title'][:20],y=dfg['Gross'][:20], palette = 'husl')
g.set_title("IMDB Rating of top Rated movies", weight = "bold")
plt.show()


# In[209]:


pip install seaborn


# In[211]:


import seaborn as sns


# In[223]:


dfg.sort_values(by=['Gross'], ascending=False)


# In[231]:


fig,axs=plt.subplots(figsize=(25,5))
g=sns.barplot(x=dfg['Movie_Title'][:20],y=dfg['IMDB_Rating'][:20], palette = 'husl')
g.set_title("IMDB Rating of top Rated movies", weight = "bold")
plt.xticks(rotation=90)
plt.show()


# In[225]:


dfghigh=dfg.sort_values(by=['Gross'], ascending=False)


# In[229]:


fig,axs=plt.subplots(figsize=(25,5))
g=sns.barplot(x=dfghigh['Movie_Title'][:20],y=dfghigh['Gross'][:20], palette = 'husl')
g.set_title("IMDB Rating of top Rated movies", weight = "bold")
plt.xticks(rotation=90)
plt.show()


# In[234]:


fig,axs=plt.subplots(figsize=(20,5))
g=sns.barplot(x=dfghigh['Released_Year'].value_counts()[:20].index,y=dfghigh['Released_Year'].value_counts()[:20])
g.set_title("Maximum Movies released in-", weight = "bold")
g.set_xlabel("Years")
plt.show()


# In[237]:


from collections import Counter
genre=[]
for x in dfghigh['Genre']:
    for y in x.split(','):
        genre.append(y.strip().lower())

count=Counter(genre)
count=count.most_common()[:15]
x,y=map(list,zip(*count))

fig,axs=plt.subplots(figsize=(20,5))
g=sns.barplot(y,x)
g.set_ylabel("Genres", weight = "bold")
g.set_title("Top Ten Genres", weight = "bold")
plt.show()


# In[ ]:




