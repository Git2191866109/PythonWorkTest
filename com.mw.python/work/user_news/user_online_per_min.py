#!/usr/bin/python
# -*- coding:utf-8 -*-

# online_path = 'D:\\user_news\\01_08_onlineuid.txt'
import datetime
import time

import itertools

online_path = 'E:\mojiworkspace\PythonWorkTest\com.mw.python\work\user_news\\101_08_onlineuid.txt'


# 处理字符串
def processonline(online_path):
    online_data = [line.strip() for line in open(online_path).readlines()]
    items = []
    dayTime = []
    for item in online_data:
        pitem = item.split("\t")
        if cmp(pitem[4], 'FEEDS_INDEX') == 0:
            items.append(pitem)
        elif cmp(pitem[4], 'FEED_PAGE_CLICK') == 0:
            if int(pitem[5]) == 0:
                items.append(pitem)
        elif cmp(pitem[4], 'FEEDS_CATEGORYL_CLICK') == 0:
            if int(pitem[5]) == 0:
                items.append(pitem)
        elif cmp(pitem[4], 'FEEDS_CATEGORYL') == 0:
            if int(pitem[5]) == 0:
                items.append(pitem)
        dayTime.append(pitem[1])
    # print set(dayTime)
    return items, set(dayTime)


# 每一天的用户数据
def formatitem(items, dayTime):
    list_day_time = []
    for day in dayTime:
        uidTime = {}
        uid_time = []
        for item in items:
            if cmp(item[1], day) == 0:
                # print item[1], day
                yz = datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S").timetuple()
                uid_time.append((int(item[3]), yz[3], yz[4]))
        # 如果第一个相同  则按照元组第2个从大到小 排序
        uidTime[day] = sorted(sorted(list(set(uid_time))), key=lambda x: (x[1], -x[2]))
        list_day_time.append(uidTime)

    return list_day_time


# 每天6~7点每分钟并发访问的人数
def getresult(list_day_time):
    for item in list_day_time:
        # print item
        for key in item:
            # print item[key]
            for i in item[key]:
                tempKey = "%s_%s" % (i[1], i[2])
                print key, tempKey, i[0]



        # result = []
#     for x in list(itertools.combinations(uidTime, 2)):
#     print x[0], x[1]
#     if 0 < abs(x[0][1] - x[1][1]) <= 60:
#         result.append((x[0][0], x[1][0]))
#


if __name__ == "__main__":
    items, dayTime = processonline(online_path)
    list_day_time = formatitem(items, dayTime)
    # print len(list_day_time)
    getresult(list_day_time)




# uidTime[item[1]] = (int(item[3]), datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S"))
# uidTime.append((int(item[3]), time.mktime(time.strptime(item[0], "%Y-%m-%d %H:%M:%S"))))
# uidTime.append((int(item[3]), datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S")))
# uidTime.append((int(item[3]), long(time.mktime(time.strptime(item[0], "%Y-%m-%d %H:%M:%S")))))
# print (int(item[3]),  long(time.mktime(time.strptime(item[0], "%Y-%m-%d %H:%M:%S"))))
