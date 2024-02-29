###############################################################################################

import ast
from datetime import timedelta, datetime

###############################################################################################

def time_to_value(today: str, time: str, api_responses: list):
    
    #time = ast.literal_eval(time)
    
    time_info = time[0].split(":")
    
    today = datetime.strptime(today, '%Y%m%d')
    day_added = today + timedelta(days=int(time_info[0]))
    day_added = day_added.strftime('%Y%m%d')
    
    target_time = time_info[1] + '00'
    
    target_weather_info = []
    
    ### 최적화 필요 일단 넘어감
    for api_response in api_responses:
        if api_response['fcstDate'] == day_added and api_response['fcstTime'] == target_time:
            target_weather_info.append(api_response)

    return target_weather_info

###############################################################################################

def period_to_value(today: str, time: str, api_responses: list):
    
    #time = ast.literal_eval(time)
    
    time_info = time[0].split(":")
    
    today = datetime.strptime(today, '%Y%m%d')
    start_day = today + timedelta(days=int(time_info[0]))
    end_day = today + timedelta(days=int(time_info[1]))
    start_day = start_day.strftime('%Y%m%d')
    end_day = end_day.strftime('%Y%m%d')
    
    target_weather_info = []
    
    ### 최적화 필요 일단 넘어감
    for api_response in api_responses:
        if api_response['fcstDate'] == start_day or api_response['fcstDate'] == end_day:
            target_weather_info.append(api_response)

    return target_weather_info

###############################################################################################

# import requests
# from datetime import datetime
# import xmltodict


# url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
# service_key = 'service_key'

# # URL에 serviceKey를 직접 추가
# full_url = f"{url}?serviceKey={service_key}"

# params = {
#     'pageNo': '1', 
#     'numOfRows': '1000', 
#     'dataType': 'XML', 
#     'base_date': '20240229', 
#     'base_time': '0500', 
#     'nx': '60', 
#     'ny': '127'
# }

# res = requests.get(full_url, params=params)
# xml_data = res.text
# dict_data = xmltodict.parse(xml_data)

# api_responses = dict_data['response']['body']['items']['item']

# aaa = period_to_value('20240229', '["00:01"]', api_responses)

# for aaaa in aaa:
    
#     print(aaaa)
    
###############################################################################################


