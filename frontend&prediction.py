#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from sys import exit


# In[2]:


from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def DolarParse():
    pasteURL = "http://tr.investing.com/currencies/usd-try"
    data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
    parse = BeautifulSoup(data)
    for dolar in parse.find_all('span', id="last_last"):
        liste = list(dolar)
    return liste


# In[3]:


try:
    dolar = float(DolarParse()[0].replace(',','.'))
    dolar
except Exception as e:
    #exit()
    dolar = 5.88


# In[4]:


try:
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
except Exception as e:
    print('Gerekli dosyalar açılamadı.')
    exit()


# In[5]:


import requests as re
import tweepy 
bs = BeautifulSoup
consumer_key = "2KUInkfMuqeFG0Q9SMU2uXTg1"
consumer_secret = "H3r2oUcpnwVZQpZzWseBDnwXI7rLDegvoMNuhDdwzmVOElZxwb"
access_token = "1632754268-F91ZBHcBSk7ZxipSdtNM6sS8Oqds6xmpOBonRuu"
access_token_secret = "tifwqapp7mJ9BGqCHVRfi4Pm1t3eZs2tvKdy9mC32NWc8"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 
texts_list=[]
date_list=[]
flag = 0
try:
    for pages in tweepy.Cursor(api.user_timeline, id='InvestingTR', count=1).pages():        
        for p in pages:
            texts_list.append(p.text+'\n')
except Exception as e:
    print(e)
    if len(texts_list) < 8:
        flag=1


# In[6]:


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
strlist = ['euro','şirket','kredi','bütçe','banka','faiz','müşteri','bitcoin','dolar','büyü','küçül','daralma',
          'daralma','ticaret','anlaşma','kısıt','enflasyon','rapor','tahvil','indirim','taksit','resmi','rezerv','varlık',
          'azal','oran','piyasa','karışık','arttı','indi','devlet','hesap','kriter','tahsilat','önle','karar','gergin',
          'gider','tüket','üret','güven','endeks','açıkla','açıl','kapan','belirsiz','paket','karışık','bölge','avrupa','asya',
          'amerika','yavaş','hızlı','altın','gümüş','fiyat','istikrar','zarar','yarar','pozitif','negatif','indirim','artış',
          'yatırım','taşınmaz','getir','bariyer','yönetme','tahmin','düş','hisse','depo','kanun','teklif','hasılat','tedbir',
          'fazla','komisyon','rakam','resesyon','olası','şirket','sanayi','hazine','brexit','savaş','vade','mali','plan',
          'cari','işlem','denge','reeskont','yürürlü','yabancı','varlık','harekat','dayanıklı','kanıt','beklen','ihracat','ithalat',
          'müzakere','anlaş','görev','deflasyon','yerel','para','teklif','gelişme','güven','gönderi','tweet','sermaye','istihdam']
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
L = []
L_yedek = []
for s in texts_list[:10]:
    s = s.split('https')[0]  #remove links
    L_yedek.append(s)
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
    


# In[7]:


from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
max_words = 1000
max_len = 200
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(L)
sequences = tok.texts_to_sequences(L)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)


# In[8]:


predicted_value= loaded_model.predict(sequences_matrix)


# In[9]:


def rescale_linear(array, new_min, new_max):
    minimum, maximum = np.min(array), np.max(array)
    m = (new_max - new_min) / (maximum - minimum)
    b = new_min - m * minimum
    return m * array + b
l = predicted_value
l = (rescale_linear(l,-0.13,0.13))


# In[10]:


change = np.mean(l)


# In[11]:


tahmin = dolar + change


# In[12]:


def create_news():       
    window = tk.Toplevel(m)
    window.title('Haberler')
    #if flag == 1:
    #    tk.Label(window, text='Haber verilerine ulaşılamadı!').grid(row=0) 
    #    return
    tk.Label(window, text=L_yedek[0]).grid(row=0) 
    tk.Label(window, text=L_yedek[1]).grid(row=1)
    tk.Label(window, text=L_yedek[2]).grid(row=2)
    tk.Label(window, text=L_yedek[3]).grid(row=3)
    tk.Label(window, text=L_yedek[4]).grid(row=4)
    tk.Label(window, text=L_yedek[5]).grid(row=5)
    tk.Label(window, text=L_yedek[6]).grid(row=6)
    tk.Label(window, text=L_yedek[7]).grid(row=7)


# In[13]:


def create_curr():
    win = tk.Toplevel(m)
    win.title('Kur değeri')
    t1 = tk.Label(win,text='Doların şu anki değeri:\n\n'+str(dolar)[:4] ,width=30,height=13,bg='white')
    t1.pack()


# In[ ]:


m = tk.Tk(screenName='Yarının dolar değeri')
m.title('Kur tahmini')
t1 = tk.Label(m,text='Doların yarınki değeri:\n\n'+str(tahmin)[:4] ,width=30,height=13,bg='white')
t1.pack()
menu = tk.Menu(m) 
m.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='Seçenekler', menu=filemenu) 
filemenu.add_command(label='Haberleri görüntüle',command=create_news) 
filemenu.add_command(label='Anlık kur bilgisi',command=create_curr) 
m.mainloop()

