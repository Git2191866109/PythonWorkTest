# !/usr/bin/python
# -*- coding:utf-8 -*-
from operator import add
import sys, re, json, time, os
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql.types import *

import MySQLdb
import traceback


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
    # date1 = getfixeddate(8,j+1)

    conf = SparkConf().setMaster("yarn-client").setAppName("FEED_READ_AVG").set("spark.driver.cores", '3') \
        .set("spark.executor.memory", '14g').set("spark.driver.memory", '6g').set("spark.executor.instances", '16') \
        .set("spark.executor.cores", '3').set("spark.driver.maxResultSize", '4g').set("spark.akka.frameSize", '100') \
        .set("spark.rdd.compress", "true").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    sqlContext.sql("use moji")

    # ------commonlog_partly 表
    try:  # 平均阅读文章时长
        a = sqlContext.sql(
            "select uid,du from commonlog_partly where key='feed_article_stay_time' and date='" + date0 + "'").map(
            lambda x: (x.uid, float(x.du))) \
            .filter(lambda (x, y): y > 0 and y < 1200000).reduceByKey(add, 200).map(lambda (x, y): (y, 1)).reduce(
            lambda (x1, y1), (x2, y2): (x1 + x2, y1 + y2))
        avg1 = float(a[0]) / float(a[1])
    except:
        avg1 = -1
    try:  # 平均在feed2.0停留时长
        a = sqlContext.sql(
            "select uid,du from commonlog_partly where key='FEED_STAY_TIME' and date='" + date0 + "'").map(
            lambda x: (x.uid, float(x.du))) \
            .filter(lambda (x, y): y > 0 and y < 200).reduceByKey(add, 200).map(lambda (x, y): (y, 1)).reduce(
            lambda (x1, y1), (x2, y2): (x1 + x2, y1 + y2))
        avg3 = float(a[0]) * 1000 / float(a[1])
    except:
        avg3 = -1

    # ------commonlog_ios 表
    try:
        i = sqlContext.sql(
            "select uid,du from commonlog_ios where key='feed_article_stay_time' and date='" + date0 + "'").map(
            lambda x: (x.uid, float(x.du))) \
            .filter(lambda (x, y): y > 0 and y < 1200000).reduceByKey(add, 200).map(lambda (x, y): (y, 1)).reduce(
            lambda (x1, y1), (x2, y2): (x1 + x2, y1 + y2))
        avg2 = float(i[0]) / float(i[1])
    except:
        avg2 = -1

    # ------------------------保存至MySQL------------------------------------
    try:
        conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',
                               passwd='BigDataMoji', db='tblu', port=3306, charset="utf8")
        cursor = conn.cursor()
        content = [(1, avg1, date0), (2, avg2, date0), (3, avg3, date0)]
        sql = """insert into feeds_stay_time(platform,avg,date) values(%s,%s,%s)"""
        cursor.executemany(sql, content)
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        print date0, avg1, avg2
        cursor.close()
        conn.close()

    sc.stop()
