#!/usr/bin/python
# -*- coding:utf-8 -*-
from operator import add

print "we are at %d%%" % 100
print 'Your host is: %s' % 'earth'
print 'Host: %s\tPort: %d' % ('mars', 80)
w, p = 'web', 'page'
print 'http://xxx.yyy.zzz/%s/%s.html' % (w, p)

# 使用字典的形式
dickStr = 'There are %(howmany)d %(lang)s Quatation symboles' % {'lang': 'python', 'howmany': 3}
print dickStr
