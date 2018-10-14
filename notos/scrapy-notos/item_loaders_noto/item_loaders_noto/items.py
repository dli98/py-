# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
import scrapy
import logging


def parse_length(text, loader_context):
    unit = loader_context.get('unit', 'm')
    # ... length parsing code goes here ...
    parsed_length = 10
    return parsed_length


def add_title_jobbole(value):
    print('-------------title', value)
    return value + "---jobbole",


def get_text(value):
    print('-------------')
    logger = logging.getLogger(__name__)
    logger.warning('text')
    print('xxxxxxxxxxxx', value)
    return value


# 继承ItemLoader这个方法，并自定义自己的方法(属性)
class TextLoader(ItemLoader):
    # 设置为只选取, 这里只是重载这个属性第一个值
    default_output_processor = TakeFirst()
    pass


class ExtractItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(add_title_jobbole),
        # MapCompose()里的参数可以是任意函数，例子中add是外置函数，也可以是lambda匿名函数
    )
    url = scrapy.Field()
    front_image_url = scrapy.Field(
        input_processor=MapCompose(get_text)
    )
    front_image_url2 = scrapy.Field(
        input_processor=MapCompose(get_text)
    )
    emial = scrapy.Field()
    social = scrapy.Field()

# ---------------------way 2----------------------#
# class TextLoader(ItemLoader):
#     default_output_processor = TakeFirst()        # (least precedence)
#     title_in = MapCompose(get_text)          #  (most precedence)
#     pass
#
#
# class ExtractItem(scrapy.Item):
#     title = scrapy.Field()
#     url = scrapy.Field()
#     front_image_url = scrapy.Field()
#     front_image_url2 = scrapy.Field()
