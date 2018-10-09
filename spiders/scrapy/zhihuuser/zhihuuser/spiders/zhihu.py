# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import json
from zhihuuser.items import UserItem
# from scrapy_redis

class ZhihuSpider(Spider):
    name = 'zhihu'
    start_urls = ['http://www.zhihui.com/']

    start_user = 'excited-vczh'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

    def start_requests(self):
        #  他关注的人的链接
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20), callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20), callback=self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item
        # 找到每个用户自己的关注列表
        yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0), callback=self.parse_follows)
        yield Request(self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0), callback=self.parse_followers)

    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') ==False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, callback=self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') ==False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, callback=self.parse_followers)

