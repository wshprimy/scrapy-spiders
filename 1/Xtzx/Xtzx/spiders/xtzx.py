import time
import scrapy
from Xtzx.items import XtzxItem
from scrapy.http import HtmlResponse
from selenium import webdriver

class XtzxSpider(scrapy.Spider):
    name = 'xtzx'
    allowed_domains = ['www.xuetangx.com']
    start_urls = ['https://www.xuetangx.com/university/all/']
    page_limit = 36

    def parse(self, response):
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--headless')
        driver_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options = driver_options)

        driver.get(response.url)
        driver.implicitly_wait(5)
        for i in range(0, self.page_limit):
            response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
            schools = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div')
            for school in schools:
                item = XtzxItem()
                item['school_name'] = school.xpath('./div[1]/p[1]/text()').get()
                item['total_courses'] = school.xpath('./p/text()').get()
                if item['school_name'] and item['total_courses']:
                    yield item
            button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[3]/button[2]')
            button.click()
            time.sleep(2)