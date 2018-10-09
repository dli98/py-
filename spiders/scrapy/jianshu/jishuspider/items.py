# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JishuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    publish_time = scrapy.Field()
    wordage = scrapy.Field()
    views_count = scrapy.Field()
    comments_count = scrapy.Field()
    likes_count = scrapy.Field()
    rewards_count = scrapy.Field()
    pass
