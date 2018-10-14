# -*- coding: utf-8 -*-
import scrapy
from item_loaders_noto.items import TextLoader, ExtractItem
import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.WARNING
)


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.jianshu.com/trending/weekly?']
    start_urls = ['https://www.jianshu.com/trending/weekly?&page=1']

    def __init__(self, *args, **kwargs):
        # logger = logging.getLogger('scrapy')
        # logger.setLevel(logging.WARNING)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        # print("Existing settings: %s" % self.settings.attributes.keys())
        # 这里的ArticalItemLoader是继承了itemloader,并重写了部分功能，实现定制
        item_loader = TextLoader(item=ExtractItem(), response=response)
        item_loader.add_value("front_image_url2", '123')
        item_loader.add_value("front_image_url2", 1)
        item_loader.add_value("title", ['456', '789'])
        item_loader.add_xpath("title", '//*[@id="note-34872153"]//text()')
        item_loader.add_value("url", response.url)
        item_loader.add_value("front_image_url", ['123', '456'])

        # print(response.xpath('//*[@id="note-34872153"]//text()').extract())
        self.logger.info(item_loader.get_input_processor('title'))
        print('2t', item_loader.get_output_value('title'))
        print(item_loader.get_output_processor('title'))
        print(item_loader.get_collected_values('title'))



        # nested loaders
        # load stuff not in the footer
        '''
             < footer >
       < a

       class ="social" href="https://facebook.com/whatever" > Like Us < / a >

       < a

       class ="social" href="https://twitter.com/whatever" > Follow Us < / a >

       < a

       class ="email" href="mailto:whatever@example.com" > Email Us < / a >

   < / footer >
   
       load stuff not in the footer
       footer_loader = item_loader.nested_xpath('//footer')
       footer_loader.add_xpath('social', 'a[@class = "social"]/@href')
       footer_loader.add_xpath('email', 'a[@class = "email"]/@href')
       # no need to call footer_loader.load_item()
       item_loader.load_item()
        '''
        # 装入Item
        artical_item = item_loader.load_item()
        yield artical_item

# It’s worth noticing that processors are just callable objects, which are called with the data to be parsed,
#  and return a parsed value. So you can use any function as input or output processor. The only requirement
#  is that they must accept one (and only one) positional argument, which will be an iterator.

# Both input and output processors must receive an iterator as their first argument. The output of those functions
#  can be anything. The result of input processors will be appended to an internal list (in the Loader) containing
# the collected values (for that field). The result of the output processors is the value that will be finally
# assigned to the item.
