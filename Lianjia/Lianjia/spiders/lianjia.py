import scrapy
from Lianjia.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']
    district_limit = 4
    page_limit = 5

    def parse(self, response):
        self.logger.info(f'Recieved url: {response.url}')
        for district in range(1, self.district_limit + 1):
            district_name = response.xpath(f'/html/body/div[3]/div/div[1]/dl[2]/dd/div[1]/div/a[{district}]/@href').get() 
            district_name = district_name.split('/')[-2]
            next_page = response.url + district_name + '/'
            if next_page is not None:
                self.logger.info(f'Next url: {next_page}')
                yield response.follow(next_page, callback=self.parse_district, cb_kwargs={'district': district_name, 'page_id': 1})
    
    def parse_district(self, response, **kwargs):
        self.logger.info(f'Recieved url: {response.url}')
        district_name = kwargs['district']
        houses = response.xpath('/html/body/div[4]/div[1]/ul/li')
        for house in houses:
            item = LianjiaItem()
            item['name'] = house.xpath('./div[1]/div[2]/div/a[1]/text()').get().strip()
            item['total_price'] = house.xpath('./div[1]/div[6]/div[1]/span/text()').get() + \
                house.xpath('./div[1]/div[6]/div[1]/i[last()]/text()').get()
            item['area'] = house.xpath('./div[1]/div[3]/div/text()').get().split('|')[1].strip()
            item['unit_price'] = house.xpath('./div[1]/div[6]/div[2]/span/text()').get()
            item['district'] = district_name
            if item['name'] and item['total_price'] and item['area'] and item['unit_price']:
                yield item
        
        page_now = kwargs['page_id']
        self.logger.info(f'page_now = {page_now}')
        if page_now >= self.page_limit:
            pass
        else:
            next_page = response.url
            if page_now != 1:
                next_page = next_page[:-4]
            next_page = next_page + 'pg' + str(page_now + 1) + '/'
            self.logger.info(f'Next url: {next_page}')
            # next_page = response.xpath('/html/body/div[4]/div[1]/div[7]/div[2]/div/a[last()]/@href').get()
            yield response.follow(next_page, callback=self.parse_district, cb_kwargs={'district': district_name, 'page_id': page_now + 1})