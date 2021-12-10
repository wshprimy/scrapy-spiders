# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class LianjiaPipeline:
    items = {}
    
    def process_item(self, item, spider):
        item_temp = ItemAdapter(item).asdict()
        district = item_temp['district']
        if district not in self.items:
            self.items[district] = []
        item_list = list(item_temp.values())[:-1]
        self.items[district].append(item_list)
        return item

    def close_spider(self, spider):
        headers = ['楼盘名称', '总价', '平米数', '单价']
        for district_name, items in self.items.items():
            with open(f'{district_name}.csv', 'w', newline='', encoding='GBK') as file:
                file_csv = csv.writer(file)
                file_csv.writerow(headers)
                file_csv.writerows(items)
                file.close()