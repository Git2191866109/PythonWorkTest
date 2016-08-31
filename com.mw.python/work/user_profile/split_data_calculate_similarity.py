# coding: utf-8

# ### n(n+1)/2=(n+a)(n-a+1)/2*t
# 
# ### right=(n*n+n)(1-1/t)+1/4；###result:a=np.sqrt(right)+1/2.0

# 
# ### 对特定catagory数据处理

# In[1]:

import pandas as pd
import gensim
import jieba

df = pd.read_csv("D:\\chen\\find_similarity\\data1.csv",
                 names=["id", "feed_type", "feed_category", "feed_title", "feed_desc"])
### aim at feed_catagory=1
######################################
feed_cg1 = df[df["feed_category"] == 29]

tt1_list = feed_cg1["feed_title"].values
texts = [list(jieba.cut(text)) for text in tt1_list]
dic = gensim.corpora.Dictionary(texts)
dic_type = dic.token2id

### stopword
stopwords = [" ", ",", "?", "-", "!", "（", "）", "|", '|', '|', '°', '“', '、', '。', '！', '，', '？', '｜', '"', '~', '”',
             '是', '的', '呢', '吗', '到底']
bone = set(dic_type.keys()) - set(stopwords)
dic_exstopword = gensim.corpora.Dictionary([bone])
texts_corpus = [dic_exstopword.doc2bow(text) for text in texts]


# ### 两title之间的相关性计算

# In[2]:

def dic_list(s_list):
    dic_list = {}
    for i in range(len(s_list)):
        m, n = s_list[i]
        dic_list[m] = dic_list.get(m, 0) + n
    return dic_list


def cross_list(l1, l2):
    dic1 = dic_list(l1)
    dic2 = dic_list(l2)
    n = len(set(dic1.keys()).intersection(set(dic2.keys())))
    m1 = sum(dic1.values())
    m2 = sum(dic2.values())
    s = 2.0 * n / (m1 + m2)
    return s


# ### 产生分块的数据点区间

# In[3]:

import numpy as np


def get_a(n, t):
    right = ((n * n + n) * (1 - 1 / t)) + 1 / 4
    a = np.sqrt(right) + 1 / 2.0
    return int(np.round(a))


def get_list_a(n, t):
    list_a = []
    for i in range(t, 1, -1):
        a = get_a(n, i)
        list_a.append(a)
        n = a - 1
    return list_a


def generate_list(n, t):
    res = get_list_a(n, t)

    tem = []
    for i in range(len(res)):
        if i == 0:
            tem.append([n, res[i]])
        else:
            tem.append([res[i - 1] - 1, res[i]])
    tem.append([res[i] - 1, 1])
    return tem


# ### 导出数据到文件

# In[4]:

##############################---*-mn=>[m,n]-*---#######
def result_mn(m, n):
    f = open("d://chen/feed_title/category_" + str(20) + "_" + str(m) + "_" + str(n) + ".csv",
             'w')  # !!!!!!!!!!!!!!!!!!!!!!
    for i in range(m, n - 1, -1):
        for j in range(i, 0, -1):
            cal = cross_list(texts_corpus[i - 1], texts_corpus[j - 1])
            if cal != 0 and i != j:
                f.write("%d,%d,%f\n" % (feed_cg1.iloc[i - 1, 0], feed_cg1.iloc[j - 1, 0], cal))
    f.close()


# In[5]:

n = len(texts_corpus)
split_list = generate_list(n, 6);
print (split_list)
import threading

threads = []
for i in range(len(split_list)):
    t = threading.Thread(target=result_mn, args=(split_list[i][0], split_list[i][1]))
    threads.append(t)
for i in range(len(split_list)):
    threads[i].start()

f = open("d:\\chen\\feed_title\\category_1_156_140.csv")
f.close()
f = open("d:\\chen\\feed_title\\category_156_140.csv")
f.close()

import os

path = "D:\\chen\\feed_title\\"
lsdir = os.listdir(path)
medi = 0
for i in range(1, len(lsdir)):
    ##########'category_1_'
    if lsdir[i][0:11] == 'category_1_' and medi == 0:
        #########
        df = pd.read_csv(path + lsdir[i], header=None)
        medi = medi + 1
    elif lsdir[i][0:11] == 'category_1_' and medi != 0:
        #########
        df_temp = pd.read_csv(path + lsdir[i], header=None)
        df = df.append(df_temp)
