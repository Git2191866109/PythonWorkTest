# !/usr/bin/python

# -*- coding:utf-8 -*-
import sys
import time
import traceback

import MySQLdb
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql.types import *


def getfixeddate(fixhours, fixdays=0):
    return time.strftime("%Y-%m-%d", time.localtime(getfixedTimeStamp(fixhours, fixdays)))


def getfixeddate1(fixhours, fixdays=0):
    return time.strftime("%Y%m%d", time.localtime(getfixedTimeStamp(fixhours, fixdays)))


def getfixedTimeStamp(fixhours, fixdays=0):
    return int(time.time() + 3600 * fixhours + 86400 * fixdays)


if __name__ == "__main__":
    j = -3;
    if len(sys.argv) == 2:
        j = -1 * int(sys.argv[1])

    date0 = getfixeddate(8, j)
    conf = SparkConf().setMaster("yarn-client").setAppName("FEED_READ_AVG").set("spark.driver.cores", '3') \
        .set("spark.executor.memory", '14g').set("spark.driver.memory", '6g').set("spark.executor.instances", '16') \
        .set("spark.executor.cores", '3').set("spark.driver.maxResultSize", '4g').set("spark.akka.frameSize", '100') \
        .set("spark.rdd.compress", "true").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    sqlContext.sql("use moji")

    # 右上角的点击量
    try:
        menu_click = sqlContext.sql(
            "select uid from commonlog_feeds where key='FEED_ACCESS_CLICK' and date='" + date0 + "'").distinct().count()
    except:
        menu_click = -1

    # 上下滑动的点击量
    try:
        up_down_click = sqlContext.sql(
            "select uid from commonlog_feeds where key='FEED_ACCESS_CLICK' and date='" + date0 + "'").distinct().count()
    except:
        up_down_click = -1

    # ------------------------保存至MySQL------------------------------------
    try:
        conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',
                               passwd='BigDataMoji', db='tblu', port=3306, charset="utf8")
        cursor = conn.cursor()

        # print "click_num...%s" %(click_num)
        # print "date..."+ date0
        # content = [(1, click_num, date0)]
        # print content
        sql = "insert into `feed_access_click` (`feed_access_click`,`date`) values(%s,'%s')" % (click_num, date0)
        cursor.execute(sql)
        # cursor.executemany(sql, content)
        conn.commit()

    except:
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()

    sc.stop()
