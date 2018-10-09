# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']


    def parse(self, response):
        # temp = response.css('.a')
        # print(temp.css('::text').extract(), '***************')
        # print(response.css('a::attr(href)').extract(), '***************')
        # print('***************************************************')
        for href in response.css('a::attr(href)').extract():
        # for href in temp.css('::attr(href)').extract():
            # 找到class为a的所有结点。提取a标签属性为href的内容
            # .extract()为了提取真实的原文数据  返回的系统自带的List    没有这个是SelectorList
            # print(href)
            try:
                # re.findall(r'[s][hz]\d{6}', href)[0]
                stock = re.findall(r'[s][hz]\d{6}', href)[0]   #以列表形式返回能匹配的字符串
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                # print(url)
                yield scrapy.Request(url, callback=self.parse_stock)
                # Request类 由scrapy生产。由downloader执行
                # 表示一个HTTP请求。.method对应请求的方法
                # classback 回调函数 将此请求返回的response传递给下一个函数进行处理
            except:
                continue

    def parse_stock(self, response):
        info_dict = {}
        temp = response
        stock_info = response.css('.stock-bets')
        name = stock_info.css('.bets-name').extract()[0]
        key_list = stock_info.css('dt').extract()
        value_list = stock_info.css('dd').extract()
        for i in range(len(key_list)):
            key = re.findall(r'>.*</dt>', key_list[i])[0][1:-5]
            try:
                val = re.findall(r'\d+.?.*.</dd>', value_list[i])[0][0:-5]
            except:
                val = '--'
            info_dict[key] = val
        info_dict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + re.findall('\>.*\<', name)[0][1: -1]})
        yield info_dict
