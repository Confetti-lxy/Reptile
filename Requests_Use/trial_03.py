# _*_ coding : utf-8 _*_
# @Time : 2023/1/15 22:39
# @Author : Confetti-Lxy
# @File : trial_03
# @Project : Reptile

import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52',

}

data = {
    'kw': 'some',
}

response = requests.post(url=url, data=data, headers=headers)
content = response.text
obj = json.loads(content)
print(obj)
print(response.json())
