# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XtzxItem(scrapy.Item):
    school_name = scrapy.Field()
    total_courses = scrapy.Field()
    pass