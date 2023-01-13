# _*_ coding : utf-8 _*_
# @Time : 2023/1/11 21:34
# @Author : Confetti-Lxy
# @File : trial_02
# @Project : Reptile

import urllib.request
from lxml import etree

url = 'https://www.baidu.com/'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)

tree = etree.HTML(content)
result = tree.xpath('//input[@id="su"]/@value')
print(result)
