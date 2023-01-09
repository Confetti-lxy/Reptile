# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 22:48
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100:90&action=&start=0&limit=20'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# open方法默认的为gbk编码,因此保存中文时需要指定utf-8编码
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
