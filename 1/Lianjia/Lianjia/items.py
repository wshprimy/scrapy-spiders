# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    name = scrapy.Field()
    total_price = scrapy.Field()
    area = scrapy.Field()
    unit_price = scrapy.Field()
    district = scrapy.Field()
    pass