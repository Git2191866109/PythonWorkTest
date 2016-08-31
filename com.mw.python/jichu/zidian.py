# encoding:utf-8
aDict = {'host': 'earth'}
aDict['port'] = 80
print aDict
print aDict.keys()
print aDict['host']

for key in aDict:
    print key, aDict[key]
stopwords = [" ", ",", "?", "-", "!", "（", "）", "|", '|', '|', '°', '“', '、', '。', '！', '，', '？', '｜', '"', '~', '”',
             '是', '的', '呢', '吗', '到底']
alist = ["a", "a", "c"]
print set(alist)
