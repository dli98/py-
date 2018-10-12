# -------------- Creating a project------------#
# scrapy startproject myproject [project_dir]
# cd project_dir

# scrapy genspider mydomain mydomain.com


# ---------run our spider
# --go to the project’s top level directory and run
# scrapy crawl name


# -------------extracting data-----------------#
# scrapy shell 'http://quotes.toscrapy.com/page/1/'
# response.css('title::text').extract_first()
# response.css('title::text').extract_first(default='Not Found')
# response.css('title::text').re(r'Quotes.*')
# response.css('title::text').re_first(r'Quotes.*')
# response.xpath('//a[contains(@href, "image")]/@href').extract()
# response.css('a[href*=image]::attr(href)').extract()

# Here’s another example, to find the “id” attribute of a <div> tag containing five <a> children
# response.xpath('//div[count(a)=$cnt]/@id', cnt=5).extract_first()

# 例如在XPath的 starts-with() 或 contains() 无法满足需求时， test() 函数可以非常有用。
# sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()


# sel.xpath('//a//text()').extract() # take a peek at the node-set


# ----------Storing the scraped data-----------#
# scrapy crawl quotes -o quotes.json
# scrapy crawl quotes -o quotes.jl


# ------A shortcut for creating Requests-------#
# resoponse.follow(href, callback=self.parse)
# supports relative URLs directly - no need to call urljoin.


# scrapy -h
# scrapy <command> -h
# scrapy view <url>
# scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'


# When writing crawl spider rules, avoid using parse as callback, since the CrawlSpider uses the
# parse method itself to implement its logic. So if you override the parse method, the crawl spider
# will no longer work.
