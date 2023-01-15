# _*_ coding : utf-8 _*_
# @Time : 15/01/2023 14:15
# @Author : Confetti-Lxy
# @File : trial_01
# @Project : Reptile

import requests

url = 'https://www.baidu.com'
response = requests.get(url)

response.encoding = 'utf-8'
print(response.text)
print(response.url)
print(response.headers)
print(response.content)
print(response.status_code)
