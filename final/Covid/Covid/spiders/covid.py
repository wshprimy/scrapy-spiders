import scrapy
from Covid.items import CovidItem

class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['ourworldindata.org']
    start_urls = [
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=Confirmed+cases&Interval=New+per+day&Relative+to+Population=false&time=2021-12-05',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=Confirmed+cases&Interval=Cumulative&Relative+to+Population=false&time=2021-12-05',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=Confirmed+cases&Interval=Cumulative&Relative+to+Population=true&time=2021-12-05',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=false&time=2021-12-05',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=true&time=2021-12-05',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=People+fully+vaccinated&Interval=Cumulative&Relative+to+Population=true&time=2021-12-05',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&Metric=Case+fatality+rate&Interval=Cumulative&time=2021-12-05'
    ]
    types = ['time', 'country', 'new_cases', 'total_cases', 'total_cases_per_million', 'vaccinated', 'vaccinated_rate', 'vaccinated_fully_rate', 'fatality_rate']
    start_date = '2021-12-05'
    end_date = '2021-12-20'

    def start_requests(self):
        for i in range(0, 7):
            yield scrapy.Request(self.start_urls[i], callback=self.parse, cb_kwargs={'date': self.start_date, 'type': self.types[i + 2]})
    
    def parse(self, response, *args, **kwargs):
        item = CovidItem()
        for keyword in self.types:
            item[keyword] = ''
        item['time'] = kwargs['date']
        for country in response.xpath('/html/body/main/div/div[3]/div/div[1]/div/table/tbody/tr'):
            item['country'] = country.xpath('./td[1]/text()').get()
            item[kwargs['type']] = country.xpath('./td[last()]/text()').get()
            yield item
            item['country'] = ''
            item[kwargs['type']] = ''
        
        now_date = kwargs['date']
        if now_date == self.end_date:
            pass
        else:
            next_date = now_date[:-2] + f'{int(now_date[-2:]) + 1:02d}'
            yield response.follow(response.url.replace(now_date, next_date), callback=self.parse, cb_kwargs={'date': next_date, 'type': kwargs['type']})