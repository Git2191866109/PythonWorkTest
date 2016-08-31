# coding: utf-8

# ### get the data and transform it to frame

# In[1]:

f1 = open("D:\\chen\\article_recommendation\\recommendation\\portrait_uid_tags_600_700_10000")
f2 = open("D:\\chen\\article_recommendation\\recommendation\\uid_cat_ratio_600_700_10000")
f3 = open("D:\\chen\\article_recommendation\\recommendation\\uid_cat_600_700_10000")
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
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.cross_validation import train_test_split
import sklearn.metrics as sm

# ### use the neural newtwork to train

# In[71]:

model = Sequential()
model.add(Dense(output_dim=46, input_dim=94, init='uniform'))
model.add(Activation("softmax"))
model.compile(loss='mean_squared_error', optimizer='adadelta', metrics=['accuracy'])

# In[72]:

X = tag_fra_fea1.ix[:, 1:]
Y = cat_fra_fea_sel.ix[:, 1:47]
X_train, X_val, yl_train, yl_val = train_test_split(X, Y, train_size=0.8)

# In[ ]:

model.fit(X_train.fillna(0).values, yl_train.fillna(0).values, nb_epoch=10,
          validation_data=(X_val.fillna(0).values, yl_val.fillna(0).values), verbose=1)

# In[66]:

model.save("D:\\chen\\article_recommendation\\recommendation\\600_700.h5")

# In[67]:

from keras.models import load_model

model0_20 = load_model("D:\\chen\\article_recommendation\\recommendation\\0_20.h5")
model3000_4000 = load_model("D:\\chen\\article_recommendation\\recommendation\\3000_4000.h5")
model600_700 = load_model("D:\\chen\\article_recommendation\\recommendation\\600_700.h5")

res0_20 = model0_20.predict(X_val.fillna(0).values)
res600_700 = model600_700.predict(X_val.fillna(0).values)
res3000_4000 = model3000_4000.predict(X_val.fillna(0).values)
print "use different model to predict the data of 600_700 and calculate the mean_squared_error"

print "0_20:", sm.mean_squared_error(yl_val.fillna(0).values, res0_20)
print "600_700:", sm.mean_squared_error(yl_val.fillna(0).values, res600_700)
print "3000_4000:", sm.mean_squared_error(yl_val.fillna(0).values, res3000_4000)


# In[ ]:
