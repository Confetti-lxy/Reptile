# _*_ coding : utf-8 _*_
# @Time : 2023/1/16 21:46
# @Author : Confetti-Lxy
# @File : trial_04
# @Project : Reptile

import requests

url = 'http://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52',
    'Cookie': 'BIDUPSID=36632A74BBAC3093B8AB24C3DD4CAC67; PSTM=1670218534; BAIDUID=0D90323E675C614A36CF36608B8D23EA:FG=1; BD_UPN=123253; ab_sr=1.0.1_ZmQwM2ZmYTdmM2I4Njc0Njk0YTQ2NGQ5MGU5MGJhODViYzE1MDQ2MWU2MzJjMjNjNzBiOTFlYjY2MzQzMDU0OWVkNTNhYTZlNGVmOGM4ZDdhMTQ3MDJmZTVjMDE2NzQyYjk3YjRmODY3MTk3Mzc1ZmRlZmM1ZTJjYmMwNTM5MDMzMDcyY2NhYWQxMmU5MjNmMmUxYTI1OWVmYWFmYzU2MQ==; H_PS_PSSID=36548_37647_38011_36920_37990_37933_26350_37957_37881; H_PS_645EC=7dafYqo2r/piUMVgdOuy4IegYTE0J+ibnbdrL9vzXgIDr7LzRjIFoNw/WMM; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=0D90323E675C614A36CF36608B8D23EA:FG=1; baikeVisitId=bc910f68-ad65-4a8e-83aa-5087ea3be265',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

data = {
    'wd': 'ip',
}

response = requests.get(url=url, params=data, headers=headers)
content = response.text
with open('daiLi.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
