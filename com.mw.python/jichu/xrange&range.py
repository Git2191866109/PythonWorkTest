# -*- coding:utf-8 -*-
# xrange做循环的性能比range好，尤其是返回很大的时候，尽量用xrange吧，除非你是要返回一个列表。
# 函数说明：range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个序列。
print range(5)
print range(1, 5)
print range(0, 6, 2)

# 函数说明：xrange用法与range完全相同，所不同的是生成的不是一个数组，而是一个生成器。
print xrange(5)
print list(xrange(5))
print xrange(1, 5)
print list(xrange(1, 5))
print xrange(0, 6, 2)
print list(xrange(0, 6, 2))
# 要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间，这两个基本上都是在循环的时候用：
for i in range(0, 3):
    print i
for i in xrange(0, 3):
    print i
# 这两个输出的结果都是一样的，实际上有很多不同，range会直接生成一个list对象：
a = range(0, 100)
print type(a)
print a
print a[0], a[1]
# 而xrange则不会直接生成一个list，而是每次调用返回其中的一个值：
a = xrange(0, 100)
print type(a)
print a
print a[0], a[1]
