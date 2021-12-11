# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    name = scrapy.Field()
    loc_0 = scrapy.Field()
    loc_1 = scrapy.Field()
    loc_2 = scrapy.Field()
    count = scrapy.Field()
    area = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    pass