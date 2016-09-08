#!/usr/bin/python
# -*- coding:utf-8 -*-

aList = [1, 2, 3, 4, 5, 6]


def jishu(aList):
    for i in aList:
        x = lambda i:i>3
        print x

if __name__ == '__main__':
    jishu(aList)
