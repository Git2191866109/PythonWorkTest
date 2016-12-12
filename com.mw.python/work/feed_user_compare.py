#!/usr/bin/python
# -*- coding:utf-8 -*-
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql.types import *
import traceback

if __name__ == "__main__":

    conf = SparkConf().setMaster("yarn-client").setAppName("FEED_READ_AVG").set("spark.driver.cores", '3') \
        .set("spark.executor.memory", '14g').set("spark.driver.memory", '6g').set("spark.executor.instances", '16') \
        .set("spark.executor.cores", '3').set("spark.driver.maxResultSize", '4g').set("spark.akka.frameSize", '100') \
        .set("spark.rdd.compress", "true").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    sqlContext.sql("use moji")

    #  commonlog_partly 表
    try:  # 平均在feed2.0停留时长
        filePath = "/mnt/"
        hsql = "select tempm_uid.pre_uid puid,com_part.du cdu,com_part.value cvalue from (select uid pre_uid from tempm_uid) tempm_uid left join commonlog_android com_part on tempm_uid.pre_uid = com_part.uid where com_part.stat_date between '2016-08-29' and '2016-09-04' and key='FEED_STAY_TIME' and com_part.value in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62,  64, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 105, 142, 145, 148, 149, 150, 155, 160, 162) group by tempm_uid.pre_uid,com_part.du,com_part.value limit 100"
        a = sqlContext.sql(hsql).map(lambda x: (x.uid, x.du, x.value)).saveAsTextFile(filePath)
        print "打印的结果，，，，，", a

    except:
        traceback.print_exc()
        # a = -1

    # ------------------------保存至MySQL------------------------------------
    # try:
    #     conn = MySQLdb.connect(host='ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn', user='moji',
    #                            passwd='BigDataMoji', db='tblu', port=3306, charset="utf8")
    #     cursor = conn.cursor()
    #     content = [(3, avg3, date0)]
    #     sql = """insert into feeds_stay_time(platform,avg,date) values(%s,%s,%s)"""
    #     cursor.executemany(sql, content)
    #     conn.commit()
    # except:
    #     traceback.print_exc()
    # finally:
    #     print date0
    #     cursor.close()
    #     conn.close()

    sc.stop()
