# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput
import time
import sys

baseurl = "http://www.tianya.cn/"

#input = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid_20180103")
input = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-error")

count = 1
flag = False
for uuid in input:  
    if uuid != '' and uuid != None:
        try:
            uuid = uuid.replace('\n','').replace('\r','')
            result = uuid

            if (uuid == "17314108"):
                flag = True
                continue
            if flag == False:
                continue
            response = urllib.request.urlopen(baseurl+uuid + "/bbs")
            buff = response.read()
            #显示
            html = buff.decode("utf8")
            array1 = html.split("<p><span>注册日期</span>")
            array2 = array1[1].split("</p>")

            response.close()
            print( uuid + "\t" + array2[0])
            sys.stdout.flush()

        except:
            print( uuid + "\terror")
            sys.stdout.flush()
