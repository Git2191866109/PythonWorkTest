# coding:utf-8

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# 计算上周五天的是哪一天
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
        print start_date
    day_num = start_date.weekday()
    print day_num
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print (datetime.today)
print (get_previous_byday('Tuesday'))
print (get_previous_byday('Tuesday', datetime(2016, 8, 28)))

from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now
print d
print relativedelta(weekday=FR)
# print (d + relativedelta(weekday=FR(-1)))
