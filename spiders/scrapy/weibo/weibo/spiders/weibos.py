# -*- coding: utf-8 -*-
from scrapy import Spider, FormRequest


class WeibosSpider(Spider):
    name = 'weibos'
    allowed_domains = ['weibo.cn']
    start_urls = 'http://weibo.cn/search/mblog'
    max_page = 0

    def start_requests(self):
        keyword = '000001'
        url = '{url}?keyword={keyword}'.format(url=self.start_urls, keyword=keyword)
        print(url)
        for page in range(self.max_page + 1):
            data = {
                'mp': str(self.max_page),
                'page': str(page)
            }
            yield FormRequest(url, callback=self.parse_index, formdata=data)

    def parse_index(self, response):
        print(response.text)
