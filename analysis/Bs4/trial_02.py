# _*_ coding : utf-8 _*_
# @Time : 2023/1/13 18:57
# @Author : Confetti-Lxy
# @File : trial_02
# @Project : Reptile

import urllib.request
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://www.starbucks.com.cn/menu/'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
        'Safari/537.36 Edg/111.0.0.0 '
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content, 'lxml')
a = soup.select('ul[class="grid padded-3 product"] strong')
name_list = []
for name in a:
    name_list.append(name.getText())
    print(name.string)
print(name_list)
# print(name_list)
# tree = etree.HTML(content)
# name_list = tree.xpath('//ul[@class="grid padded-3 product"]//strong/text()')
# print(name_list)
