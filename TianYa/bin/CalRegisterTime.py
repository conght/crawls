# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput
import time

input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/registertime")

time_dict = {}
for line in input:  
    if line != '' and line != None:
        try:
            line = line.replace('\n','').replace('\r','')
            uuid = line.split("\t")[0]
            time = line.split("\t")[1]

            timeArray = time.split("-")
            time = timeArray[0]+"-"+timeArray[1]

            count = time_dict.get(time, 0)
            time_dict[time] = (count+1)
            
        except:
            pass
            #print(uuid + "\t" + "error")
            #time.sleep(3)

for (d,x) in time_dict.items():
    print(d+"\t"+str(x))