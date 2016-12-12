#!/usr/bin/python
# -*- coding:utf-8 -*-

# online_path = 'D:\\user_news\\01_08_onlineuid.txt'
import datetime
import time

print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print datetime.datetime.strptime("2016-12-01 06:46:33", "%Y-%m-%d %H:%M:%S")
print datetime.datetime.strptime("2016-12-01 06:46:33", "%Y-%m-%d %H:%M:%S").timetuple()
print datetime.datetime.strptime("2016-12-01 06:47:33", "%Y-%m-%d %H:%M:%S").timetuple()
print datetime.datetime.strptime("2016-12-01 07:47:33", "%Y-%m-%d %H:%M:%S").timetuple()
yuanzutime = datetime.datetime.strptime("2016-12-01 06:47:33", "%Y-%m-%d %H:%M:%S").timetuple()
yuanzutime1 = datetime.datetime.strptime("2016-12-01 06:47:33", "%Y-%m-%d %H:%M:%S").timetuple()
yuanzutime2 = datetime.datetime.strptime("2016-12-01 07:47:33", "%Y-%m-%d %H:%M:%S").timetuple()
yuanzutime2 = datetime.datetime.strptime("2016-12-01 07:47:33", "%Y-%m-%d %H:%M:%S")
yuanzutime3 = datetime.datetime.strptime("2016-12-02 07:47:33", "%Y-%m-%d %H:%M:%S").timetuple()
yuanzutime3 = datetime.datetime.strptime("2016-12-02 07:47:33", "%Y-%m-%d %H:%M:%S")
print (yuanzutime3 - yuanzutime2).days

print yuanzutime[0], yuanzutime[1], yuanzutime[2], yuanzutime[3], yuanzutime[4], yuanzutime[5]
print yuanzutime1[0], yuanzutime1[1], yuanzutime1[2], yuanzutime1[3], yuanzutime1[4], yuanzutime1[5]
# if yuanzutime[2] == yuanzutime1[2]:
#     print yuanzutime1[4] - yuanzutime[4]
#
#
# now = datetime.datetime.now()
# timestamp = time.mktime(now.timetuple())
# # 1481274160.0
# print timestamp
# print time.mktime(time.strptime("2016-12-01 06:46:33", '%Y-%m-%d %H:%M:%S'))
# a = "2011-09-28 10:00:00"
# # 中间过程，一般都需要将字符串转化为时间数组
# print datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
# # 将"2011-09-28 10:00:00"转化为时间戳
# print time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
# # 1317091800.0
# # 将时间戳转化为localtime
# x = time.localtime(1480545993.0)
# print time.strftime('%Y-%m-%d %H:%M:%S', x)


# 转换成时间戳后的差值  《= 60 s不就行了
