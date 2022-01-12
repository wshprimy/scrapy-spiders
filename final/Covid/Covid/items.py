# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class CovidItem(scrapy.Item):
    time = scrapy.Field() # 时间
    country = scrapy.Field() # 国家/地区
    new_cases = scrapy.Field() # 新增确诊人数
    total_cases = scrapy.Field() # 累计确诊人数
    total_cases_per_million = scrapy.Field() # 国家每百万人口累计确诊人数
    vaccinated = scrapy.Field() # 累计疫苗接种人数
    vaccinated_rate = scrapy.Field() # 国家累计疫苗接种率
    vaccinated_fully_rate = scrapy.Field() # 国家累计疫苗全程接种率
    fatality_rate = scrapy.Field() # 病死率
    pass