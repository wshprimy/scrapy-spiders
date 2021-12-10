import scrapy
from Xtzx.items import XtzxItem

class XtzxSpider(scrapy.Spider):
    name = 'xtzx'
    allowed_domains = ['www.xuetangx.com']
    start_urls = ['https://www.xuetangx.com/university/all/']

    def parse(self, response):
        test = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/p[1]/text()').get()
        print('1111111!!!!!', test)
        # /html/body/div[1]/div/div[2]/div[1]/div[2]
        schools = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div')
        # /html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/p
        # /html/body/div[1]/div/div[2]/div[1]/div[2]/div[4]/p
        # /html/body/div[1]/div/div[2]/div[1]/div[2]/div[16]/p
        for school in schools:
            item = XtzxItem()

            item['name'] = school.xpath('./div[1]/p[1]/text()').get()
            item['count'] = school.xpath('./p/text()').get()
            self.logger.info('name = %s, count = %s', item['name'], item['count'])
            if item['name'] and item['count']:
                yield item
        
        if response.url != None:
            yield scrapy.Request(response.url, callback=self.parse)