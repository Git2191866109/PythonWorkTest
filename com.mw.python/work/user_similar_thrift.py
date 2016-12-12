#!/usr/bin/python
# -*- coding:utf-8 -*-

from util.Log import Logger
from hbase.ttypes import *
from util.MojiConfig import MojiConfig
from util.Log import Logger
from util import HbaseClient
import datetime, os

iLog = Logger("Similars")

thrift_host = "54.223.210.215"
port = 9090




# if __name__ == "__main__":
