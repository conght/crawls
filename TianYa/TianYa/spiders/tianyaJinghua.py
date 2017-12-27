# -*- coding:utf-8 -*-  

from scrapy.loader import ItemLoader
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from TianYa.items import TianyaItem, TianyaUserItem
import scrapy
import lxml.html as lh
import sys
import time
import os
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urljoin
from xml.dom.minidom import parse
import xml.dom.minidom
from imp import reload
import random
import time

class tianyaBBSspider(CrawlSpider):

    reload(sys)
    #sys.setdefaultencoding('utf8')
    
    #爬虫名称，非常关键，唯一标示
    name = "tianyaJinghua"

    #域名限定
    allowed_domains = ["bbs.tianya.cn","www.tianya.cn"]

    #爬虫的爬取得起始url
    start_urls = [

            #天涯论坛热帖榜  可以写多个用，分隔
            "http://bbs.tianya.cn/list.jsp?item=funinfo&grade=1&order=1",
         ]
    baseurl = 'http://bbs.tianya.cn'

    def parse(self, response):
        print(response.url)
        #选择器
        sel = Selector(response)
        item =  TianyaItem()
        
        #文章url列表     
        article_url = sel.xpath('//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[1]/a/@href').extract()     
        author_url = sel.xpath('//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[2]/a/@href').extract()
        click_num = sel.xpath('//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[3]/text()').extract()
        reply_num = sel.xpath('//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[4]/text()').extract()
        create_time = sel.xpath('//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[5]/text()').extract() 

        #下一页地址
        next_page_url = sel.xpath('//div[@class="short-pages-2 clearfix"]/div/a[last()]/@href').extract()
        
        for i in range(len(article_url)):
            print("result"+"\t"+article_url[i]+"\t"+author_url[i]+"\t"+click_num[i]+"\t"+reply_num[i]+"\t"+create_time[i])

        if next_page_url[0]:
            request = scrapy.Request(urljoin(self.baseurl,next_page_url[0]),callback=self.parse)
            yield request
