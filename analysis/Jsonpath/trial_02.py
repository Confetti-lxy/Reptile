# _*_ coding : utf-8 _*_
# @Time : 2023/1/13 15:42
# @Author : Confetti-Lxy
# @File : trial_02
# @Project : Reptile

import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1673595819773_104&jsoncallback=jsonp105&action' \
      '=cityAction&n_s=new&event_submit_doGetAllRegion=trues '
headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1673595819773_104&jsoncallback=jsonp105&action=cityAction&n_s=new'
    #          '&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.2.3',
    'cookie': 't=54a304adfd76fd8866c42b3ea71eb935; cookie2=1818c3f2445c3f807b09311f5e17e528; v=0; '
              '_tb_token_=e57eb313e873e; cna=RasdHDCxnRACASSYGJhl/E69; '
              'l=fBPKiV9lTCPJKbQXBOfanurza779lIRASuPzaNbMi9fPO_fH54jhW6RX_08MCnhVFsYBR3l94-XHBeYBcG0sjqj4axom47MmnmOk'
              '-Wf..; tfstk=ci1NBVwRVIjBnyQY2BAVLaYwB8JOaV1lMD8XIokXS-8TerpM4sxtDeb3xpJS8mvG.; '
              'isg=BK-vcSNaEOeGcxTaTdOzoGr8PsW5VAN26EZHFsE8L54lEM8SySRRxvmOkwAuRdvu',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.49',
    'x-requested-with': 'XMLHttpRequest',
}

# 获取json数据
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]
# print(content)
with open('trial_02.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

# json数据分析
# obj = json.load(open('trial_02.json', encoding='utf-8'))
# city_list = jsonpath.jsonpath(obj, '$..regionName')
# print(city_list)
