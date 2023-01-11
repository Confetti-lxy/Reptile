# _*_ coding : utf-8 _*_
# @Time : 2023/1/11 22:01
# @Author : Confetti-Lxy
# @File : trial_03
# @Project : Reptile


import urllib.request
import urllib.parse
from lxml import etree

base_url = 'https://sc.chinaz.com/tupian/ribenmeinv_'


def create_request(p):
    if p == 1:
        u = 'https://sc.chinaz.com/tupian/ribenmeinv.html'
    else:
        u = base_url + str(p) + '.html'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
            'Safari/537.36 Edg/111.0.0.0 '
    }
    r = urllib.request.Request(url=u, headers=headers)
    return r


def get_content(r):
    response = urllib.request.urlopen(r)
    c = response.read().decode('utf-8')
    return c


def download(c):
    tree = etree.HTML(c)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    src_list = tree.xpath('//div[@class="container"]//img/@data-original')
    for i in range(len(name_list)):
        name = '/Users/mac/Desktop/Reptile/img/' + name_list[i] + '.jpg'
        url = 'https:' + src_list[i]
        url = url.replace('_s', "")
        urllib.request.urlretrieve(url=url, filename=name)


if __name__ == '__main__':
    start_page = int(input('please enter the start page:'))
    end_page = int(input('please enter the end page:'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(content)
        print('page ' + str(page) + ' has finished!')
    print("end!")
