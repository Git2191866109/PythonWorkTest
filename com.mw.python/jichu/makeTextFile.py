#!/usr/bin/enr python
# encoding:utf-8
'makeTextFIle.py -- create text file'

import os

ls = os.linesep
fname = "/Users/mawei/Documents/PycharmProjects/PythonWorkTest/com.mw.python/jichu/testwrite"

# get filename
while True:
    if os.path.exists(fname):
        print "error: '%s' already exists" % fname
    else:
        break

# get file content
all = []
print "\nEnter lines ('.' by itself to quit).\n"
# 循环直到user停止输入
while True:
    entry = raw_input("> ")
    if entry == '.':
        break
    else:
        all.append(entry)

# 将内容写入文件
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'
