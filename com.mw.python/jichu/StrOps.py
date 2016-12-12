# encoding:utf-8
pyStr = 'python'
pyStr_shuang = "python"
iscool = 'is cool!'
print pyStr[0]
print pyStr_shuang
print pyStr[2:5]
print iscool[:2]
print iscool[3:]
print iscool[-1]
print pyStr + iscool
# *表示字符串重复
print pyStr * 2
print '-' * 20
# 3个引号包含特殊字符
ps3yinhao = '''python ...
is cool'''
print ps3yinhao

strs =str([0, 3, 5, 6])
print strs
print `strs`
print repr(strs)
# 反转字符串
s = 'abcdefg'
print s[::-1]
# 每隔一个取字符
print s[::2]

# 字符串比较
sStr1 = 'strchr'
sStr2 = 'strchr'
print cmp(sStr1, sStr2)