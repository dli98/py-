# -*- coding: utf-8 -*-
import scrapy
from jishuspider.items import JishuItem
import re
import json


class ZhihuSpider(scrapy.Spider):
    name = 'jishu'
    def start_requests(self):

        self.url = 'https://www.jianshu.com/trending/weekly?&page=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        yield scrapy.Request(self.url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        lis = response.css('#list-container > ul li')
        for li in lis:
            href = li.css('.title::attr(href)').extract_first()
            url = response.urljoin(href)
            meta = {'Referer' : url}
            yield scrapy.Request(url, meta=meta, headers=self.headers, callback=self.parse_page)

    def parse_page(self, response):
        page_data =re.search(r'page-data">(.*?)<',response.text,re.S).group(1)
        note = json.loads(page_data)['note']
        id = note['id']
        meta = {
            'author': note['author'],  #作者信息
            'title': response.css('body > div.note > div.post > div.article >.title::text').extract_first(), # 标题
            'wordage': note['public_wordage'] , # 总字数
            'views_count': note['views_count'],  # 阅读数
            'comments_count': note['comments_count'],  # 评论数
            'likes_count': note['likes_count'] , # 喜欢人数
            'rewards_count': note['total_rewards_count']  # 赞赏人数
        }
        comment_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': response.meta['Referer'],
            'Accept': 'application/json',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive'
        }
        comments_url = 'https://www.jianshu.com/notes/%s/comments?comment_id=&author_only=false&since_id=0&max_id=1586510606000&order_by=desc&page=1' % str(id)
        yield scrapy.Request(url=comments_url, headers=comment_headers, meta=meta, callback=self.parse_comments)

    def parse_comments(self, response):
        item = JishuItem()
        page = json.loads(response.text)
        comments = page['comments']
        comment_info = {}   # 存放评论者的信息和评论的内容
        for comment in comments:
            user = comment['user']
            comment_info['nick_name'] = user['nickname']   # 评论者的姓名
            comment_info['compiled_comment'] = comment['compiled_content']  # 评论的内容
            # for children in comment['children']:   # 跟评论内容
            #     nick_name = user['nickname']  # 跟评论者的姓名
            #     compiled_comment = comment['compiled_content']  # 跟评论的内容









