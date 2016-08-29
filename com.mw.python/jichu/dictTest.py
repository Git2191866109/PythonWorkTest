#!/usr/bin/python
# -*- coding:utf-8 -*-

dict1 = {}
dict2 = {'name': 'earth', 'port': 80}
print dict1
print dict2
fdict = dict((['x', 1], ['y', 2]))
print fdict

ddict = {}.fromkeys(('x', 'y'), (-1))
edict = {}.fromkeys(('foo', 'bar'))  # 没有给出值，默认为None
print ddict
print edict

for key in dict2.keys():
    print 'key=%s,value=%s' % (key, dict2[key])
print 'host %s is running on port %d' % (dict2['name'], dict2['port'])

print 'name' in dict2
