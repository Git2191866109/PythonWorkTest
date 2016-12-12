#!/usr/bin/python
# -*- coding:utf-8 -*-
# biaozhun_list = [1, 2, 4, 5, 6]
# temp_list = [0]*len(biaozhun_list)
# print temp_list
# test_list = [2, 5]
# # # 期望得到   [1,0,0,5,0]
# #
# for i in xrange(0, len(biaozhun_list)):
#     # 判断用户哪些标签在list列表中
#     for j in xrange(0, len(test_list)):
#         if (test_list[j] == biaozhun_list[i]):
#             temp_list[i] = test_list[j]
#         else:
#             temp_list[i] == 0
# print temp_list


li = [ u' \u4f1a', u' \u53eb']
# print ", ".join(li).strip()
print ", ".join(li).replace(" ","")
print




# li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
# hwords = ["妹子", "女", "过分"]
# hhword = ['\xe5\x85\x89\xe8\xbe\x89', '\xe6\xaf\x8d\xe6\x80\xa7', '\xe5\x85\x85\xe6\xbb\xa1', '\xe5\x84\xbf\xe5\xa5\xb3', '\xe6\x8b\xa5']
#
# # ['mpilgrim', 'foo']
# # print [elem for elem in li if elem != "b"]
# # ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
# # print [elem for elem in li if li.count(elem) == 1]
# # print [elem for elem in hwords if str(elem) == 1]
# # ['a', 'mpilgrim', 'foo', 'c']
#
# x = ['\xe4\xba\x86', ' \xe8\x80\x81\xe5\xb8\x88', ' \xe5\x91\x8a', ' \xe8\xa6\x81', ' \xe6\x88\x91', ' \xe8\xbf\x99\xe6\xa0\xb7', ' \xe5\x9c\xa8', ' \xe4\xbd\xa0\xe4\xbb\xac', ' \xe7\x88\xb1', ' \xe6\xb2\xa1\xe6\x9c\x89', ' \xe9\x9c\x80\xe6\xb1\x82', ' \xe6\x9c\x89', ' \xe5\x8f\xaa', ' \xe6\x83\x85\xe6\x84\x9f', ' \xe7\x9a\x84', ' \xe5\xae\x89\xe6\x94\xbe', ' \xe6\x97\xa0\xe5\xa4\x84', ' \xe5\xa4\xab\xe5\xa6\xbb', ' \xe4\xb8\xb4\xe6\x97\xb6', ' \xe5\x86\x9c\xe6\xb0\x91\xe5\xb7\xa5', ' \xe5\x91\xa2', ' \xe5\x98\x9b', ' \xe5\xb9\xb2', ' \xe6\x89\x8b', ' \xe4\xbd\xa0', ' \xe5\xa5\xb3', ' \xe7\xbe\x8e', ' \xe5\x95\x8a', ' \xe9\x95\xbf', ' \xe6\xaf\x9b\xe6\x8c\xba', ' \xe5\xa6\xb9\xe5\xad\x90', ' \xe6\x80\xa7\xe6\x84\x9f', ' \xe4\xbb\x80\xe4\xb9\x88', ' \xe8\xb0\x88', ' 120', ' \xe4\xb8\x8d\xe5\xa4\x9f', ' \xe4\xbd\x93\xe9\x87\x8d', ' \xe6\x80\x81\xe5\xba\xa6', ' \xe4\xba\x86', ' \xe5\xa4\xb4', ' \xe8\xb5\xb7', ' \xe4\xb8\x8d', ' \xe6\x8a\xac', ' \xe9\x83\xbd', ' \xe8\xbe\x88\xe5\xad\x90', ' \xe8\xbf\x99', ' \xe4\xbc\xb0\xe8\xae\xa1']
#
#
# for elem in x:
#     print elem,len(elem.decode("utf-8"))
#
# # print len(u"你")
#
# def passedItem(item):
#     try:
#         return len(item) >= 2  # can be more a complicated condition here
#     except ValueError:
#         return False
# ss = [filter(passedItem, item) for item in x]
# print ",".join(ss)
# print ",".join(x)
# # print [elem for elem in x if len(item.decode("utf-8")) > 1]
# # for elem in words:
# #     print elem,len(elem)
#
#
#
#
#
#
# # filter out some unwanted tags
# def passed(item):
#     try:
#         return item != "techbrood"  # can be more a complicated condition here
#     except ValueError:
#         return False
#
#
# org_words = [["this", "is"], ["demo", "from"], ["techbrood"]]
# words = [filter(passed, item) for item in org_words]
# print words