# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput
import time

def merge_file():
    input1 = open("/Users/conght/WORK/crawls/TianYa/jinghua")
    input2 = open("/Users/conght/WORK/crawls/TianYa/jinghuaPublish")

    dict1 = {}

    for line in input1:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                url = "http://bbs.tianya.cn"+line.split("\t")[1]
                dict1[url] = line
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)

    for line in input2:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                url = line.split("\t")[0]
                value = dict1.get(url, "")
                if value != "":
                    print(value+"\t"+line.split("\t")[1].split("：")[1].split(" ")[0])
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)

    input1.close()
    input2.close()

def merge_file2():
    input1 = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/wordcount")
    input2 = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/jinghua-common-info")

    dict1 = {}

    for line in input1:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                url = line.split("\t")[0]
                dict1[url] = line.split("\t")[1]
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)

    for line in input2:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                url = "http://bbs.tianya.cn"+line.split("\t")[1]
                value = dict1.get(url, 0)
                print(line+"\t"+str(value))
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)

    input1.close()
    input2.close()

def CalNumbers():
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/jinghua-common-info")
    num_dict = {}
    for line in input:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                time = "-".join(line.split("\t")[6].split("-")[:-1])
                count = num_dict.get(time, 0)
                num_dict[time] = count + 1
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)
    for (d,x) in num_dict.items():
        print(d+"\t"+str(x))

def CalClickCount():
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/jinghua-common-info")
    num_dict = {}
    for line in input:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                time = "-".join(line.split("\t")[6].split("-")[:-1])
                count = num_dict.get(time, 0)
                num_dict[time] = count + int(line.split("\t")[3])
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)
    for (d,x) in num_dict.items():
        print(d+"\t"+str(x))

def CalReplyCount():
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/jinghua-common-info")
    num_dict = {}
    for line in input:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                time = "-".join(line.split("\t")[6].split("-")[:-1])
                count = num_dict.get(time, 0)
                num_dict[time] = count + int(line.split("\t")[4])
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)
    for (d,x) in num_dict.items():
        print(d+"\t"+str(x))

def CalRegisterTimeDistrube():
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/registertime")
    class1 = "2017-12-20"
    class2 = "2017-12-01"
    class3 = "2017-10-01"
    class4 = "2017-07-01"
    class5 = "2017-01-01"
    class6 = "2016-01-01"
    for line in input:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                time = "-".join(line.split("\t")[1].split(" ")[0].split("-")[:-1])
                if (time > class1):
                    print(line+"\t1")
                elif time > class2:
                    print(line+"\t2")
                elif time > class3:
                    print(line+"\t3")
                elif time > class4:
                    print(line+"\t4")
                elif time > class5:
                    print(line+"\t5")
                elif time > class6:
                    print(line+"\t6")
                else:
                    print(line+"\t7")
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)

def CalWordCount():
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/jinghua-common-info")
    num_dict = {}
    for line in input:  
        if line != '' and line != None:
            try:
                line = line.replace('\n','').replace('\r','')
                time = "-".join(line.split("\t")[6].split("-")[:-1])
                count = num_dict.get(time, [0,0])
                count[0] = count[0] + 1
                count[1] = count[1] + int(line.split("\t")[7])
                num_dict[time] = count
                
            except:
                pass
                #print(uuid + "\t" + "error")
                #time.sleep(3)
    for (d,x) in num_dict.items():
        print(d+"\t"+str(x[0])+"\t"+str(x[1])+"\t"+str(x[1]//x[0]))

CalWordCount()