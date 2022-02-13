import scrapy
import random
from scrapy.http.cookies import CookieJar
from NewsCollection.items import JingjiItem
from NewsCollection.Structures.alchemy import engine
from NewsCollection.Structures.tables import Jingji


class A21jingjiSpider(scrapy.Spider):
    name = '21jingji'
    # allowed_domains = ['http://www.21jingji.com/']
    start_urls = ['http://www.21jingji.com/']

    custom_settings = {
        'DOWNLOAD_DELAY': random.randint(2, 15),
        # 'LOG_LEVEL': 'ERROR',
        'COOKIES_ENABLED': True,
        'COOKIES_DEBUG': True,
        'ITEM_PIPELINES': {
            'NewsCollection.pipelines.JingjiPipeline': 300
        }
    }

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        next_url = 'http://api.21jingji.com/timestream/getListweb?page=1'
        next_h = {
            'Host': 'api.21jingji.com',
            'Referer': 'http://www.21jingji.com/'
        }
        yield scrapy.Request(next_url, headers=next_h, cookies=cookie_jar.processed, callback=self.json_parse)

    def json_parse(self, response):
        id_list = set()
        check = engine('ods').query(Jingji.id).order_by(Jingji.id.desc()).limit(100)
        for ids in check:
            id_list.add(ids[0])
        for i in response.json()['list']:
            if i['id'] not in id_list:
                print('~~~No~~~',i['title'], '没没没没没没爬过！！！！！')
                item = JingjiItem()
                item['id'] = i['id']
                item['title'] = i['title']
                item['content'] = ''.join(i['content']).strip().replace('<br />\n','')
                item['inputtime'] = i['inputtime']
                item['tag'] = i['tag']
                item['source'] = str(i['source'])
                item['author'] = i['author']
                item['url'] = i['url']
                yield item
            else:
                # print(i['title'], '爬过了！！！！')
                pass
