###############################################################################################

import ast

###############################################################################################

def convert_weather_info(city: str, weather_info):
    
    #city_list = ast.literal_eval(city)
    city_list = city
    city_name = ''.join(city_list)

    start_day = weather_info[0]['fcstDate']
    start_time = weather_info[0]['fcstTime']
    
    converted_weather_info = []
    location_time_info = {'location' : city_name, 'day' : start_day, 'time' : start_time}
    forecast_info = {}
    
    for weather_ in weather_info:
        
        if weather_['fcstTime'] != start_time:
            location_time_info['forecast_info'] = forecast_info
            converted_weather_info.append(location_time_info)
            start_day = weather_['fcstDate']
            start_time = weather_['fcstTime']
            location_time_info = {'location' : city_name, 'day' : start_day, 'time' : start_time}
            forecast_info = {}
        
        forecast_info[weather_['category']] = weather_['fcstValue']
        
    location_time_info['forecast_info'] = forecast_info
    converted_weather_info.append(location_time_info)
    
    return converted_weather_info

###############################################################################################

# weather_info_ = [{'baseDate': '20240229', 'baseTime': '0500', 'category': 'TMP', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '2', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'UUU', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '1.2', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'VVV', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '0.9', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'VEC', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '233', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'WSD', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '1.5', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'SKY', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '4', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'PTY', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '0', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'POP', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '30', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'WAV', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '0', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'PCP', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '강수없음', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'REH', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '80', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'SNO', 'fcstDate': '20240302', 'fcstTime': '2300', 'fcstValue': '적설없음', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'TMP', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '2', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'UUU', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '1.3', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'VVV', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '0.9', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'VEC', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '235', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'WSD', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '1.6', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'SKY', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '4', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'PTY', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '0', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'POP', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '30', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'WAV', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '0', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'PCP', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '강수없음', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'REH', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '80', 'nx': '60', 'ny': '127'},
# {'baseDate': '20240229', 'baseTime': '0500', 'category': 'SNO', 'fcstDate': '20240303', 'fcstTime': '0000', 'fcstValue': '적설없음', 'nx': '60', 'ny': '127'}]
# convert_weather_info("['서울특별시','용산구','']", weather_info_)

###############################################################################################