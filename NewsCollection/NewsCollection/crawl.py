"""
Running Multiple Spiders in Parallel
"""
# Methods 1 below:
# notice that it is not running in parallel.
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
crawl_list = ['eastmoney',
              'snowball',
              'jiemian'
              ]
for i in crawl_list:
    process.crawl(i)
process.start()

