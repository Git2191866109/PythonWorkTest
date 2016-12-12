#! /usr/bin/env python
#coding=utf-8
__author__ = 'huixia.cao'

import getopt,sys,time
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

class HbaseClient:
    def __init__(self, host, port):
        self.transport = TBufferedTransport(TSocket(host, port))
        self.transport.open()
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)
        self.scan = TScan()

    def createTable(self, table, contents):
        return self.client.createTable(table, [contents])

    def mutateRow(self, table, row, mutations, st):
        return self.client.mutateRow(table, row, mutations, st)

    def getTable(self):
        return self.client.getTableNames()

    def scannerGetList(self, tableName, num):
        id = self.client.scannerOpenWithScan(tableName, self.scan, None)
        return self.client.scannerGetList(id, num)

    def scannerGet(self, tableName):
        id = self.client.scannerOpenWithScan(tableName, self.scan, None)
        return self.client.scannerGet(id)

    def close(self):
        self.transport.close()

