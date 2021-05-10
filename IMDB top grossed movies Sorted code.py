#!/usr/bin/env python
# coding: utf-8

# In[2]:


# # What type of movies are getting good rating and gross amount?
#Its a task from kaggle. The data file was top rated 1000 movies of IMDB. The task is to sort and analyze them according to the 
#ratings and the gross amount.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'D:\Upal\Python\IMDB top grossed movies\imdb_top_1000.csv')

del df['Certificate']

df=df.drop(['Star3','Star4'], axis=1)

df.sort_values(by=['Gross'], ascending=False)

df=df.drop(['Poster_Link'], axis=1)

df['Gross'] = df['Gross'].replace('NaN', '0')

df.dropna(subset=["Gross"], axis = 0 , inplace= True)

df['Gross'].fillna(0, inplace=True)

df['Meta_score'].fillna(0, inplace=True)

df.sort_values(by=['Released_Year'], ascending=True)

df['Gross'] = df['Gross'].str.replace(',','')

df.sort_values(by=['Gross'], ascending=False)

df['Gross'] = df['Gross'].astype(np.int64)

df.sort_values(by=['Gross'], ascending=False)

df.sort_values(by=['IMDB_Rating'], ascending=True)

dfir=df[df['IMDB_Rating']>=8]

dfir

dfvc=df[df['No_of_Votes']>=700000]

dfir=dfvc[dfvc['IMDB_Rating']>=8]

dfir.sort_values(by=['Gross'], ascending=False)

dfg=dfir[dfir['Gross']>=100000000]

dfg.rename(columns={'Series_Title':'Movie_Title'}, inplace=True)

dfg.corr()
#relation among the datas, such as IMDB rating has a 70% of relation due to we took the data according to the votes and IMDB ratings

numerical_attributes = ['IMDB_Rating', 'Meta_score', 'No_of_Votes', 'Gross']
dfg[numerical_attributes].hist(figsize = (15, 6), color = 'blue', edgecolor = 'red', layout = (2, 2));

fig,axs=plt.subplots(figsize=(25,5))
g=sns.barplot(x=dfg['Movie_Title'][:20],y=dfg['Gross'][:20], palette = 'husl')
g.set_title("IMDB Rating of top Rated movies", weight = "bold")
plt.show()




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




