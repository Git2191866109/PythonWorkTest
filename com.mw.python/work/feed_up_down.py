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

# 主要功能是统计用户的行为习惯，up 上滑，down 下拉
if __name__ == "__main__":

    j = -3;
    if len(sys.argv) == 2:
        j = -1 * int(sys.argv[1])

    date0 = getfixeddate(8, j)
    # date1 = getfixeddate(8,j+1)

    conf = SparkConf().setMaster("yarn-client").setAppName("FEED_UP").set("spark.driver.cores", '3') \
        .set("spark.executor.memory", '14g').set("spark.driver.memory", '6g').set("spark.executor.instances", '16') \
        .set("spark.executor.cores", '3').set("spark.driver.maxResultSize", '4g').set("spark.akka.frameSize", '100') \
        .set("spark.rdd.compress", "true").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    sqlContext.sql("use moji")

    ###上拉与下滑###
    ### android up###
    try:
        user_sum_up = sqlContext.sql(
            "select uid from commonlog_feeds where (key='feed_page_request' or key='FEED_PAGE_REQUEST') and date='" + date0 + "' and value='2'").distinct().count()
        data_up = sqlContext.sql(
            "select uid from commonlog_feeds where (key='feed_page_request' or key='FEED_PAGE_REQUEST') and value='2' and date='" + date0 + "'").count()
        up_avg_and = float(data_up) / float(user_sum_up)
        # print "up_and:", up_avg_and
    except:
        up_avg_and = -1
        # print "up_avg_and:", -1

    ###android down###
    try:
        user_sum_down = sqlContext.sql(
            "select uid from commonlog_feeds where (key='feed_access_click' or key='FEED_ACCESS_CLICK') and date='" + date0 + "'").distinct().count()
        data_down = sqlContext.sql(
            "select uid from commonlog_feeds where (key='feed_page_request' or key='FEED_PAGE_REQUEST') and value='1' and date='" + date0 + "'").count()
        down_avg_and = float(data_down) / float(user_sum_down)
        # print "down_and:", down_avg_and
    except:
        down_avg_and = -1
        # print " down_avg_and:", -1

    ##ios up##
    try:
        user_sum_up_ios = sqlContext.sql(
            "select uid from commonlog_ios where key='feed_page_request' and date='" + date0 + "' and value='2'").distinct().count()
        data_up_ios = sqlContext.sql(
            "select uid from commonlog_ios where key='feed_page_request' and value='2' and date='" + date0 + "'").count()
        up_avg_ios = float(data_up_ios) / float(user_sum_up_ios)

    except:
        up_avg_ios = -1
        # print "up_avg_ios:", -1

    ###ios down###
    try:
        user_sum_down_ios = sqlContext.sql(
            "select uid from commonlog_ios where key='feed_access_click' and date='" + date0 + "'").distinct().count()
        data_down_ios = sqlContext.sql(
            "select uid from commonlog_ios where key='feed_page_request' and value='1' and date='" + date0 + "'").count()
        down_avg_ios = float(data_down_ios) / float(user_sum_down_ios)
    except:
        down_avg_ios = -1
        # print "down_avg_ios:", -1

    # ------------------------保存至MySQL------------------------------------
    try:
        conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',
                               passwd='BigDataMoji', db='tblu', port=3306, charset="utf8")
        cursor = conn.cursor()
        content = [(1, up_avg_and, date0), (2, down_avg_and, date0), (3, up_avg_ios, date0), (4, down_avg_ios, date0)]
        sql = """insert into feeds_up(platform,avg,date) values(%s,%s,%s)"""  ##""" """
        cursor.executemany(sql, content)
        conn.commit()
    except:
        traceback.print_exc()
    finally:
        print date0, up_avg_and, down_avg_and, up_avg_ios, down_avg_ios
        cursor.close()
        conn.close()

    sc.stop()
