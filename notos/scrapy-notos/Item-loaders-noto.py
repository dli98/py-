from scrapy.loader import ItemLoader
from myproject.items import Product


def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today')  # you can also use literal values
    return l.load_item()

# 在爬虫文件中：

# 先引入
# from ArticalSpider.items import JobboleArticalItem,ArticalItemLoader
#         #使用Itemloader来简化这个解析，装入Item这个过程，使得代码量减少
#         #先创建一个itemLoader()这样一个对象,不需解析list第一个等问题
#         #这里的ArticalItemLoader是继承了itemloader,并重写了部分功能，实现定制
#         item_loader = ArticalItemLoader(item=JobboleArticalItem(), response=response)
#         #使用ItemLoader这个对象的xpath解析器
#         item_loader.add_xpath("title",'/html//div[@class="entry-header"]/h1/text()')
#         #使用get_value()直接从response中选取内容
#         item_loader.add_value("url_object_id",get_md5(response.url))
#         item_loader.add_xpath("add_time", '/html//p[@class="entry-meta-hide-on-mobile"]/text()')
#         item_loader.add_value("url", response.url)
#         item_loader.add_value("front_image_url", [front_image_url])
#         item_loader.add_value("front_image_url2",front_image_url)
#         item_loader.add_xpath("tags",'/html//p[@class="entry-meta-hide-on-mobile"]/a/text()')
#         item_loader.add_xpath("comment_num",'//span[@class="btn-bluet-bigger href-style hide-on-480"]/text()')
#         item_loader.add_xpath("fav_num",'//span[contains(@class,"bookmark-btn")]/text()')
#         item_loader.add_xpath("like_num",'//span[contains(@class,"vote-post-up")]/h10/text()')
#         item_loader.add_xpath("content",'//div[@class="entry"]')
#         #装入Item
#         artical_item = item_loader.load_item()
#
#         yield artical_item
#


# 在Item.py中:
# #继承ItemLoader这个方法，并自定义自己的方法(属性)
# class ArticalItemLoader(ItemLoader):
#     #实现之前的extract_first()方法
#     #，设置为只选取这里只是重载这个属性第一个值
#     default_output_processor = TakeFirst()
#
# #以下将之前的各种清洗语句整合到函数中
# def add_title_jobbole(value):
#     return value+"---jobbole"
#
# def get_time(value):
#     #这个好像更改不了
#     try:
#         add_time = datetime.datetime.strptime(value,"%Y/%m/%d").data()
#     except Exception as e:
#         print(e)
#         add_time = datetime.datetime.now().date()
#     return add_time
#
# def get_tags(value):
#     tag_list = [x for x in value if not str(x).strip().endswith("评论") ]
#
#     return tag_list
# def get_comment_num(value):
#     re_comment = re.match(".*(\d+).*",value)
#     if re_comment:
#         comment_num = int(re_comment.group(1))
#     else:
#         comment_num = 0
#     return comment_num
# def get_fav_num(value):
#     re_fav_num = re.match(".*(\d+).*",value)
#     if re_fav_num:
#         fav_num =  int(re_fav_num.group(1))
#     else:
#         fav_num = 0
#     return fav_num
# #小技巧：在出IteaLoad时,将之前进入的类型按原先的返回，怎么进入怎么返回
# def get_value(value):
#     return value
# class JobboleArticalItem(scrapy.Item):
#     title = scrapy.Field(
#     #调用方法，为传进的数据字段进行清洗，调用外部的方法
#         #input_processor 方法是将进入的数据进行调用函数清洗
#         #MapCompose 调用函数名
#         input_processor = MapCompose(add_title_jobbole)
#     )
#     add_time = scrapy.Field(
#         input_processor = MapCompose(get_time),
#         #只获取传入Item的这个列表中的第一个值作为Item的值
#         #但是要是字段太多，都得写下面这个语句，岂不麻烦，所以可以继承ItemLoader这个类，完成自己类
#         #TakeFirsr()就是 extrct_first()
#         output_processor = TakeFirst()
#     )
#     url = scrapy.Field()
#     content = scrapy.Field()
#     #不同url长度不同，通过md5统一长度
#     url_object_id = scrapy.Field()
#
#     front_image_url = scrapy.Field(
#         #自定义的类之后，所有的Item都默认了list的第一个值，但传入下载图片的管道时会报错，因为下载图片的Item为list
#         #出去ItemLoader时处理数据的方法
#         output_processor = MapCompose(get_value)
#     )
#     front_image_url2 = scrapy.Field()
#     #url本地存放路径
#     front_image_path = scrapy.Field()
#
#     tags = scrapy.Field(
#         input_processor = MapCompose(get_tags),
#         #使用processor自带的Join拼接方法
#         output_processor = Join(",")
#     )
#     comment_num = scrapy.Field(
#         input_processor = MapCompose(get_comment_num)
#     )
#     fav_num = scrapy.Field(
#         input_processor = MapCompose(get_fav_num)
#     )
#     like_num = scrapy.Field(
#
#     )
