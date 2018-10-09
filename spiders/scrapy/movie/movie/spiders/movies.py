# -*- coding: utf-8 -*-
import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['phthon.com']
    start_urls = ['http://phthon.com/']

    def parse(self, response):
        movies = response.x
