# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 16:12
# @Author : Confetti-Lxy
# @File : trial_04
# @Project : Reptile

import urllib.request
import urllib.parse

# url = 'https://www.baidu.com/s?wd='
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'
}

# quote() 将一个词变为unicode编码
# name = urllib.parse.quote('周杰伦')
# url += name

# 当出现多个中文参数时,quote()使用起来较为麻烦
# 如:https://www.baidu.com/s?wd=周杰伦&sex=男
# data = {'wd': '周杰伦', 'sex': '男'}
# a = urllib.parse.urlencode(data)

base_url = 'https://www.baidu.com/s?'
data = {'wd': '周杰伦', 'sex': '男', 'location': '中国台湾省'}
new_data = urllib.parse.urlencode(data)
url = base_url + new_data

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
