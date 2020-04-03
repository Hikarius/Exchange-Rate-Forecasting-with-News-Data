#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('daily.csv',sep=',')
df


# In[3]:


df.Tarih = df.Tarih.astype(str)


# In[4]:


df['day'] = [(str(each)[6:10])+'-'+str(each)[3:5]+'-'+str(each)[0:2] for each in df.Tarih]


# In[5]:


df.drop(['Tarih','Şimdi','Yüksek','Düşük','Fark %'],axis=1,inplace=True)
df


# In[6]:


a = [float(df.Açılış[i].replace(',','.') ) -  float(df.Açılış[i+1].replace(',','.')) for i in range(len(df.Açılış)-1)]


# In[7]:


df.drop(0,axis=0,inplace = True)


# In[8]:


df['fark'] = a


# In[9]:


df['değişim'] = ['pozitif' if each > 0 else 'negatif' for each in df.fark]
df


# In[11]:


c1 = ['p6' for each in df.fark]
for i in range(1,len(c1)):
    if df.fark[i] < 0.12:
        c1[i] = 'p5'
    if df.fark[i] < 0.09:
        c1[i] = 'p4'
    if df.fark[i] < 0.07:
        c1[i] = 'p3'
    if df.fark[i] < 0.05:
        c1[i] = 'p2'
    if df.fark[i] < 0.03:
        c1[i] = 'p1'
    if df.fark[i] < 0.01:
        c1[i] = 'n'
    if df.fark[i] < -0.01:
        c1[i] = 'n1'
    if df.fark[i] < -0.03:
        c1[i] = 'n2'
    if df.fark[i] < -0.05:
        c1[i] = 'n3'
    if df.fark[i] < -0.07:
        c1[i] = 'n4'
    if df.fark[i] < -0.09:
        c1[i] = 'n5'
    if df.fark[i] < -0.12:
        c1[i] = 'n6'


# In[13]:


c1[0] = 'n'


# In[20]:


df['c'][:-1] = c1[1:]


# In[25]:


c2 = ['p2' if each == 'p4' or each == 'p5' or each == 'p6' else each for each in df.c]
c2 = ['n' if each == 'p1' or each == 'n' or each == 'n1' else each for each in df.c]
c2 = ['p1' if each == 'p2' or each == 'p3'  else each for each in df.c]
c2 = ['n1' if each == 'n2' or each == 'n3'  else each for each in df.c]
c2 = ['n2' if each == 'n4' or each == 'n5' or each == 'n6' else each for each in df.c]


# In[32]:


from collections import Counter
print(Counter(c1).keys(),Counter(c1).values())


# In[29]:


df['c2'] = c2


# In[30]:


df.to_excel('kur.xlsx')


# In[64]:


df = df.sort_index()
df

