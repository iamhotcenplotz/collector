import scrapy
import random
from datetime import datetime
from scrapy.http.cookies import CookieJar
from NewsCollection.items import EgsItem
from NewsCollection.Structures.alchemy import engine
from NewsCollection.Structures.tables import Egs


class EgsSpider(scrapy.Spider):
    name = 'egs'
    # allowed_domains = ['egs.stcn.com']
    start_urls = ['http://egs.stcn.com/']

    custom_settings = {
        'DOWNLOAD_DELAY': random.randint(2, 15),
        'LOG_LEVEL': 'ERROR',
        'COOKIES_ENABLED': True,
        'COOKIES_DEBUG': True,
        'ITEM_PIPELINES': {
            'NewsCollection.pipelines.EgsPipeline': 300
        }
    }

    def start_requests(self):
        h = {
            'Host': 'egs.stcn.com'
        }
        yield scrapy.Request(self.start_urls[0], headers=h)

    def parse(self, response):
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        next_url = 'http://egs.stcn.com/news/flash-list.html?sidebar=1&page=1&pageTime=0&per-page=10'
        next_h = {
            'Referer': 'http://egs.stcn.com/'
        }
        yield scrapy.Request(next_url, headers=next_h, cookies=cookie_jar.processed, callback=self.json_parse)

    def json_parse(self, response):
        id_list = set()
        check = engine('ods').query(Egs.egs_id).order_by(Egs.egs_id.desc()).limit(100)
        for ids in check:
            id_list.add(ids[0])
        d = response.json()['data']
        for i in d:
            if str(i['id']) not in id_list:
                print('~~~NO~~~',i['title'], '没没没没爬过！！！！！')
                item = EgsItem()
                item['egs_id'] = str(i['id'])
                item['title'] = i['title']
                item['content'] = i['content']
                item['content_url'] = 'https://egs.stcn.com/' + i['url']
                item['pageTime'] = str(datetime.fromtimestamp(float(i['pageTime'])))
                yield item
            else:
                print(i['title'], '爬过了！！！！！')
