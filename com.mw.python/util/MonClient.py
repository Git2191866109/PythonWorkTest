#!/usr/bin/python
#-*-coding:UTF-8-*-
__author__ = 'huixia.cao'

import pymongo
from util.Log import Logger

# 构建pymongo连接
iLog = Logger("MonClient")

class MonClient:
    def __init__(self, db_host, port):
        """
        create connection to pymongo
        """
        self.conn = pymongo.MongoClient(host=db_host, port=port)

    def insertone(self, database, collection, data):
        """
        query
        """
        db = self.conn[database]
        query = db[collection]
        try:
            insert = query.insert_one(data)
            iLog.info("mongodb insert one: %s" % data)
        except Exception, e:
            iLog.error("mongodb insert one error:%s" % e)

    def insertmany(self, database, collection, datalist):
        """
        query
        """
        db = self.conn[database]
        query = db[collection]
        try:
            for i in range(len(datalist)):
                insert = query.insert_many(datalist[i])
                iLog.info("mongodb insert many: %s" % datalist[i])
        except Exception, e:
            iLog.error("mongodb insert many error:%s" % e)

    def updateone(self, database, collection, olddata, newdata):
        """
        update
        """
        db = self.conn[database]
        query = db[collection]
        try:
            query.update(olddata, newdata)
            iLog.info("mongodb update: %s" % newdata)
        except Exception, e:
            iLog.error("mongodb update error:%s" % e)

    def findone(self, database, collection, data):
        """
        query
        """
        db = self.conn[database]
        query = db[collection]
        try:
            result = query.find_one(data)
            # iLog.info("mongodb findone: %s" % data)
            return result
        except Exception, e:
            iLog.error("mongodb findone error:%s" % e)

    def find(self, database, collection, data):
        """
        query
        """
        db = self.conn[database]
        query = db[collection]
        try:
            result = query.find(data)
            iLog.info("mongodb find: %s" % result)
            return result
        except Exception, e:
            iLog.error("mongodb find error:%s" % e)

    def delete(self, database, collection, filters):
        """
        query
        """
        db = self.conn[database]
        query = db[collection]
        try:
            result = query.delete_many(filters)
            iLog.info("mongodb find: %s" % result)
            return result
        except Exception, e:
            iLog.error("mongodb find error:%s" % e)


def __del__(self):
    iLog.info("del MonClient")

