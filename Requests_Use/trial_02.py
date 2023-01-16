# _*_ coding : utf-8 _*_
# @Time : 2023/1/15 21:37
# @Author : Confetti-Lxy
# @File : trial_02
# @Project : Reptile

import requests

url = 'http://www.baidu.com/s'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': 'BIDUPSID=36632A74BBAC3093B8AB24C3DD4CAC67; PSTM=1670218534; BAIDUID=0D90323E675C614A36CF36608B8D23EA:FG=1; BD_UPN=123253; ZFY=Vh9aHxpyq2alr172dpPt262CrBJgK56vJPRCWGIjkxU:C; BAIDUID_BFESS=0D90323E675C614A36CF36608B8D23EA:FG=1; B64_BOT=1; BDRCVFR[ibifSmLtzfY]=mk3SLVN4HKm; delPer=0; PSINO=5; BD_HOME=1; H_PS_PSSID=36548_37647_38011_36920_37990_37933_26350_37957_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=925aO3YInbsgUPkGzvfyq4n3cQcsDyAIq9rZNOulPKAhBsXAilD1NIAHosI; BA_HECTOR=8ha1248k058l8ha4008h0g7u1hs82e41l; baikeVisitId=03fcbc78-d2f9-42db-ab6e-d900e7364eb1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52',
}

data = {
    'wd': '北京',
}

response = requests.get(url=url, params=data, headers=headers)
response.encoding = 'utf-8'
print(response.text)
