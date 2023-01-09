# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 23:03
# @Author : Confetti-Lxy
# @File : trial_02
# @Project : Reptile

import urllib.request
import urllib.parse


def create_request(p):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100:90&action=&'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'
    }
    data = {
        'start': (p - 1) * 20,
        'limit': 20,
    }
    url = base_url + urllib.parse.urlencode(data)
    print(url)
    r = urllib.request.Request(url=url, headers=headers)
    return r


def get_content(r):
    response = urllib.request.urlopen(r)
    c = response.read().decode('utf-8')
    return c


def download(c, p: int):
    name = 'douban' + str(p) + '.json'
    with open(name, 'w', encoding='utf-8') as fp:
        fp.write(c)


if __name__ == '__main__':
    start_page = int(input('please enter the start page:'))
    end_page = int(input('please enter the end page:'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(content, page)
    print('end!')
