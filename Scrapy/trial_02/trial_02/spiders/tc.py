import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['su.58.com/sou/?key=前端开发&classpolicy=classify_D']
    start_urls = ['https://su.58.com/sou/?key=前端开发&classpolicy=classify_D']

    def parse(self, response):
        span_list = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')
        print('================================')
        print(span_list[0].extract())
        print('================================')
