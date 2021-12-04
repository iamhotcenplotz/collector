import time

import scrapy
import json
from NewsCollection.items import EastmoneyItem
from NewsCollection.Structures.alchemy import engine
from NewsCollection.Structures.tables import Eastmoney


class EastmoneySpider(scrapy.Spider):
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'LOG_LEVEL': 'ERROR',
        'ITEM_PIPELINES': {
            'NewsCollection.pipelines.EastmoneyPipeline': 300
        }
    }

    name = 'eastmoney'
    start_urls = ['https://newsapi.eastmoney.com/kuaixun/v1/getlist_102_ajaxResult_50_1_.html']

    def start_requests(self):
        print('*' * 30, 'start request', '*' * 30)
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def parse(self, response):
        data = response.text.removeprefix('var ajaxResult=')
        data = json.loads(data)['LivesList']
        id_list = set()
        check = engine('ods').query(Eastmoney.newsid).order_by(Eastmoney.newsid.desc()).limit(500)
        for ids in check:
            id_list.add(ids[0])
        cnt = 0
        for i in data:
            if i['newsid'] not in id_list:
                item = EastmoneyItem()
                item['newsid'] = i['newsid']
                item['url_unique'] = i['url_unique']
                item['title'] = i['title']
                item['digest'] = ''.join(i['digest']).replace(' ', '').replace("\u3000", '').replace("\n", '').replace(
                    "\r", '')
                if len(i['topic']) == 0:
                    item['topic'] = str(None)
                else:
                    item['topic'] = i['topic']
                item['showtime'] = i['showtime']
                item['commentnum'] = i['commentnum']
                item['newstype'] = i['newstype']
                if len(i['editor_name']) == 0:
                    item['editor_name'] = str(None)
                else:
                    item['editor_name'] = i['editor_name']
                print(i['title'], '没没没没没爬过！！！！！')
                yield scrapy.Request(i['url_unique'], headers={'Referer': 'https://finance.eastmoney.com/'},
                                     callback=self.content_parse, meta={'item': item})
            else:
                cnt += 1
                # print(i['title'], '爬过了！！！')

    def content_parse(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="ContentBody"]//p//text()').extract()
        content = ''.join(content).replace(' ', '').replace("\u3000", '').replace("\n", '').replace("\r", '')
        item['content'] = content
        yield item
