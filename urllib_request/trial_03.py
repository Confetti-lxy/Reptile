# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 15:59
# @Author : Confetti-Lxy
# @File : trial_03
# @Project : Reptile

import urllib.request

url = 'https://www.baidu.com'

# UA
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
