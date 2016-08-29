# encoding:utf-8
myStr = 'hello world'
print myStr
# 表示 %s 用一个字符串来替换，%d表示用一个整形来提替换，%f表示使用一个浮点数来替换
print "%s is number %d!" % ("Python", 2)

counter = 0
miles = 1000.0
name = 'bob'
killomiters = 1.609 * miles
print '%f miles is the same as %f km' % (miles, killomiters)


# 给一些变量赋值
go_surf,get_a_tan_while,boat_size,toll_money = (1,'windsurfing',30.2,-2.00)
print go_surf
print get_a_tan_while

# 将两个对象交换
x,y = 1,3
print x
print y
x,y = y,x #交换
print x
print y
