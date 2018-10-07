from scrapy import Spider
from wikiSpider.items import WikispiderItem


class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page",
                  "https://en.wikipedia.org/wiki/Python_%28programming_language%29"]

    def parse(self, response):
        item = WikispiderItem()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is:" + title)
        item['title'] = title
        return item
