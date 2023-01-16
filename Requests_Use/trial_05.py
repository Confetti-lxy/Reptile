# _*_ coding : utf-8 _*_
# @Time : 2023/1/16 21:56
# @Author : Confetti-Lxy
# @File : trial_05
# @Project : Reptile

import requests
import urllib.request
from bs4 import BeautifulSoup

# __VIEWSTATE:+V7+NpF9MrhAeX9juwaLeaWw/Uaiw2xIce4qxTJE5xWLkp51NIkyalzy8PLkqsAEuGRX3484A2NIcrohWAWOh+oFDzKT6S9sQ5r46lT9zGmYcx/+qn5cDGZyX9j6/WO18+OyM4B8fFaFruA45795+gEupKc=
# __VIEWSTATEGENERATOR:C93BE1AE
# from:http://so.gushiwen.cn/user/collect.aspx?type=s
# email:3038454387@qq.com
# pwd:123456
# code:BLSR
# denglu:登录

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx?type=s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52',

}

response = requests.get(url=url, headers=headers)
content = response.text
soup = BeautifulSoup(content, 'lxml')
viewState = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewStateGenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
codeImg = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn/' + codeImg
# urllib.request.urlretrieve(url=code_url, filename='code.jpg') 不行,上一次的不是这一次的验证码
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
    print('code saved!')
code_name = input('imgCode:')

# 登陆
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx?type=s'
data_post = {
    '__VIEWSTATE': viewState,
    '__VIEWSTATEGENERATOR': viewStateGenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx?type=s',
    'email': '3038454387@qq.com',
    'pwd': 'LXY200210254718',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
    print('end!')
