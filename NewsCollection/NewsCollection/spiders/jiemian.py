import time

import scrapy
from NewsCollection.items import JiemianItem
from NewsCollection.Structures.alchemy import engine
from NewsCollection.Structures.tables import Jiemian


class JiemianSpider(scrapy.Spider):
    name = 'jiemian'
    allowed_domains = ['www.jiemian.com']
    start_urls = ['https://www.jiemian.com/lists/4.html']
    custom_settings = {
        'DOWNLOAD_DELAY': 5,
        'LOG_LEVEL': 'ERROR',
        # 'COOKIES_ENABLED': True,
        # 'COOKIES_DEBUG': True,
        'ITEM_PIPELINES': {
            'NewsCollection.pipelines.JiemianPipeline': 300
        }
    }

    def start_requests(self):
        h = {
            'Host': self.allowed_domains[0]
        }
        yield scrapy.Request(self.start_urls[0], headers=h)

    def parse(self, response):
        div_list = response.xpath('//*[@id="lists"]/ul/li')
        id_list = set()
        check = engine('ods').query(Jiemian.news_id).order_by(Jiemian.news_id.desc()).limit(200)
        for ids in check:
            id_list.add(ids[0])
        for div in div_list:
            item = JiemianItem()
            if div.xpath('./div/@data-id').extract_first() is not None:
                if div.xpath('./div/@data-id').extract_first() not in id_list:
                    item['date_time'] = div.xpath('./div/@data-time').extract_first()
                    item['news_id'] = div.xpath('./div/@data-id').extract_first()
                    item['title'] = ''.join(div.xpath('./div/div[3]/p//text()').extract()).strip().replace(' ', '').replace('\n','').replace('\t', '').replace('\xa0','').replace('\r', '')
                    item['content_url'] = div.xpath('./div/div[3]/p/a/@href').extract_first()
                    print('~~~No~~~',item['title'], '没没没没爬过！！！！')
                    yield item
            # else:
                # print(''.join(div.xpath('./div[2]/p//text()').extract()).strip().replace(' ', '').replace('\n', '').replace('\t', ''), '爬过了！！！！！')
	         # pass 


