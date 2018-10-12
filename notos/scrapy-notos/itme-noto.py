# -----------Declaring Items----------#
import scrapy


class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)


# -----------Creationg items----------#
product = Product(name='Ds', price=1000)


# -----------Extending Items------------#
class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()


class SpecificProduct(Product):
    name = scrapy.Field(Product.fields['name'], serializer=my_serializer)


