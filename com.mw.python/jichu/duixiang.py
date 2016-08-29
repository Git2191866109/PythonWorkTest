#!/usr/bin/enr python
# encoding:utf-8

a = 10
b = a
print a is b

c = 1 + 6
print a is c
print b is c
print id(a)
print id(b)
print id(c)


# 接受一个数的参数,判断类型
def displayNumType(num):
    print num, ' is '
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num)._name_
    else:
        print 'not a number at all'


# displayNumType(9)
displayNumType('xxx')
# displayNumType(-2.1 + 1.3j)
