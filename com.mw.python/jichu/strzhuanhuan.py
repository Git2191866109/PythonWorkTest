#!/usr/bin/python
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    # s = u'中国'
    # s1 = "中国"
    # s_gb = s.encode('gb2312')
    # print s
    # print s1
    # print s_gb

    x ='\xbf\xb0\xb3\xc6'
    # print x.encode('gb2312')
    print x.decode('gb2312')