# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput

baseurl = "http://www.tianya.cn/"
input = open("/Users/conght/WORK/crawls/TianYa/datasets/user_artical_list")

for line in input:
    if line != '' and line != None:
        try:
            line = line.replace('\n','').replace('\r','')
            array1 = line.split('\t')
            response = urllib.request.urlopen(baseurl + array1[1])
            buff = response.read()
            #显示
            html = buff.decode("utf8")
            array1 = html.split("<p><span>注册日期</span>")
            array2 = array1[1].split("</p>")

            response.close()
            print( uuid + "\t" + array2[0])
        
            print(array1[0] + "\t" + str(len(array1) - 1))

        except:
            print(uuid + "\t" + "error")
