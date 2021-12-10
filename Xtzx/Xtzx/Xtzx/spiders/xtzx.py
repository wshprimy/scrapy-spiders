import scrapy


class XtzxSpider(scrapy.Spider):
    name = 'xtzx'
    allowed_domains = ['www.xuetangx.com']
    start_urls = ['https://www.xuetangx.com/university/all/']

    def parse(self, response):
        pass
