# coding=utf-8
'''
Created on 2014年9月28日

@author: kai.zhang
'''
import redis

def connectredis(rediscfgmap):
    if not rediscfgmap.has_key("host"):
        h = "127.0.0.1"
    else:
        h = rediscfgmap["host"]
        
    if not rediscfgmap.has_key("port"):
        p = 6379
    else:
        p = rediscfgmap["port"]
        
    if not rediscfgmap.has_key("db"):
        d = 0
    else:
        d = rediscfgmap["db"]
        
    if not rediscfgmap.has_key("password"):
        passwd = 0
    else:
        passwd = rediscfgmap["password"]
    #red = redis.Redis(host=h,port=p,db=d,password=passwd,charset='utf-8')
    
    pool = redis.ConnectionPool(host=h,port=p,db=d,password=passwd)
    red = redis.Redis(connection_pool=pool)
    return red