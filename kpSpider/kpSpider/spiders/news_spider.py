import scrapy

from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NewsSpider(CrawlSpider):
    name = 'kp_all_news'
    allowed_domains = ['perm.kp.ru']
    start_urls = ['https://www.perm.kp.ru/']

    rules = (
        Rule(LinkExtractor(allow=r".*?/daily/[0-9.]+/\d+"), callback='parse_items', follow=True),
        Rule(LinkExtractor(allow=()), follow=True),
    )

    def parse_items (self, response):
        url = response.url
        title = response.xpath('/html/head/title/text()').get().strip()
        description = response.xpath("//meta[@name='description']/@content")[0].extract().strip()
        images = response.xpath('//div[@data-gtm-el="content-body"]/*//img/@src').extract() # аналогичное response.css('div[data-gtm-el="content-body"]').css('img::attr(src)').extract()  
        # publish_date = 

        yield{
            'url':url,
            'title':title,
            'description':description,
            'image_urls':images,
            'scraping_date':datetime.now()
        }
        