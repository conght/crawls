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

    user_agent_list = [\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
    
    #爬虫名称，非常关键，唯一标示
    name = "tianyaUser"

    #域名限定
    allowed_domains = ["bbs.tianya.cn","www.tianya.cn"]

    #爬虫的爬取得起始url
    start_urls = [

            #天涯论坛热帖榜  可以写多个用，分隔
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7592206",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7585028",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7580351",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7531426",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7524709",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7504328",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7501067",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7491075",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7490475",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7489807",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7466113",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7453745",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7440342",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7421062",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7418307",
            #"http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7414865",
            "http://bbs.tianya.cn/list.jsp?item=funinfo&order=1&nextid=7407382",

         ]
    baseurl = 'http://bbs.tianya.cn'

    def in_the_set(self, article_time):
        time_str = article_time.split("：")[1]
        timeArray = time.strptime(time_str.strip(), "%Y-%m-%d %H:%M:%S")
        
        if (timeArray.tm_year == 2016 and timeArray.tm_mon >= 11) or (timeArray.tm_year == 2017 and timeArray.tm_mon <= 9):
            if timeArray.tm_wday != 2:
                return False
            if (timeArray.tm_hour < 10 or timeArray.tm_hour > 22):
                return False
            return True
        return False

    def parse(self, response):
        #选择器
        sel = Selector(response)
        item =  TianyaItem()
        
        #文章url列表     
        article_url = sel.xpath('//div[@class="mt5"]/table[@class="tab-bbs-list tab-bbs-list-2"]//tr[@class="bg"]/td[1]/a/@href').extract() 
        #下一页地址
        next_page_url = sel.xpath('//div[@class="short-pages-2 clearfix"]/div/a[last()]/@href').extract()
        
        #print("article_url lens is " + str(len(article_url)))
        print("current article_url is " + response.url)
        for url in article_url:
            #拼接url
            urll = urljoin(self.baseurl,url)
            #调用parse_item解析文章内容
            request = scrapy.Request(urll,callback=self.parse_each_article)
            request.meta['item'] = item
            yield request

        if next_page_url[0]:
            #调用自身进行迭代
            request = scrapy.Request(urljoin(self.baseurl,next_page_url[0]),callback=self.parse)
            yield request

    def parse_each_article(self, response):

        #选择器
        sel = Selector(response)
        article_time =  sel.xpath('//div[@id="post_head"]/div[2]/div[@class="atl-info"]/span[2]/text()').extract()
        if len(article_time) > 0 and self.in_the_set(article_time[0]):
            #用户url列表
            user_url = sel.xpath('//div[@class="atl-item"]/div[@class="atl-head"]/div[@class="atl-info"]/span/a[1]/@href').extract() 
            #下一页地址
            next_page_url = sel.xpath('//div[@class="clearfix"]/div[@class="atl-pages"]/form/a[last()]/@href').extract()
            #是否是最后一页
            is_end_page = sel.xpath('//div[@class="clearfix"]/div[@class="atl-pages"]/form/span/text()').extract()
            for url in user_url:
                #调用parse_user_item解析文章内容
                #ua = random.choice(self.user_agent_list)#随机抽取User-Agent
                print ("user_url is " + url)
                request = scrapy.Request(url,callback=self.parse_user_item)
                yield request
                #self.save_user_id(url)
            
            if (len(is_end_page) == 0 or is_end_page[0] != "下页") and len(next_page_url) > 0:
                #调用自身进行迭代
                #print (next_page_url[0])
                request = scrapy.Request(urljoin(self.baseurl,next_page_url[0]),callback=self.parse_each_article)
                yield request


    def parse_user_item(self, response):

        print(response.url)
    
        sel = Selector(response)
        #l = ItemLoader(item=TianyaUserItem(), response=response)
        l = TianyaUserItem()

        userinfo_url = response.url
        today_timestamp = "2017.12.14"#sp.get_tody_timestamp()
        #article_id = hash(article_url)#sp.hashForUrl(article_url)
        
        #l.add_value('userinfo_url',userinfo_url)
        #l.add_value('crawl_time',today_timestamp)
        l['crawl_time'] = today_timestamp
        l['userinfo_url'] = userinfo_url

        return l
        #yield l.load_item()

    def save_user_id(self, user_url):

        print(user_url)

        l = ItemLoader(item=TianyaUserItem(), response=response)
        #l = TianyaUserItem()

        userinfo_url = response.url
        today_timestamp = "2017.12.14"#sp.get_tody_timestamp()
        #article_id = hash(article_url)#sp.hashForUrl(article_url)
        
        l.add_value('userinfo_url',userinfo_url)
        l.add_value('crawl_time',today_timestamp)
        #l['crawl_time'] = today_timestamp
        #l['userinfo_url'] = userinfo_url

        #return l
        yield l.load_item()
