# -*- coding:utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
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


class tianyaUserArticalDetail(CrawlSpider):

    # 爬虫名称，非常关键，唯一标示
    name = "articleDetail"

    # 域名限定
    allowed_domains = ["bbs.tianya.cn", "www.tianya.cn"]

    # 爬虫的爬取得起始url
    start_urls = [
        # 天涯论坛热帖榜  可以写多个用，分隔
    ]

    def __init__(self):
        input = open("/Users/conght/WORK/crawls/TianYa/datasets-v2/uuid-articlelist")
        for line in input:
            articalIdArray = line.replace("\n","").replace("\r","").split("\t")
            if len(articalIdArray) < 3:
                continue
            articalIdArray = articalIdArray[1:]
            articalIdArray = articalIdArray[:-1]
            for id in articalIdArray:
                self.start_urls.append("http://bbs.tianya.cn/post-funinfo-"+id+"-1.shtml")

    baseurl = 'http://bbs.tianya.cn'

    def parse(self, response):

        content = ''
        sel = Selector(response)

        article_url = str(response.url)
        today_timestamp = "2017.12.14"  # sp.get_tody_timestamp()
        article_content = sel.xpath(
            '//div[@class="atl-main"]//div/div[@class="atl-content"]/div[2]/div[1]/text()').extract()
        article_author = sel.xpath('//div[@id="post_head"]/div[2]/div[@class="atl-info"]/span[1]/a/@href').extract()
        #article_time = sel.xpath('//div[@id="post_head"]/div[2]/div[@class="atl-info"]/span[1]/a/@href').extract()

        qa_content = sel.xpath(
            '//div[@class="wd-question"]/div[5]/div/text()').extract()

        qa_author = sel.xpath(
            '//div[@class="wd-question"]/div[3]/span[2]/a/@href').extract()

        if len(article_content) > 0:
            print(article_author[0] + "\t" + str(len(article_content[0].strip())))
            sys.stdout.flush()
        if len(qa_content) > 0:
            print(qa_author[0] + "\t" + str(len(qa_content[0].strip())))
            sys.stdout.flush()
