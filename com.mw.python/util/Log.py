# -*-coding:UTF-8-*-
__author__ = 'chx'

import logging
import logging.config
import datetime
import os

class Logger:
    '''
    日志类
    '''
    def __init__(self, aName):
        """
        初始化对象
        """
        self.iName = aName
        # info
        self.iLogInfo = logging.getLogger(self.iName + "-info")
        self.iLogInfo.setLevel(logging.INFO)
        # error
        self.iLogErr = logging.getLogger(self.iName + "-error")
        self.iLogErr.setLevel(logging.ERROR)
        # console输出流
        self.sh = logging.StreamHandler()
        self.sh.setLevel(logging.DEBUG)
        # 文件输出流
        prjPath = os.getcwdu()
        logDir = prjPath + "/logs/" + datetime.datetime.now().strftime("%Y%m")
        if False == os.path.exists(logDir) :
            os.makedirs(logDir)
        #print prjDir
        infoUrl = "%s/info_%s.log" % (logDir, datetime.datetime.now().strftime("%Y%m%d"))
        errUrl = "%s/error_%s.log" % (logDir, datetime.datetime.now().strftime("%Y%m%d"))
        self.fhInfo = logging.FileHandler(infoUrl)
        self.fhErr = logging.FileHandler(errUrl)
        # 输出格式
        self.format = logging.Formatter("[%(asctime)s](%(levelname)s) %(message)s")
        self.sh.setFormatter(self.format)
        self.fhInfo.setFormatter(self.format)
        self.fhErr.setFormatter(self.format)
        # 添加控制器
        self.iLogInfo.addHandler(self.sh)
        self.iLogInfo.addHandler(self.fhInfo)
        self.iLogErr.addHandler(self.sh)
        self.iLogErr.addHandler(self.fhErr)

    def __del__(self):
        """
        析构对象
        """
        # print "== del Logger %s == " % self.iName
        del self.iLogInfo
        del self.iLogErr

    def info(self, msg):
        """
        输出info类日志
        """
        self.iLogInfo.info( "%s : %s " % (self.iName, msg) )

    def error(self ,msg):
        """
        输出error类日志
        """
        self.iLogErr.error( "%s : %s " % (self.iName, msg) )