# -*- coding: utf-8 -*-
import scrapy
import os


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ['python123,io']
    start_urls = ["http://python123.io/ws/demo.html"]

    def parse(self, response):
        """
        用于处理响应，解析内容形成字典，发现新的URL爬取请求
        :param response:
        """
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file &s.' % fname)
