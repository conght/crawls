# -*- coding: utf-8 -*-

import json
import fileinput
import time
from datetime import date
import csv

def getRLabel(value):
    if (value <= 10):
        return 5
    if (value <= 30):
        return 4
    if (value <= 90):
        return 3
    if (value <= 180):
        return 2
    return 1

def getFLabel(value):
    if (value == 0):
        return 1
    if (value <= 1000//4):
        return 5
    if (value <= (1000//4)*2):
        return 4
    if (value <= (1000//4)*3):
        return 3
    if (value <= 1000):
        return 2
    return 1

def getTLabel(value):
    if (value >= 80):
        return 5
    if (value >= 50):
        return 4
    if (value >= 30):
        return 3
    if (value >= 15):
        return 2
    return 1

def getRFTLevel(item):
    if (item[1]>=4 and item[3]>=4 and item[5]>=4):
        return 8
    elif (item[1]<4 and item[3]>=4 and item[5]>=4):
        return 7
    elif (item[1]>=4 and item[3]<4 and item[5]>=4):
        return 6
    elif (item[1]<4 and item[3]<4 and item[5]>=4):
        return 5
    elif (item[1]>=4 and item[3]>=4 and item[5]<4):
        return 4
    elif (item[1]<4 and item[3]>=4 and item[5]<4):
        return 3
    elif (item[1]>=4 and item[3]<4 and item[5]<4):
        return 2
    else:
        return 1

#------------------- step.1--------------------#
#registerTimeFile = open("/Users/conght/WORK/crawls/TianYa/datasets/userregistertimeinfowithouterror")
#lastActiveTimeFile = open("/Users/conght/WORK/crawls/TianYa/datasets/userlastactivetimewithouterror")
#articleCountFile = open("/Users/conght/WORK/crawls/TianYa/datasets/userarticalcountwithourerror")
#wordCountFile = open("/Users/conght/WORK/crawls/TianYa/datasets/userarticalwordcountwithouterror")

registerTimeFile = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-registertime-withouterror")
lastActiveTimeFile = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-lastactivetime-withouterror")
articleCountFile = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-artcount")
wordCountFile = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-totalwordcount")


aggData = {}
registerTime = {}
lastActiveTime = {}
articleCount = {}
wordCount = {}
baseTimeStruct = time.strptime('2017-09-30', '%Y-%m-%d')
baseData = date(baseTimeStruct.tm_year, baseTimeStruct.tm_mon, baseTimeStruct.tm_mday)

maxF = 0
minF = 100

#------------------- step.2--------------------#
for line in registerTimeFile:
    line = line.replace('\n','').replace('\r','')
    array1 = line.split('\t')
    registerTime[array1[0]] = array1[1]

for line in lastActiveTimeFile:
    line = line.replace('\n','').replace('\r','')
    array1 = line.split('\t')
    lastActiveTime[array1[0]] = array1[1]

for line in articleCountFile:
    line = line.replace('\n','').replace('\r','')
    array1 = line.split('\t')
    articleCount[array1[0]] = array1[1]

for line in wordCountFile:
    line = line.replace('\n','').replace('\r','')
    array1 = line.split('\t')
    wordCount[array1[0]] = array1[1]

#------------------- step.3--------------------#

for (uuid,rtime) in registerTime.items():
    item = [None] * 8
    ltime = lastActiveTime.get(uuid, None)
    if ltime == None or ltime == '':
        continue
    #print(ltime)
    ltime_struct = time.strptime(ltime.split(' ')[0], '%Y-%m-%d')
    ldata = date(ltime_struct.tm_year, ltime_struct.tm_mon, ltime_struct.tm_mday)
    item[0] = (baseData-ldata).days
    item[1] = getRLabel(item[0])

    rtime_struct = time.strptime(rtime.split(' ')[0], '%Y-%m-%d')
    rdata = date(rtime_struct.tm_year, rtime_struct.tm_mon, rtime_struct.tm_mday)
    l_r_data_detla = (ldata - rdata).days
    articleCountItem = articleCount.get(uuid, None)
    if articleCountItem == None:
        continue
    if int(articleCountItem) == 0:
        item[2] = 0
    else:
        item[2] = l_r_data_detla // int(articleCountItem)
    item[3] = getFLabel(item[2])

    #if item[2] > maxF:
    #    maxF = item[2]
    #if item[2] < minF:
    #    minF = item[2]

    wordCountItem = wordCount.get(uuid, '0')
    if int(articleCountItem) == 0:
        item[4] = 0
    else:
        item[4] = int(wordCountItem) // int(articleCountItem)
    item[5] = getTLabel(item[4])
    item[6] = item[1]*100 + item[3]*10 + item[5]
    item[7] = getRFTLevel(item)
    aggData[uuid] = item

#------------------- step.4--------------------#

for (uuid, item) in aggData.items():
    print(uuid+"\t"+str(item[0])+"\t"+str(item[1])+"\t"+str(item[2])+"\t"+str(item[3])+"\t"+str(item[4])+"\t"+str(item[5])+"\t"+str(item[6])+"\t"+str(item[7]))

errorFile = open("rft_info.csv", 'w')  
writeCSV = csv.writer(errorFile)
writeCSV.writerow(["用户id","R","R分类","F","F分类","T","T分类","RFT","RFT分类"])
for (uuid, item) in aggData.items():
    row = []
    row.append(uuid)
    row.append(item[0])
    row.append(item[1])
    row.append(item[2])
    row.append(item[3])
    row.append(item[4])
    row.append(item[5])
    row.append(item[6])
    row.append(item[7])
    #print(uuid+"\t"+str(item[0])+"\t"+str(item[1])+"\t"+str(item[2])+"\t"+str(item[3])+"\t"+str(item[4])+"\t"+str(item[5])+"\t"+str(item[6])+"\t"+str(item[7]))
    writeCSV.writerow(row)

errorFile.close()

#print(str(len(registerTime)))
#print(str(len(lastActiveTime)))
#print(str(len(articleCount)))
#print(str(len(wordCount)))
#print(str(len(aggData)))
