#!/usr/bin/python
# -*- coding:utf-8 -*-
biaozhun_list = [1, 2, 4, 5, 6]
temp_list = [0]*len(biaozhun_list)
print temp_list
test_list = [2, 5]
# # 期望得到   [1,0,0,5,0]
#
for i in xrange(0, len(biaozhun_list)):
    # 判断用户哪些标签在list列表中
    for j in xrange(0, len(test_list)):
        if (test_list[j] == biaozhun_list[i]):
            temp_list[i] = test_list[j]
        else:
            temp_list[i] == 0
print temp_list
