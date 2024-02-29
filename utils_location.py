###############################################################################################

import pandas as pd
import ast

import requests
from datetime import datetime
import xmltodict

###############################################################################################

# 'example.csv' 파일을 DataFrame으로 읽기
df = pd.read_csv('location.csv', encoding='cp949')

# 관심 있는 컬럼만 추출
df = df[['first', 'second', 'third', 'x', 'y']]

# 계층적인 딕셔너리를 생성하기 위한 함수
def create_nested_dict(df):
    result_dict = {}
    for _, row in df.iterrows():
        first, second, third, x, y = row['first'], row['second'], row['third'], row['x'], row['y']
        if pd.isna(first):
            continue
        if first not in result_dict:
            result_dict[first] = {'x': str(x), 'y': str(y)}
        if pd.notna(second):
            if second not in result_dict[first]:
                result_dict[first][second] = {'x': str(x), 'y': str(y)}
            if pd.notna(third):
                result_dict[first][second][third] = {'x': str(x), 'y': str(y)}
    return result_dict

###############################################################################################

# 딕셔너리 생성
location_dict = create_nested_dict(df)
location_copy_dict = dict(location_dict)

###############################################################################################

def city_to_xy(city_info: str):
    
    global location_dict
    location_copy_dict = dict(location_dict)

    #city_list = ast.literal_eval(city_info)
    city_list = city_info
    
    try:
        result = location_copy_dict[city_list[0]]
    except:
        ### locaton에 없을 시 예외처리
        raise Exception("location error")
        
    else:
        for city in city_list:
            if city in location_copy_dict:
                location_copy_dict = location_copy_dict[city]
            else:
                x = location_copy_dict['x']
                y = location_copy_dict['y']
                
                break
            
    x = location_copy_dict['x']
    y = location_copy_dict['y']
    
    return x, y

### print(city_to_xy("['서울특별시','용산구','']"))
### ('60', '126')

###############################################################################################

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
service_key = 'service_key'

# URL에 serviceKey를 직접 추가
full_url = f"{url}?serviceKey={service_key}"

###############################################################################################

def request_weather(base_date: str, nx: str, ny: str):
    
    global full_url
    
    params = {
        'pageNo': '1', 
        'numOfRows': '1000', 
        'dataType': 'XML', 
        'base_date': base_date, 
        'base_time': '0500', 
        'nx': nx, 
        'ny': ny
    }
    
    res = requests.get(full_url, params=params)
    xml_data = res.text
    dict_data = xmltodict.parse(xml_data)
    
    api_responses = dict_data['response']['body']['items']['item']
    
    return api_responses

###############################################################################################

### print(request_weather('20240229', '60', '127'))

###############################################################################################