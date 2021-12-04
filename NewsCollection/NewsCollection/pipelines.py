# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time

from itemadapter import ItemAdapter
from NewsCollection.Structures.alchemy import engine
from NewsCollection.Structures.tables import Eastmoney
from NewsCollection.Structures.tables import Snowball
from NewsCollection.Structures.tables import Jiemian
from NewsCollection.Structures.tables import Egs

class EastmoneyPipeline:
    connection = None

    def open_spider(self, spider):
        print('*' * 30, 'Eastmoney Database Connected', '*' * 30)
        self.connection = engine('ods')

    def process_item(self, item, spider):
        # print('*' * 30, 'Eastmoney Database Processing', '*' * 30)
        print(item['title'])
        self.connection.add(Eastmoney(**item))
        return item

    def close_spider(self, spider):
        # print('*' * 30, 'Eastmoney Data Saved', '*' * 30)
        self.connection.commit()
        print('*' * 30, 'Eastmoney Database Closed', '*' * 30)
        self.connection.close()


class SnowballPipeline:
    connection = None
    def open_spider(self, spider):
        print('*' * 30, 'Snowball Database Connected', '*' * 30)
        self.connection = engine('ods')

    def process_item(self, item, spider):
        time.sleep(1)
        # print('*' * 30, 'Snowball Database Processing', '*' * 30)
        print(item['text'])
        self.connection.add(Snowball(**item))
        # print('*' * 30, 'Snowball Database Complete Processing', '*' * 30)
        return item

    def close_spider(self, spider):
        # print('*' * 30, 'Snowball Data Saved', '*' * 30)
        self.connection.commit()
        print('*' * 30, 'Snowball Database Closed', '*' * 30)
        self.connection.close()


class JiemianPipeline:
    connection = None
    def open_spider(self, spider):
        print('*' * 30, 'Jiemian Database Connected', '*' * 30)
        self.connection = engine('ods')

    def process_item(self, item, spider):
        time.sleep(1)
        # print('*' * 30, 'Jiemian Database Processing', '*' * 30)
        # print(item['title'])
        self.connection.add(Jiemian(**item))
        # print('*' * 30, 'Jiemian Database Complete Processing', '*' * 30)
        return item

    def close_spider(self, spider):
        # print('*' * 30, 'Jiemian Data Saved', '*' * 30)
        self.connection.commit()
        print('*' * 30, 'Jiemian Database Closed', '*' * 30)
        self.connection.close()
        
        
class EgsPipeline:
    connection = None
    def open_spider(self, spider):
        print('*' * 30, 'Egs Database Connected', '*' * 30)
        self.connection = engine('ods')

    def process_item(self, item, spider):
        # time.sleep(1)
        # print('*' * 30, 'Jiemian Database Processing', '*' * 30)
        # print(item['title'])
        self.connection.add(Egs(**item))
        # print('*' * 30, 'Jiemian Database Complete Processing', '*' * 30)
        return item

    def close_spider(self, spider):
        # print('*' * 30, 'Jiemian Data Saved', '*' * 30)
        self.connection.commit()
        print('*' * 30, 'Egs Database Closed', '*' * 30)
        self.connection.close()
