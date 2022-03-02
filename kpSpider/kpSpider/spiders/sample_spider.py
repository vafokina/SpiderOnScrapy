import scrapy

from datetime import datetime
from scrapy.spiders import Spider

class NewsSpider(Spider):
    name = 'sample'
    start_urls = ['https://zen.yandex.ru/media/diva/top14-luchshih-jenskih-duhov-camye-populiarnye-duhi-u-jenscin-6154e30548745b42e403546b']

    def parse (self, response):
        url = response.url
        title = response.xpath('/html/head/title/text()').get().strip()
        description = response.xpath("//meta[@name='description']/@content")[0].extract().strip()
        images = response.xpath('//img/@src').extract() 

        yield{
            'im_count':len(images),
            'url':url,
            'title':title,
            'description':description,
            'image_urls':images,
            'scraping_date':datetime.now()
        }
        