# encoding:utf-8
# 显示对象的属性,如果没有提供参数,则显示全局变量的名字
print dir()
aList = [1, 2, 3, 4, 5, 6, 7, 8]
# print dir(aList)

# print help(aList)
# len返回对象的长度
print len(aList)
# 以mode（'r'=读,'w'=写）,方式打开一个名为name的文件
print open("zidian.py", 'r')

# 返回一个整形列表,起始为start,结束为stop-1,start默认为0,step为1
print range(1, len(aList), 2)
# str 将一个对象转换成字符串
print str(aList)
# 返回对象的类型
print type(aList)

# 比较两个值:i<0(obj1<obj2) i>0(obj1>obj2)
obj1, obj2 = 12, 34
i = cmp(obj1, obj2)
print i
