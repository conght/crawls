# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput

input = open("/Users/conght/WORK/crawls/TianYa/datasets/user_article_word_count")

dict = {}

for uuid in input:
    if uuid != '' and uuid != None:
        try:
        #print(uuid)
            uuid = uuid.replace('\n','').replace('\r','')
            array1 = uuid.split('\t')
        #array1 = array1[:-1]

            uuid = array1[0].split('.cn/')[1]
            dict[uuid] = dict.get(uuid, 0) + int(array1[1])

        except:
            print(uuid + "\t" + "error")

for (d,x) in dict.items():
    print (d + '\t' + str(x))
