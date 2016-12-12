#!/usr/bin/python
# -*- coding:utf-8 -*-


# 在Python中，当你排序一个元组时，如下所示：

items = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
# [(0, 'B'), (0, 'a'), (1, 'A'), (1, 'B'), (2, 'A')]
print sorted(items)

# 默认情况下，sort和sorted内建函数会优先排序第一个元素，然后再排序第二个元素，大写字母会排在小写字母前面。当你想要不区分大小写排序时，可能会按如下写代码：
# print sorted(items, key=str.lower)
# 出现了错误，lower需要的是字符串对象，但是接收到了元组。下面的应用lamdba，返回一个元组：
print sorted(items, key=lambda x: (x[0], x[1].lower()))
# [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]
# 我确定你知道可以通过
# sorted(items, reverse=True, ...)
# 将其反转，但是如果你想要依赖你提供的key来获得不同的排序顺序时，该怎么办呢？使用lambda函数返回一个元组可以实现，下面是一个更高级的结构排序
#
peeps = [{'name': 'Bill', 'salary': 1000}, {'name': 'Bill', 'salary': 500}, {'name': 'Ted', 'salary': 500}]
print sorted(peeps, key=lambda x: (x['name'], x['salary']))
# [{'salary': 500, 'name': 'Bill'}, {'salary': 1000, 'name': 'Bill'}, {'salary': 500, 'name': 'Ted'}]
# 如果你想要使salary逆序，只需要如下改动：
#
print sorted(peeps, key=lambda x: (x['name'], -x['salary']))
# [{'salary': 1000, 'name': 'Bill'}, {'salary': 500, 'name': 'Bill'}, {'salary': 500, 'name': 'Ted'}]


myList = [('dungeon',7),('winterfell',4),('bran',9),('meelo',6)]
print sorted(myList, key=lambda x:x[1])