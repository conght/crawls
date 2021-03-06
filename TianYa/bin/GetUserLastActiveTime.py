# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput
import sys

baseurl1 = "http://www.tianya.cn/api/bbsuser?method=userinfo.ice.getUserTotalArticleList&params.pageSize=100&params.bMore=true&params.kindId=-1&params.userId="
baseurl2 = "http://www.tianya.cn/api/bbsuser?method=userinfo.ice.getUserTotalReplyList&params.pageSize=100&params.bMore=true&params.kindId=-1&params.userId="

input = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid_20180103")

for uuid in input:
    if uuid != '' and uuid != None:
        try:
            uuid = uuid.replace('\n','').replace('\r','')
            #result = uuid + "\t"

            response1 = urllib.request.urlopen(baseurl1 + uuid)
            response2 = urllib.request.urlopen(baseurl2 + uuid)

            data1 = json.loads(response1.read())['data']
            data2 = json.loads(response2.read())['data']

            rows1 = data1.get('rows', None)
            rows2 = data2.get('rows', None)
            time1 = ""
            time2 = ""
            if (rows1 != None):
                time1 = rows1[0]['compose_time']
            if (rows2 != None):
                time2 = rows2[0]['reply_time']

            time = time1
            if (time2 > time1):
                time = time2
        
            print(uuid + "\t" + time)
            sys.stdout.flush()

        except:
            print(uuid + "\t" + "error")
            sys.stdout.flush()
