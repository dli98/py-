# -*- coding: utf-8 -*-
from scrapy import Spider, Request

from Tencent.items import TencentItem


class TencentSpider(Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = 'https://hr.tencent.com/position.php?&start={index}#a'

    def start_requests(self):
        start_url = self.url.format(index=0)
        yield Request(start_url, callback=self.parse)

    def parse(self, response):
        table_list = response.xpath('//*[@id="position"]/div[1]/table/tr')
        for tr in table_list[1:-1]:
            item = TencentItem()
            item['position_name'] = tr.xpath('./td/a/text()').extract_first()
            item['position_link'] = tr.xpath('./td/a/@href').extract_first()
            item['position_type'] = tr.xpath('./td[2]/text()').extract_first()
            item['position_number'] = tr.xpath('./td[3]/text()').extract_first()
            item['work_location'] = tr.xpath('./td[4]/text()').extract_first()
            item['publish_time'] = tr.xpath('./td[5]/text()').extract_first()
            yield item
        for i in range(2, 331):
            url = self.url.format(index=i*10)
            yield Request(url=url, callback=self.parse)
