# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class XtzxPipeline:
    def open_spider(self, spider):
        self.result = []
    
    def process_item(self, item, spider):
        item_temp = ItemAdapter(item).asdict()
        print(type(item_temp))
        self.result.append(item_temp)
        return item

    def close_spider(self, spider):
        with open('xuetangzaixian.json', 'w', encoding='utf-8') as file:
            json_str = json.dumps(self.result, ensure_ascii=False, indent=4)
            file.write(json_str)
            file.close()