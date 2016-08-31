# coding: utf-8

# In[627]:


import pandas as pd
import sqlalchemy as sc
from sqlalchemy.orm import sessionmaker

# configuration of mysql and connect

engine = sc.create_engine("mysql+pymysql://mojiro:moji_readonly@192.168.1.14:3323/fdstrm?charset=utf8")
session = sessionmaker(engine)
db = session()

# In[628]:

f1 = open("C:\\Users\\huiliang.chen\\Desktop\\stopkeys.txt")
f1_lines = f1.readlines()
f1_lines_str = []
for i in f1_lines:
    f1_lines_str.append(i.strip())

# In[629]:

import jieba
# jieba.load_userdict("D:\\chen\\feed\\feed_dic\\dic.txt")
import gensim


def feed_cate(n):
    feed_cg1 = df_se[df_se["feed_category"] == n]
    tt1_list = feed_cg1["feed_title"].values
    texts = [list(jieba.cut(text)) for text in tt1_list]

    dic = gensim.corpora.Dictionary(texts)
    dic_type = dic.token2id
    ### stopword
    global f1_lines_str
    stopwords = [" ", ",", "?", "-", "!", "（", "）", "(", '+', '#', ")", "|", '|', '|', '°', '“', '、',
                 '。', '：', '！', ',', ' ', '？', '｜', '"', '~', '”', '是', '被', '从', '的', '呢', '为', '图', '后', '吗', '到底',
                 '人', '岁']
    stopwords = stopwords + f1_lines_str
    global stopwords_uni
    stopwords_uni = []
    for i in stopwords:
        stopwords_uni.append(i.decode('utf-8'))
    bone = set(dic_type.keys()) - set(stopwords_uni)
    global dic_exstopword
    dic_exstopword = gensim.corpora.Dictionary([bone])

    global dic_exstopword
    texts_corpus = [dic_exstopword.doc2bow(text) for text in texts]
    return texts_corpus, feed_cg1


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
    s1 = max(n / float(m1), n / float(m2))
    s2 = 2 * n / float(m1 + m2)
    return [s2, s1]


# In[630]:

dic_cate = {1: 0.7, 3: 0.7, 4: 0.29, 5: 0.6, 18: 0.7, 19: 0.7, 20: 0.7, 21: 0.7, 22: 0.7, 28: 0.7, 29: 0.7, 34: 0.7,
            42: 0.7, 44: 0.7, 49: 0.7, 57: 0.7, 77: 0.7, 81: 0.7, 82: 0.7, 84: 0.7, 85: 0.7, 101: 0.7}

engine1 = sc.create_engine("mysql+pymysql://root:chen123@localhost/chen?charset=utf8")
session = sessionmaker(engine1)
db1 = session()
db1.execute("drop table if exists feed_similarity_2")
db1.execute(
    "create table if not exists feed_similarity_2(id_1 bigint(20),id_2 bigint(20),cal_cross float(5,4),max_part float(5,4),`feed_title1` varchar(255),`feed_title2` varchar(255))DEFAULT CHARSET=utf8")


def w_sql(n):
    texts_corpus, feed_cg1 = feed_cate(n)
    # calculate the similarity
    cal_sum = []
    for i in range(len(texts_corpus)):
        for j in range(i + 1, len(texts_corpus)):
            cal = cross_list(texts_corpus[i], texts_corpus[j])
            if cal[0] != 0 and cal[0] >= dic_cate[n]:
                db1.execute(
                    "insert into feed_similarity_2(id_1,id_2,cal_cross,max_part,feed_title1,feed_title2)values(:a1,:a2,:a3,:a4,:a5,:a6)",
                    {"a1": int(feed_cg1.iloc[i, 0]), "a2": int(feed_cg1.iloc[j, 0]),
                     "a3": float(cal[0]), "a4": float(cal[1]), "a5": feed_cg1.iloc[i, 3].encode('utf-8'),
                     "a6": feed_cg1.iloc[j, 3].encode('utf-8')})


# In[ ]:

import time

while True:
    engine = sc.create_engine("mysql+pymysql://mojiro:moji_readonly@192.168.1.14:3323/fdstrm?charset=utf8")
    session = sessionmaker(engine)
    db = session()
    engine1 = sc.create_engine("mysql+pymysql://root:chen123@localhost/chen?charset=utf8")
    session = sessionmaker(engine1)
    db1 = session()
    db1.execute("drop table if exists feed_similarity_2")
    db1.execute(
        "create table if not exists feed_similarity_2(id_1 bigint(20)not null AUTO_INCREMENT,id_2 bigint(20),cal_cross float(5,4),max_part float(5,4),`feed_title1` varchar(255),`feed_title2` varchar(255))DEFAULT CHARSET=utf8")
    se = db.execute(
        "select id,feed_type,feed_category,feed_title,feed_desc,create_time,FROM_UNIXTIME(create_time/1000,'%d,%T') from feed  where (UNIX_TIMESTAMP()-create_time/1000)/60/60<24 GROUP BY create_time").fetchall()
    df_se = pd.DataFrame(se)
    df_se.columns = ["id", "feed_type", "feed_category", "feed_title", "feed_desc", "microsecond_time", "time"]

    for i in dic_cate.keys():
        w_sql(i)
    db1.commit()
    time.sleep(60)
