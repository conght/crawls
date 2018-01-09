# -*- coding: utf-8 -*-


import urllib.request
import json
import fileinput
import sys

baseurl = "http://www.tianya.cn/api/bbsuser?method=userinfo.ice.getUserTotalArticleList&params.pageSize=100&params.bMore=true&params.kindId=-1&params.userId="

input = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid_20180103")

for uuid in input:
    if uuid != '' and uuid != None:
        try:
            uuid = uuid.replace('\n','').replace('\r','')
            result = uuid + "\t"

            response = urllib.request.urlopen(baseurl + uuid)

            data = json.loads(response.read())['data']

            rows = data.get('rows', None)
            if (rows != None):

                for item in rows:
                    if (item['item_name'] == "娱乐八卦"):
                        result = result + item['art_id'] + "\t"
            print(result)
            sys.stdout.flush()

        except:
            print(uuid + "\t" + "error")
            sys.stdout.flush()
