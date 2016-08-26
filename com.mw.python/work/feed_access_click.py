#!/usr/bin/python
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


# 主要功能是统计Android用户的右上角的新闻入口点击量
if __name__ == "__main__":
    j = -3;
    if len(sys.argv) == 2:
        j = -1 * int(sys.argv[1])

    date0 = getfixeddate(8, j)
    conf = SparkConf().setMaster("yarn-client").setAppName("FEED_ACCESS_CLICK").set("spark.driver.cores", '3') \
        .set("spark.executor.memory", '14g').set("spark.driver.memory", '6g').set("spark.executor.instances", '16') \
        .set("spark.executor.cores", '3').set("spark.driver.maxResultSize", '4g').set("spark.akka.frameSize", '100') \
        .set("spark.rdd.compress", "true").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    sqlContext.sql("use moji")

    ### android 新闻入口点击量###
    try:
        click_num = sqlContext.sql("select uid from commonlog_feeds where key='FEED_ACCESS_CLICK' and date='" + date0 + "'").distinct().count()
    except:
        click_num = -1

    # ------------------------保存至MySQL-------------------------------------
try:
    conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',
                           passwd='BigDataMoji', db='tblu', port=3306, charset="utf8")
    cursor = conn.cursor()
    content = [(1, click_num, date0)]
    sql = """insert into feed_access_click(click_num,date) values(%s,%s)"""  ##""" """
    cursor.executemany(sql, content)
    conn.commit()
except:
    traceback.print_exc()
finally:
    print date0, click_num
    cursor.close()
    conn.close()

sc.stop()







