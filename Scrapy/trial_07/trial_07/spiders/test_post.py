import scrapy
import json


class TestPostSpider(scrapy.Spider):
    name = 'test_post'
    allowed_domains = ['fanyi.baidu.com/sug']

    # start_urls = ['https://fanyi.baidu.com/sug']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'final',
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        # print(content)
        obj = json.loads(content)
        print(obj)
