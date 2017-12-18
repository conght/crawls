# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TianyaPipeline(object):

    def __init__(self):
        #self.file = open('/Users/conght/WORK/crawls/TianYa/tianya.json', 'w')
        self.file = open('/Users/conght/WORK/crawls/TianYa/tianyaUser.json', 'a')
 
 
    #def process_item(self, item, spider):
    #    #line = "%s  %s\n" % (item['company'][0].encode('utf-8'), item['title'][0].encode('utf-8'))
    #    for i in range(len(item['article_name'])):
    #    	line = "%s %s %s %s %s %s %s %s\n" % (item['article_id'][i],item['article_name'][i],item['article_time'][i],item['article_url'][i],item['crawl_time'][i],item['click_num'][i],item['reply_num'][i],item['article_author'][i])
    #    	self.file.write(line)
    #    return item

    def proces_item(self, item ,spider):
        for i in range(len(item['userinfo_url'])):
            line = "%s %s\n" % (item['userinfo_url'][i],item['crawl_time'][i])
            self.file.write(line)
        return item