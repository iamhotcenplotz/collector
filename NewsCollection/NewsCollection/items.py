# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Eastmoney Items defined below
class EastmoneyItem(scrapy.Item):
    newsid = scrapy.Field()
    url_unique = scrapy.Field()
    title = scrapy.Field()
    digest = scrapy.Field()
    topic = scrapy.Field()
    showtime = scrapy.Field()
    commentnum = scrapy.Field()
    newstype = scrapy.Field()
    content = scrapy.Field()
    editor_name = scrapy.Field()


class SnowballItem(scrapy.Item):
    snowball_id = scrapy.Field()
    text = scrapy.Field()
    mark = scrapy.Field()
    target = scrapy.Field()
    created_at = scrapy.Field()
    view_count = scrapy.Field()
    status_id = scrapy.Field()
    reply_count = scrapy.Field()
    share_count = scrapy.Field()

class JiemianItem(scrapy.Item):
    date_time = scrapy.Field()
    news_id = scrapy.Field()
    title = scrapy.Field()
    content_url = scrapy.Field()
    
    
class EgsItem(scrapy.Item):
    egs_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pageTime = scrapy.Field()
    content_url = scrapy.Field()


class JingjiItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    inputtime = scrapy.Field()
    url = scrapy.Field()
    tag = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
