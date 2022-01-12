# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class CovidPipeline:
    types = ['time', 'country', 'new_cases', 'total_cases', 'total_cases_per_million', 'vaccinated', 'vaccinated_rate', 'vaccinated_fully_rate', 'fatality_rate']

    def open_spider(self, spider):
        self.df = pd.DataFrame(columns=self.types) # 创建df表头
    
    def process_item(self, item, spider):
        item_dict = ItemAdapter(item).asdict()
        # 判断是否不存在关键字time和country相同的行
        if (self.df[(self.df['time'] == item_dict['time']) & (self.df['country'] == item_dict['country'])].empty):
            # df.empty成立，不存在，于是插入新的行
            self.df = self.df.append(item_dict, ignore_index=True)
        else:
            # df.empty不成立，存在，于是将对应行的对应格子插入非空数据
            index = self.df[(self.df['time'] == item_dict['time']) & (self.df['country'] == item_dict['country'])].index[0]
            for key, value in item_dict.items():
                if value != '':
                    self.df.at[index, key] = value
        return item

    def close_spider(self, spider):
        self.df.sort_values(by=['time', 'country'], inplace=True) # 按照'time', 'country'为关键字排序
        self.df.to_csv('covid.csv', index=False, encoding='utf-8-sig') # 将df输出到csv中