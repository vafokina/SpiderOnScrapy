from turtle import title
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NewsSpider(CrawlSpider):
    name = 'kp_all_news'
    start_urls = ['https://www.perm.kp.ru/']

    rules = (
        Rule(LinkExtractor(allow='daily'), callback='parse_items', follow=True),
    )

    def parse_items (self, response):
        url = response.url
        title = response.xpath('/html/head/title/text()').get().strip()
        description = response.xpath("//meta[@name='description']/@content")[0].extract().strip()
        images = response.xpath('//div[@data-gtm-el="content-body"]/*//img/@src').extract()

        yield{
            'url':url,
            'title':title,
            'description':description,
            'image_urls':images
        }
        