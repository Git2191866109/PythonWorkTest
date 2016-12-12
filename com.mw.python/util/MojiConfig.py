# -*-coding:UTF-8-*-
__author__ = 'chx'

import os,sys,re

class MojiConfig:
    '''
        配置类
    '''
    def __init__(self):
        # 访问HIVE数据库的配置信息
        MojiConfig.HIVE_ETL_USER = 'hadoop'
        MojiConfig.HIVE_ETL_PWD = ''
        MojiConfig.HIVE_ETL_HOST = 'ec2-54-223-210-215.cn-north-1.compute.amazonaws.com.cn'
        MojiConfig.HIVE_ETL_PORT = 10001
        MojiConfig.HIVE_ETL_NAME = 'moji'
        MojiConfig.HIVE_ETL_AUTHMECHANISM = 'PLAIN'

        MojiConfig.HIVE_ETL_HOST2 = 'ec2-54-223-57-88.cn-north-1.compute.amazonaws.com.cn'

        MojiConfig.HIVE_ETL_HOST3 = 'ec2-54-223-100-40.cn-north-1.compute.amazonaws.com.cn'

        # # 访问MONGODB数据库的配置信息(正式的数据库只读)
        MojiConfig.MONGO_HOST = 'ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn'
        MojiConfig.MONGO_PORT = 27017

        # 访问Hbase数据库的配置信息
        MojiConfig.HBASE_HOST = 'ec2-54-223-210-215.cn-north-1.compute.amazonaws.com.cn'
        MojiConfig.HBASE_PORT = 9090
        # MojiConfig.HBASE_HOST = 'ec2-54-223-82-25.cn-north-1.compute.amazonaws.com.cn'
        # MojiConfig.HBASE_PORT = 60000

        DB_CHARSET = 'utf8'
        DB_PORT = '3306'
        DB_HOST = '192.168.1.7'
        DB_USER = 'root'
        DB_PASS = ''
        DB_NAME = 'scrapy_test'
        ##'mysql://root:@192.168.1.7:3306/scrapy_test?charset=utf8'
        MojiConfig.DB_URL = "mysql://%s:%s@%s:%s/%s?charset=%s" % (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, DB_CHARSET)

        # ##'mysql://moji:BigDataMoji@ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn:3306/moji_persona?charset=utf8'
        MojiConfig.DB_URL2 = 'mysql://moji:BigDataMoji@ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn:3306/userinfo?charset=utf8'

        MojiConfig.DB_URL3 = 'mysql://moji:BigDataMoji@ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn:3306/assist?charset=utf8'

        MojiConfig.DB_URL4 = 'mysql://moji:BigDataMoji@ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn:3306/test?charset=utf8'

    @staticmethod
    def getredisParam_test():
        # return {'host':"mojidcR1", 'password':"moji_dcR1", 'port': 6388, 'db':0}
        return {'host':"192.168.1.12", 'password':"mojichina", 'port': 6379, 'db':0}

    @staticmethod
    def getredisParam_read():
        return {'host':"ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn", 'password':"", 'port': 6380, 'db':3}
        # return {'host':"192.168.1.11", 'password':"mojichina", 'port': 6381, 'db':5}
    @staticmethod
    def getIosredisParam_read():
        return {'host':"ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn", 'password':"", 'port': 6380, 'db':2}

    @staticmethod
    def getredisParam():
        return {'host':"ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn", 'password':"", 'port': 6380, 'db':4}
        # return {'host':"192.168.1.11", 'password':"mojichina", 'port': 6381, 'db':5}
    @staticmethod
    def getIosredisParam():
        return {'host':"ec2-54-223-197-216.cn-north-1.compute.amazonaws.com.cn", 'password':"", 'port': 6380, 'db':5}