# -*- coding:utf-8 -*-
import time
#print  time.time()
#print time.localtime()

print int(time.time() + 3600 * 8 + 86400 * 3)

def getfixeddate(fixhours, fixdays=0):
    print time.strftime("%Y-%m-%d", time.localtime(getfixedTimeStamp(fixhours, fixdays)))
    return time.strftime("%Y-%m-%d", time.localtime(getfixedTimeStamp(fixhours, fixdays)))


def getfixeddate1(fixhours, fixdays=0):
    print time.strftime("%Y%m%d", time.localtime(getfixedTimeStamp(fixhours, fixdays)))
    return time.strftime("%Y%m%d", time.localtime(getfixedTimeStamp(fixhours, fixdays)))


def getfixedTimeStamp(fixhours, fixdays=0):
    print int(time.time() + 3600 * fixhours + 86400 * fixdays)
    return int(time.time() + 3600 * fixhours + 86400 * fixdays)

# 比如今天是2016-08-26，如果j= 3 取的是26号的后三天即：2016-08-29，如果j=-3，取得是26号的前三天2016-08-23
j = -7
print j

date0 = getfixeddate(8, j)

print date0