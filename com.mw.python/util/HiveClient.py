#!/usr/bin/python
#-*-coding:UTF-8-*-

import pyhs2
from util.Log import Logger


# 构建hive server2连接
aLog = Logger("HiveClient")

class HiveClient:
    def __init__(self, db_host, user, password, database, port=10001, authMechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  authMechanism=authMechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )
        self.cur = self.conn.cursor()

    def execHql(self, aHql):
        """
            执行HQL指令
        """
        aLog.info(" --execHQL-- %s" % aHql)
        aLog.info(aHql)
        self.cur.execute(aHql)
        return self.cur.fetch()


    def close(self):
        """
        close connection
        """
        self.conn.close()

def __del__(self):
    aLog.info("del HiveClient")

