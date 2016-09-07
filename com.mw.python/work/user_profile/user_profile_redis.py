#!/usr/bin/python
# -*- coding:utf-8 -*-
import traceback
import logging as log
import numpy as np

from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql.types import *


# import redis


def user_model_computation(user_tags, model):
    userprofile = np.array(user_tags)
    user_weights = userprofile.dot(model)
    print "user_weights: ", user_weights
    category_list = [81, 20, 36, 42, 29, 18, 4, 22, 34, 101, 19, 5, 3, 21, 28, 44, 49, 57, 74, 75, 77, 82, 85, 103, 105]
    category_weights = []
    for i in xrange(len(category_list)):
        category_weights.append((category_list[i], user_weights[i]))
    ###排序###
    category_weights_sorted = sorted(category_weights, key=lambda x: x[1], reverse=True)
    return userprofile, category_weights_sorted


# 将tag 作为一个标签list，然后遍历，用户的tag也是一个数组用户的标签和list中的tagid相对应，对应上的就是该tag，没有 就是0
# 最后得到一个用户的tag标签列表  1 * 85
def tagprocess(tags, user_tags):
    temp_list = [0] * len(tags)
    for i in xrange(0, len(tags)):
        # 判断用户哪些标签在list列表中
        for j in xrange(0, len(user_tags)):
            if (user_tags[j] == tags[i]):
                temp_list[i] = user_tags[j]
            else:
                temp_list[i] == 0
    return temp_list


def format_tag(taglist):
    fond_tags = []
    tag_path = "/mnt/patriot/feed/mw/data/tag_list_v5.npy"
    tags = np.load(tag_path)
    fond_tags = tagprocess(tags,taglist)
    return fond_tags

def parse(line):
    try:
        result = ''
        result += 'uid:%s:utag:%s' % (line[0], line[1])
        return result
    except Exception, e:
        print "exception:", e
        return None





try:
    print "output......processTags...processTags....开始调用...."
    def processTags(iterator):
        print "output......processTags...processTags....开始调用....",iterator
        for x in iterator:
            print "output......print...processTags....success....", x
except:
    traceback.print_exc()
    print "output....processTags.........出错了"
    x = -1


if __name__ == "__main__":
    # model_path = "E:\mojiworkspace\PythonWorkTest\com.mw.python\test\model_v5.npy"
    # tag_path = "E:\mojiworkspace\PythonWorkTest\com.mw.python\test\tag_list_v5.npy"
    model_path = "/mnt/patriot/feed/mw/data/model_v5.npy"
    tag_path = "/mnt/patriot/feed/mw/data/tag_list_v5.npy"
    # 配置spark的环境
    conf = SparkConf().setMaster("yarn-client").setAppName("FEED_ACCESS_CLICK").set("spark.driver.cores", '3') \
        .set("spark.executor.memory", '14g').set("spark.driver.memory", '6g').set("spark.executor.instances", '16') \
        .set("spark.executor.cores", '3').set("spark.driver.maxResultSize", '4g').set("spark.akka.frameSize", '100') \
        .set("spark.rdd.compress", "true").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = HiveContext(sc)
    sqlContext.sql("use moji")
    # ------------------------从hive中得到选取用户的uid和tagid，这是用户画像已经搞好的，哪些用户喜欢的那些tag分类------------------------- #
    # 从hive中获取用户和用户标签的数据
    filePath = "/mnt/mw/data"
    try:
        hql = "select uid,tagid from user_profile_selected"
        # user_select = sqlContext.sql(hql).map(lambda line: line).saveAsTextFile(filePath)
        # user_select = sqlContext.sql(hql).map(lambda line: line).collect()
        # user_select = sqlContext.sql(hql).map(lambda x: (x.uid, x.tagid)).groupByKey().mapValues(list).map(parse).collect()
        user_select = sqlContext.sql(hql).map(lambda x: (x.uid, x.tagid)).groupByKey().mapValues(list).map(parse).saveAsTextFile(filePath)
        # print "output......print.......success....", user_select
        # print "output......print.......success....", user_select
    except:
        traceback.print_exc()
        print "output.............出错了"
        user_select = -1

    # 上面得到的是
    # print "output.........foreachPartition....执行"
    # result = user_select.foreachPartition(processTags)
    # user_select.foreach(processTags)

    # print "output.........result....执行了",result
    # ["uid:165262092:utag:[u'11', u'7', u'13', u'3', u'6', u'54', u'71']",
    #  "uid:212137205:utag:[u'13', u'71', u'7', u'11', u'3', u'56', u'6', u'54']"]
    # print "output.........foreachPartition....执行了"

    # 直接得到用户的tag
    user_tags = []
    ### 用户的tag标签总数 ###
    # tags = np.load(tag_path)
    # 用户的模型是 85 * 25 的  tag * model = 1*25 的标签列表，这就是要存入redis中的
    # user_tags = tagprocess(user_tags, tags)
    # 将用户的tags和读取的model传入计算模型的方法
    ### 用户的model ###
    # model = np.load(model_path)
    # print "recommend_model: ", model

    result_tag = {}
    # result_tag = user_model_computation(user_tags, model)
    # ------------------------保存至redis------------------------- #
    # redclient = redis.Redis(host='192.168.1.11', port=6381, db=3, password='mojichina')  # local test redis
    # redclient.append(result_tag)
    # 查看格式
