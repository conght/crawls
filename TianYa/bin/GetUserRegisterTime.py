# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput
import time

baseurl = "http://www.tianya.cn/"

input = open("/home/conght/CODES/crawls/TianYa/uuid")

for uuid in input:
    if uuid != '' and uuid != None:
        try:
            uuid = uuid.replace('\n','').replace('\r','')
            result = uuid + "\t"

            response = urllib.request.urlopen(baseurl + uuid)
            buff = response.read()
            #显示
            html = buff.decode("utf8")
            array1 = html.split("<p><span>注册日期</span>")
            array2 = array1[1].split("</p>")

            response.close()
            print( uuid + "\t" + array2[0])
            time.sleep(1)

        except:
            print(uuid + "\t" + "error")
