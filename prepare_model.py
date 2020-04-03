#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import keras as ks


# In[2]:


df1 = pd.read_excel('ForeksTurkey_fixed.xlsx',index_col='day',usecols=['day','fixed'])
df2 = pd.read_excel('garantiyatirim_fixed.xlsx',index_col='day',usecols=['day','fixed'])
df3 = pd.read_excel('InvestingTR_fixed.xlsx',index_col='day',usecols=['day','fixed'])
df4 = pd.read_excel('MerkezBankası_fixed.xlsx',index_col='day',usecols=['day','fixed'])
df5 = pd.read_excel('ulketv_fixed.xlsx',index_col='day',usecols=['day','fixed'])
df6 = pd.read_excel('uzmanparacom_fixed.xlsx',index_col='day',usecols=['day','fixed'])


# In[3]:


df = df1.append(df2)
df = df.append(df3)
df = df.append(df4)
df = df.append(df5)
df = df.append(df6)


# In[4]:


df = df.sort_index(ascending=False)


# In[5]:


df_kur = pd.read_excel('kur.xlsx',index_col='day')
df_kur.drop('Unnamed: 0',axis=1,inplace=True)
df_kur


# In[6]:


data = pd.merge(df,df_kur,how='left',on='day')


# In[7]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping


# In[9]:


def c2f(l):
    r = []
    for each in l:
        if each == 'p6':
            r.append(0.13)
        if each == 'p5':
            r.append(0.10)
        if each == 'p4':
            r.append(0.08)
        if each == 'p3':
            r.append(0.06)
        if each == 'p2':
            r.append(0.04)
        if each == 'p1':
            r.append(0.02)
        if each == 'n':
            r.append(0)
        if each == 'n1':
            r.append(-0.02)
        if each == 'n2':
            r.append(-0.04)
        if each == 'n3':
            r.append(-0.06)
        if each == 'n4':
            r.append(-0.08)
        if each == 'n5':
            r.append(-0.10)
        if each == 'n6':
            r.append(-0.13)
    return r


# In[10]:


def str2float(l):
    res = []
    for each in l:
        t = str(each)
        tmp = t.replace(',','.')
        res.append(float(tmp))
    return res


# In[12]:


data = data.dropna()
data['change'] = c2f(data.c2)


# In[13]:


data.fixed = data.fixed.astype(str)
data.Açılış = str2float(data.Açılış)
X = data[['fixed','Açılış','change']]
Y = data.change
Y_yedek = Y
#le = LabelEncoder()
#Y = le.fit_transform(Y)
Y = Y.values.reshape(-1,1)


# In[14]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)


# In[16]:


max_words = 1000
max_len = 200
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(X_train.fixed)
sequences = tok.texts_to_sequences(X_train.fixed)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)


# In[17]:


def RNN():
    inputs = Input(name='inputs',shape=[max_len])
    layer = Embedding(max_words,50,input_length=max_len)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.5)(layer)
    layer = Dense(1,name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = Model(inputs=inputs,outputs=layer)
    return model


# In[18]:


model = RNN()
model.summary()
model.compile(loss='cosine_proximity',optimizer=RMSprop(),metrics=['accuracy'])


# In[19]:


model.fit(sequences_matrix,Y_train,batch_size=128,epochs=10,
          validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',min_delta=0.0001)])


# In[21]:


test_sequences = tok.texts_to_sequences(X_test.fixed)
test_sequences_matrix = sequence.pad_sequences(test_sequences,maxlen=max_len)


# In[22]:


accr = model.evaluate(test_sequences_matrix,Y_test)


# In[23]:


print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))


# In[24]:


predicted_value= model.predict(test_sequences_matrix)


# In[27]:


def rescale_linear(array, new_min, new_max):
    """Rescale an arrary linearly."""
    minimum, maximum = np.min(array), np.max(array)
    m = (new_max - new_min) / (maximum - minimum)
    b = new_min - m * minimum
    return m * array + b


# In[28]:


l = predicted_value


# In[29]:


l = (rescale_linear(l,min(Y_test),max(Y_test)))


# In[39]:


import matplotlib.pyplot as plt
plt.plot(l[:50], color= 'red',label='Tahmin',linestyle='-.')
plt.plot(Y_test[:50],color= 'blue',label='Gerçek')
plt.xlabel("Twitler")
plt.ylabel("Değişim miktarı(kuruş)")
plt.legend()
plt.show()


# In[31]:


def accr_control(pre,real):
    n = len(pre)
    one = 0
    three = 0 
    five = 0
    seven = 0
    ten = 0
    twenty = 0
    for i in range(len(pre)):
        if abs(pre[i] - real[i]) < 0.20 :
            twenty += 1
        if abs(pre[i] - real[i]) < 0.10  :
            ten += 1
        if abs(pre[i] - real[i]) < 0.07  :
            seven += 1
        if abs(pre[i] - real[i]) < 0.05  :
            five += 1
        if abs(pre[i] - real[i]) < 0.03  :
            three += 1
        if abs(pre[i] - real[i]) < 0.01  :
            one += 1
    print("N:"+str(n))     
    print("Twenty:"+ str(twenty/n))
    print("Ten:"+ str(ten/n))
    print("Seven:"+ str(seven/n))
    print("Five:"+str(five/n))
    print("Three:"+str(three/n))
    print("One:"+str(one/n))


# In[32]:


(accr_control(l,Y_test))


# In[33]:


model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")

