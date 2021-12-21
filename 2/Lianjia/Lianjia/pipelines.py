# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class LianjiaPipeline:
    items = []

    def process_item(self, item, spider):
        item_list = list(ItemAdapter(item).asdict().values())
        self.items.append(item_list)
        return item
    
    def close_spider(self, spider):
        headers = ['名称', '地理位置1', '地理位置2', '地理位置3', '房型', '面积', '均价', '总价']
        # ['name', 'location_area', 'location_town', 'location_exact', 'type', 'area', 'price', 'price_type']
        with open('loupan.csv', 'w', newline='', encoding='utf-8-sig') as file:
            file_csv = csv.writer(file)
            file_csv.writerow(headers)
            file_csv.writerows(self.items)
            file.close()