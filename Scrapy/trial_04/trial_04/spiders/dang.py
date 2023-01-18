import scrapy
from trial_04.items import Trial04Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    base_url = 'http://category.dangdang.com/pg'
    end = '-cp01.01.02.00.00.00.html'
    page = 1

    def parse(self, response):
        # src_list = response.xpath('//ul[@id="component_59"]/li/img/@src')
        # alt_list = response.xpath('//ul[@id="component_59"]/li/img/@alt')
        # price = response.xpath('//ul[@id="component_59"]/li/p[@class="price"]/span[@class="search_now_price"]/text()')
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            book = Trial04Item(src=src, name=name, price=price)
            yield book
        if self.page < 100:
            self.page += 1
            url = self.base_url + str(self.page) + self.end
            yield scrapy.Request(url=url, callback=self.parse)
