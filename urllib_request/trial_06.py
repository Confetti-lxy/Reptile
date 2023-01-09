# _*_ coding : utf-8 _*_
# @Time : 08/01/2023 21:58
# @Author : Confetti-Lxy
# @File : trial_06
# @Project : Reptile

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    'Cookie': 'BIDUPSID=67A8780116E8C8CAB85376240D48A0D0; PSTM=1663771043; BAIDUID=67A8780116E8C8CA4BF51893B4B2FA77:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1669859464,1669886261,1669955672,1670079592; BDUSS=g1RnhtQVFmeTJnMWhJVjMtTzFzd1dwWU5pYkxQdnR6Ymg2bUQtMHowMjBXOEZqSUFBQUFBJCQAAAAAAAAAAAEAAABH6mV53Pi7zbXEuqO9xwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALTOmWO0zpljRF; BDUSS_BFESS=g1RnhtQVFmeTJnMWhJVjMtTzFzd1dwWU5pYkxQdnR6Ymg2bUQtMHowMjBXOEZqSUFBQUFBJCQAAAAAAAAAAAEAAABH6mV53Pi7zbXEuqO9xwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALTOmWO0zpljRF; BA_HECTOR=808ka5ag05ak20050g052l4l1hrl0co1k; BAIDUID_BFESS=67A8780116E8C8CA4BF51893B4B2FA77:FG=1; ZFY=N3QVzbBu5XG1jcCKZE:Bno:AJ8jHHZeL:BJFXhozkKPHTE:C; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ab_sr=1.0.1_MGVjZDcwZjgxNGNkYmIxZmI4MDE0MmQ5NzVmNmY2NmQ3NjA3MjNkNzhjZWVkYWRjYjI4MDMyNDFmZWJjMDY5Y2FkNmExYzhiM2NjOTE1YmRiMzgxMWJkOWNmN2NmYzBkZjg0YThhNDM5YjNiOTE4OWNmMjA0MTNkYjFlODUxOWQ2M2Y3ZTBiMDE3MjE2YTFkYWI4ZmJlZDE4MDUyMDQ1MTZmMzMwNjkyNzhmNzQ0MjIxZDFmZjU0NGE1ZjU5ZjY3',
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '73313d8f609d908bdca91aefbe8b8e7a',
    'domain': 'common',
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)
