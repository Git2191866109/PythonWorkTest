#!/usr/bin/python
# -*- coding:utf-8 -*
import os
path = 'E:\\MojieWork\\data'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')<0:
            newname=file+'.txt'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
#        print file.split('.')[-1]