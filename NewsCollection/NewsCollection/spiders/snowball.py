import random
import time
from datetime import datetime
import scrapy
from scrapy.http.cookies import CookieJar
from NewsCollection.items import SnowballItem
from NewsCollection.Structures.alchemy import engine
from NewsCollection.Structures.tables import Snowball


class SnowballSpider(scrapy.Spider):
    name = 'snowball'
    # allowed_domains = ['www.xueqiu.com']
    start_urls = ['https://xueqiu.com/?category=livenews']
    custom_settings = {
        'DOWNLOAD_DELAY': random.randint(2, 15),
        'LOG_LEVEL': 'ERROR',
        'COOKIES_ENABLED': True,
        'COOKIES_DEBUG': True,
        'ITEM_PIPELINES': {
            'NewsCollection.pipelines.SnowballPipeline': 300
        }
    }

    def start_requests(self):
        start_headers = {
            'Referer': 'https://xueqiu.com'
        }
        print("Download dealy is: ", self.custom_settings['DOWNLOAD_DELAY'])
        yield scrapy.Request(self.start_urls[0], headers=start_headers)

    def parse(self, response):
        next_url = 'https://xueqiu.com/statuses/livenews/list.json'

        next_headers = {
            'Referer': 'https://xueqiu.com/?category=livenews'
        }

        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        yield scrapy.Request(next_url, headers=next_headers, cookies=cookie_jar.processed, callback=self.json_parse)

    def json_parse(self, response):
        id_list = set()
        check = engine('ods').query(Snowball.snowball_id).order_by(Snowball.snowball_id.desc()).limit(10)
        for ids in check:
            id_list.add(ids[0])
        for i in response.json()['items']:
            if str('snowball' + str(i['id'])) not in id_list:
                item = SnowballItem()
                item['snowball_id'] = str('snowball' + str(i['id']))
                item['text'] = ''.join(i['text']).replace(' ','').replace('\n','')
                item['mark'] = i['mark']
                item['target'] = i['target']
                item['created_at'] = str(datetime.fromtimestamp(float(i['created_at']) / 1000))
                item['view_count'] = i['view_count']
                item['status_id'] = i['status_id']
                item['reply_count'] = i['reply_count']
                item['share_count'] = i['share_count']
                print('~~~NO~~~',i['text'], '没没没没没爬过！！！！！')
                yield item
            # else:
                # print(i['text'], '爬过了！！！！')
		#  pass 
