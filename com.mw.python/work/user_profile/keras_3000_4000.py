# coding: utf-8

# ### get the data and transform it to frame

# In[1]:

f1 = open("D:\\chen\\article_recommendation\\recommendation\\portrait_uid_tags_3000_4000_10000")
f2 = open("D:\\chen\\article_recommendation\\recommendation\\uid_cat_ratio_3000_4000_10000")
f3 = open("D:\\chen\\article_recommendation\\recommendation\\uid_cat_3000_4000_10000")
flines1 = f1.readlines()
flines2 = f2.readlines()
flines3 = f3.readlines()

flist_tag = [(line.strip().split('\t'))[1:4] for line in flines1]
flist_cat = [(line.strip().split('\t')) for line in flines2]
flist_num = [(line.strip().split('\t')) for line in flines3]

import pandas as pd

tag_fra = pd.DataFrame(flist_tag, columns=['uid', 'tag', 'weight']).astype(float)
cat_fra = pd.DataFrame(flist_cat, columns=['uid', 'cat', 'ratio']).astype(float)
num_fra = pd.DataFrame(flist_num, columns=['uid', 'num']).astype(float)

# In[2]:

cat_fra_fea = cat_fra.set_index(['uid', 'cat']).unstack()['ratio'].reset_index()
tag_fra_fea = tag_fra.set_index(['uid', 'tag']).unstack()['weight'].reset_index()
tag_fra_fea1 = pd.merge(tag_fra_fea, num_fra, on='uid', how='left')
cat_fra_fea_sel = pd.merge(cat_fra_fea, tag_fra_fea1['uid'].reset_index(), on='uid', how='inner')
tag_fra_fea1 = pd.merge(tag_fra_fea1, cat_fra_fea_sel['uid'].reset_index(), on='uid', how='inner')
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.cross_validation import train_test_split
import sklearn.metrics as sm

# In[3]:

model = Sequential()
model.add(Dense(output_dim=46, input_dim=94, init='uniform'))
model.add(Activation("softmax"))
model.compile(loss='mean_squared_error', optimizer='adadelta', metrics=['accuracy'])

# In[4]:

cat_fra_fea.shape, tag_fra_fea.shape, num_fra.shape, tag_fra_fea1.shape, cat_fra_fea_sel.shape

# In[5]:

cat_fra_fea_sel.head()

# In[8]:

X = tag_fra_fea1.ix[:, 1:95]
Y = cat_fra_fea_sel.ix[:, 1:47]
X = X.reindex_axis([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,
                    11.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0,
                    21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0,
                    30.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 42.0,
                    43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 52.0,
                    53.0, 54.0, 55.0, 56.0, 57.0, 59.0, 60.0, 61.0, 62.0,
                    63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0,
                    73.0, 74.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0,
                    84.0, 105.0, 142.0, 145.0, 164.0, 165.0, 166.0, 167.0, 168.0,
                    169.0, 170.0, 171.0, 172.0, 173.0, 174.0, 175.0, 176.0, 177.0,
                    178.0, 179.0, 180.0, u'num'], axis=1)
Y = Y.reindex_axis([1.0, 3.0, 4.0, 5.0, 18.0, 19.0, 20.0, 21.0, 22.0, 28.0,
                    29.0, 34.0, 36.0, 41.0, 42.0, 44.0, 49.0, 57.0, 65.0, 66.0,
                    71.0, 72.0, 73.0, 74.0, 75.0, 77.0, 78.0, 79.0, 80.0, 81.0,
                    82.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 93.0, 96.0,
                    97.0, 98.0, 99.0, 100.0, 101.0, 102.0], axis=1)
X_train, X_val, yl_train, yl_val = train_test_split(X, Y, train_size=0.8)

# In[14]:

model.fit(X_train.fillna(0).values, yl_train.fillna(0).values, nb_epoch=10,
          validation_data=(X_val.fillna(0).values, yl_val.fillna(0).values), verbose=1)

# In[16]:

model.save("D:\\chen\\article_recommendation\\recommendation\\3000_4000.h5")

# In[18]:

from keras.models import load_model

model0_20 = load_model("D:\\chen\\article_recommendation\\recommendation\\0_20.h5")
model3000_4000 = load_model("D:\\chen\\article_recommendation\\recommendation\\3000_4000.h5")
model600_700 = load_model("D:\\chen\\article_recommendation\\recommendation\\600_700.h5")

res0_20 = model0_20.predict(X_val.fillna(0).values)
res600_700 = model600_700.predict(X_val.fillna(0).values)
res3000_4000 = model3000_4000.predict(X_val.fillna(0).values)

print "use different model to predict the data of 3000_4000 and calculate the mean_squared_error"

print "0_20:", sm.mean_squared_error(yl_val.fillna(0).values, res0_20)
print "600_700:", sm.mean_squared_error(yl_val.fillna(0).values, res600_700)
print "3000_4000:", sm.mean_squared_error(yl_val.fillna(0).values, res3000_4000)


# In[ ]:
