
###############################################################################################

from datetime import datetime
import ast
import openai

from utils_chatGPT import extract_city_and_time, recommend_weather_message
from utils_location import city_to_xy, request_weather
from utils_time import time_to_value, period_to_value
from utils import convert_weather_info

###############################################################################################

current_date = datetime.now()
today_date = current_date.strftime('%Y%m%d')
now_time = current_date.strftime('%H:%M:%S')

###############################################################################################

question = input("질문을 입력해주세요.")
#question = '내일 17시에 부산광역시 서구와 서울 종로구에 놀려가야 하는데 날씨가 궁금해'
#question = '이틀동안 강원도 여행 계획을 작성해줘'

###############################################################################################

response = extract_city_and_time(question, today_date, now_time)
response_list = eval(f"[{response}]")

cities_info = []
time_info = response_list[-1]

for city_info in response_list[:-1]:
    
    nx, ny = city_to_xy(city_info)
    weather_api_responses = request_weather(today_date, nx, ny)

    if len(time_info[0]) == 8:
        target_weather_info = time_to_value(today_date, time_info, weather_api_responses)
    elif len(time_info[0]) == 5:
        target_weather_info = period_to_value(today_date, time_info, weather_api_responses)

    converted_weather_info = convert_weather_info(city_info, target_weather_info)
    cities_info.append(converted_weather_info)

###############################################################################################

final_message = recommend_weather_message(question, cities_info, today_date, now_time)

response = openai.ChatCompletion.create(
    model = 'gpt-4-0125-preview',
    messages = final_message,
    temperature = 0.9,
    stream = True,
)

for chunk in response:
    
    try:
        print(chunk.choices[0].delta.content, end = '')
    except:
        print()

###############################################################################################




###############################################################################################















