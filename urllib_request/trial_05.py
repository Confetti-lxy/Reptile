# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 21:43
# @Author : Confetti-Lxy
# @File : trial_05
# @Project : Reptile

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'
}
data = {
    'kw': 'spider'
}

# post的请求的参数必须要进行编码->调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
# print(data)

# post的请求参数是不会拼接在url后面的,会放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)

# string->json
obj = json.loads(content)
print(obj)
