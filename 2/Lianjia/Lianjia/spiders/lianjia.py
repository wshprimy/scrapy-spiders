import scrapy
from Lianjia.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.fang.lianjia.com']
    start_urls = ['https://bj.fang.lianjia.com/loupan/']

    def parse(self, response):
        houses = response.xpath('/html/body/div[3]/ul[2]/li')
        for house in houses:
            try:
                item = LianjiaItem()
                item['name'] = house.xpath('./div/div[1]/a/text()').get().strip()
                loc = house.xpath('./div/div[2]')
                item['loc_0'] = loc.xpath('./span[1]/text()').get().strip()
                item['loc_1'] = loc.xpath('./span[2]/text()').get().strip()
                item['loc_2'] = loc.xpath('./a/text()').get().strip()
                item['count'] = house.xpath('./div/a/span[1]/text()').get().strip()
                area = house.xpath('./div/div[3]/span/text()').get()
                area = area.split(' ')[1].split('-')[0].rstrip('㎡')
                item['area'] = int(area)
                flag = house.xpath('./div/div[6]/div[1]/span[2]/text()').get().strip()
                if flag == '元/㎡(均价)':
                    unit_price = house.xpath('./div/div[6]/div[1]/span[1]/text()').get()
                    unit_price = unit_price.split('-')[0].strip()
                    item['unit_price'] = int(unit_price)
                    item['total_price'] = item['unit_price'] * item['area'] / 10000
                else:
                    total_price = house.xpath('./div/div[6]/div[1]/span[1]/text()').get()
                    total_price = total_price.split('-')[0].strip()
                    item['unit_price'] = 0
                    item['total_price'] = float(total_price)
                    item['unit_price'] = round(item['total_price'] / item['area'] * 10000)
                item['total_price'] = '{:.4f}'.format(item['total_price'])
                yield item
            except:
                self.logger.info('Recieved an item containing null values')
        
        self.logger.info(f'Recieved next_page: {response.url}')
        if response.url == 'http://none/':
            # 由于HtmlResponse要求url必须为一个合法的url，故我们定义'http://none/'为结束的标志
            pass
        else:
            yield scrapy.Request(response.url)