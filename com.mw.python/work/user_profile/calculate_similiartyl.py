# coding: utf-8

# In[29]:


# ********calculate  the similarity of two titles********
import pandas as pd
import gensim
import jieba
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

df = pd.read_csv("D:\\chen\\find_similarity\\data1.csv",
                 names=["id", "feed_type", "feed_category", "feed_title", "feed_desc"])

### aim at feed_catagory=1

######################################
feed_cg1 = df[df["feed_category"] == 4]

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

texts_corpus_tfidf = gensim.models.TfidfModel(texts_corpus)
texts_corpus_tfidf_texts = texts_corpus_tfidf[texts_corpus]


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


f = open("d://chen/feed_title_4.csv", 'w')
for i in range(len(texts_corpus)):
    for j in range(i + 1, len(texts_corpus)):
        cal = cross_list(texts_corpus[i], texts_corpus[j])
        if cal != 0:
            f.write("%d,%d,%f\n" % (feed_cg1.iloc[i, 0], feed_cg1.iloc[j, 0], cal))
            ##########################################################
