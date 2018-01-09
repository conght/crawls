# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput

#input = open("/Users/conght/WORK/crawls/TianYa/datasets/user_artical_list")
input = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-articlelist")

for uuid in input:
    if uuid != '' and uuid != None:
        try:
            uuid = uuid.replace('\n','').replace('\r','')
            array1 = uuid.split('\t')
            array1 = array1[:-1]
        
            print(array1[0] + "\t" + str(len(array1) - 1))

        except:
            print(uuid + "\t" + "error")
