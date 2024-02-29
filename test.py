import requests
from datetime import datetime
import xmltodict


url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
service_key = '7i9BdFoGGNdILy59nG6hK7i6D2FIfZvfiBXf%2BEsRXYgLQWCjfjo2JKON9qqBrkZcPA6ovPEkSdM90R8D%2BrCPHw%3D%3D'

# URL에 serviceKey를 직접 추가
full_url = f"{url}?serviceKey={service_key}"

params = {
    'pageNo': '1', 
    'numOfRows': '12', 
    'dataType': 'XML', 
    'base_date': '20240229', 
    'base_time': '0500', 
    'nx': '60', 
    'ny': '127'
}

res = requests.get(full_url, params=params)
xml_data = res.text
dict_data = xmltodict.parse(xml_data)

api_responses = dict_data['response']['body']['items']['item']

for a in api_responses:
    print(a)

