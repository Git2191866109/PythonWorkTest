#!/usr/bin/python
# -*- coding:utf-8 -*-
from operator import add

# print "we are at %d%%" % 100
# print 'Your host is: %s' % 'earth'
# print 'Host: %s\tPort: %d' % ('mars', 80)
# w, p = 'web', 'page'
# print 'http://xxx.yyy.zzz/%s/%s.html' % (w, p)
#
# # 使用字典的形式
# dickStr = 'There are %(howmany)d %(lang)s Quatation symboles' % {'lang': 'python', 'howmany': 3}
# print dickStr

rec_str = "uid:238383377:utag:[u'7', u'57', u'6', u'13', u'54', u'11', u'56', u'71', u'70', u'3']"
temp_resu = rec_str.split(":")
# print temp_resu[-1]
# print temp_resu[-1].replace("[", "").replace("]", "").split(",")
result = temp_resu[-1].replace("[", "").replace("]", "").split(",")
# print type(temp_resu[-1])
for i in result:
    print type(i)
