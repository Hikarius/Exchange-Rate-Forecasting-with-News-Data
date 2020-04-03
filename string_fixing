#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


name = 'ForeksTurkey' # fixing file name


# In[3]:


df = pd.read_excel(name+'.xlsx')


# In[4]:


def int2str(s):
    l1 = s.split()
    l2 = []
    for each in l1 :
        if each.isalpha():
            l2.append(each)
            l2.append(' ')
        else:
            if each.isnumeric():
                e = int(each)
                if e>2050 or e<1980:
                    if e > 5000:
                        e=5000
                    elif e > 1000:
                        e=1000
                    elif e > 900:
                        e=900
                    elif e >800:
                        e=800
                    elif e >700:
                        e=700
                    elif e >600:
                        e=600
                    elif e >500:
                        e=500
                    elif e >400:
                        e=400
                    elif e >300:
                        e=300
                    elif e >200:
                        e=200
                    elif e >100:
                        e=100
                    elif e >90:
                        e=90
                    elif e >80:
                        e=80
                    elif e >70:
                        e=70
                    elif e >60:
                        e=60
                    elif e >50:
                        e=50
                    elif e >40:
                        e=40
                    elif e >30:
                        e=30
                    elif e >20:
                        e=20
                    elif e >10:
                        e=10
                    elif e >5:
                        e=5
                    elif e >1:
                        e=1
                each = str(e)
                l2.append(each)
                l2.append(' ')

                
    return ''.join(l2)


# In[5]:


def ek_sil(s):
    l1 = s.split()
    l2 = []
    for word in l1:
        if word.find('`') != -1:
            if word[0] == '`':
                word = word.replace('`','')
            else:
                word = word[:word.find('`')]
        l2.append(word)
        l2.append(' ')
    return ''.join(l2)


# In[6]:


strlist = ['euro','şirket','kredi','bütçe','banka','faiz','müşteri','bitcoin','dolar','büyü','küçül','daralma',
          'daralma','ticaret','anlaşma','kısıt','enflasyon','rapor','tahvil','indirim','taksit','resmi','rezerv','varlık',
          'azal','oran','piyasa','karışık','arttı','indi','devlet','hesap','kriter','tahsilat','önle','karar','gergin',
          'gider','tüket','üret','güven','endeks','açıkla','açıl','kapan','belirsiz','paket','karışık','bölge','avrupa','asya',
          'amerika','yavaş','hızlı','altın','gümüş','fiyat','istikrar','zarar','yarar','pozitif','negatif','indirim','artış',
          'yatırım','taşınmaz','getir','bariyer','yönetme','tahmin','düş','hisse','depo','kanun','teklif','hasılat','tedbir',
          'fazla','komisyon','rakam','resesyon','olası','şirket','sanayi','hazine','brexit','savaş','vade','mali','plan',
          'cari','işlem','denge','reeskont','yürürlü','yabancı','varlık','harekat','dayanıklı','kanıt','beklen','ihracat','ithalat',
          'müzakere','anlaş','görev','deflasyon','yerel','para','teklif','gelişme','güven','gönderi','tweet','sermaye','istihdam']


# In[7]:


def root(s,strlist):
    l1 = s.split()
    l2 = []
    for s1 in l1:
        for sl in strlist:
            if sl in s1:
                s1 = sl
        l2.append(s1)
        l2.append(' ')
        
        
    return ''.join(l2) 


# In[8]:


L = []
for s in df.text:
    s = s.split('https')[0]  #remove links
    s = s.replace('I','ı')
    s = s.replace('İ','i')
    s = s.replace('Ü','ü')
    s = s.replace('Ö','ö')
    s = s.replace('Ğ','ğ')
    s = s.replace('Ş','ş')
    s = s.replace('Ç','ç')
    s = s.replace('!','')
    s = s.replace('?','')
    s = s.replace(':','')
    s = s.replace(',','')
    s = s.replace(' ile ',' ') #edat ve bağlaç
    s = s.replace(' da ',' ') 
    s = s.replace(' de ',' ') 
    s = s.replace(' gibi ',' ')
    s = s.replace(' için ',' ') 
    s = s.replace(' kadar ',' ') 
    s = s.replace(' ve ',' ') 
    s = s.lower()
    s = ek_sil(s)
    s = root(s,strlist)
    s = int2str(s)
    L.append(s)
    
L


# In[9]:


L = np.array(L)


# In[10]:


df['fixed'] = L


# In[11]:


df


# In[12]:


df.drop('Unnamed: 0', axis = 1, inplace = True)


# In[13]:


df['day'] = [str(each)[:10]  for each in df.date  ]


# In[14]:


df.to_excel(name+'_fixed.xlsx')

