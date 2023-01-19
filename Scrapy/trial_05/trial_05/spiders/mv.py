import scrapy
from trial_05.items import Trial05Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//a[@class="ulink"]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            print(name)
            src = 'https://www.ygdy8.net' + href
            yield scrapy.Request(url=src, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        src = response.xpath('//div[@class="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        movie = Trial05Item(name=name, src=src)
        yield movie
