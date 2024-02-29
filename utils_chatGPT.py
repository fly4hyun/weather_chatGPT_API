###############################################################################################

import os
import openai

###############################################################################################

openai.api_key = 'api_key'

def extract_city_and_time(quest: str, date: str, time: str):
    
    response = openai.ChatCompletion.create(
        model = 'gpt-4-0125-preview',
        messages = [
            {"role": "system", "content": "너는 문장에서 도시랑 시간을 추출하는 모델이야."},
            {"role": "system", "content": "도시는 '도', '시/구', '동'으로 구성되어 있어."},
            {"role": "system", "content": "서울/서울시/서울특별시의 경우에는 '서울특별시', '구', '동'으로 구성되어 있어."},
            {"role": "system", "content": "도시를 출력할 때는 '[도,시/구,동]'으로 출력하고 문장에서 비어있으면 해당 칸에 ''로만 추출해."},
            {"role": "system", "content": "시간은 지정된 시간인 경우에는, 'dd:hh:mm'으로 표현해줘. 이때 'dd'는 오늘이면 '00' 내일이면 '01'과 같이 오늘 기준 며칠인지야."},
            {"role": "system", "content": "시정된 시간이 아닌, 하루, 이틀과 같이 기간인 경우에는 'dd:dd'로 오늘을 기준으로 며칠부터 며칠인지로 표현해줘. 기본 기준점은 오늘이야."},
            {"role": "system", "content": "출력은 '[도시정보],[도시정보],[시간정보]'와 같이 등장한 모든 도시 정보를 먼저 나열하고 마지막에 시간 정보를 알려줘."},
            {"role": "system", "content": "참고로, 오늘의 날짜는 " + date + " 이고, 지금 시간은 " + time + " 이야."},
            {"role": "user", "content": "경기도 용인시와 서울시 용산구 한남동의 내일 16시 날씨를 알려줘."},
            {"role": "assistant", "content": "['경기도','용인시',''],['서울특별시','용산구','한남동'],['01:16:00']"},
            {"role": "user", "content": "이틀동안 제주도 여행 계획을 작성해줘"},
            {"role": "assistant", "content": "['제주도','',''],['00:01']"},
            {"role": "user", "content": quest},
        ], 
        temperature = 0,
    )

    return response["choices"][0]["message"]["content"]

### 내일 17시에 부산광역시 서구에 놀려가야 하는데 날씨가 궁금해
### ['부산광역시','서구',''],['01:17:00']

###############################################################################################

openai.api_key = 'api_key'

def recommend_weather(quest: str, cities_info: str, date: str, time: str):
    
    response = openai.ChatCompletion.create(
        model = 'gpt-4-0125-preview',
        messages = [
            {"role": "system", "content": "너는 날씨 정보랑 여행 계획을 짜주는 모델이야."},
            {"role": "system", "content": str(cities_info)},
            {"role": "system", "content": "계획을 짤 때에는, 전반적인 날씨에 대한 간략한 요약을 우선 말하고, 시간 단위로 날씨를 고려해서 짜줘"},
            {"role": "system", "content": "날씨만을 답변할 때에는 구어체를 이용해서 서술을 한 다음, 각 항목을 나타내줘."},
            {"role": "system", "content": "참고로, 오늘의 날짜는 " + date + " 이고, 지금 시간은 " + time + " 이야."},
            {"role": "user", "content": "오늘 서울 종로에서 출발하여 경기도 화성시를 여행갈거야. 여행계획을 짜줘"},
            {"role": "assistant", "content": "날씨요약내용\n### **1일차: 서울 종로구 -> 경기도 화성시**\n- **출발지:** 서울 종로구\n- **목적지:** 경기도 화성시\n- **날짜:** 20240301\n- **날씨 예보:** 한낮 기온이 대체로 7°C로 예상되며, 맑은 날씨가 지속될 전망입니다. 강수 확률이 낮으므로 야외 활동하기 좋은 날입니다.\n- **여행 일정:**\n    - 오전 9시: 서울 종로구에서 출발\n    - 오전 11시: 화성 동탄 롯데프리미엄 아울렛 도착 및 쇼핑\n    - 오후 1시: 점심 식사 (화성 지역의 유명한 한식 혹은 특색 있는 식당)\n    - 오후 2시30분: 제부도 탐방 (바다와 자연 경관 즐기기)\n    - 오후 5시: 화성 방문 전시관 혹은 문화시설 둘러보기\n    - 저녁 7시: 화성시 내 숙소 체크인 및 저녁 식사\n\n이 여행 계획은 날씨 예보 및 개인 취향에 따라 유연하게 조정 가능합니다. 중간에 휴식 시간을 충분히 가지며, 각 지역의 문화와 자연을 만끽하세요. 안전한 여행 되시길 바랍니다!"},
            {"role": "user", "content": quest},
        ], 
        temperature = 0.3,
        stream = True,
    )

    return response["choices"][0]["message"]["content"]

###############################################################################################

openai.api_key = 'api_key'

def recommend_weather_message(quest: str, cities_info: str, date: str, time: str):
    
    messages = [
        {"role": "system", "content": "너는 날씨 정보랑 여행 계획을 짜주는 모델이야."},
        {"role": "system", "content": str(cities_info)},
        {"role": "system", "content": "계획을 짤 때에는, 전반적인 날씨에 대한 간략한 요약을 우선 말하고, 시간 단위로 날씨를 고려해서 짜줘"},
        {"role": "system", "content": "날씨만을 답변할 때에는 구어체를 이용해서 서술을 한 다음, 각 항목을 나타내줘."},
        {"role": "system", "content": "참고로, 오늘의 날짜는 " + date + " 이고, 지금 시간은 " + time + " 이야."},
        {"role": "user", "content": "오늘 서울 종로에서 출발하여 경기도 화성시를 여행갈거야. 여행계획을 짜줘"},
        {"role": "assistant", "content": "날씨요약내용\n### **1일차: 서울 종로구 -> 경기도 화성시**\n- **출발지:** 서울 종로구\n- **목적지:** 경기도 화성시\n- **날짜:** 20240301\n- **날씨 예보:** 한낮 기온이 대체로 7°C로 예상되며, 맑은 날씨가 지속될 전망입니다. 강수 확률이 낮으므로 야외 활동하기 좋은 날입니다.\n- **여행 일정:**\n    - 오전 9시: 서울 종로구에서 출발\n    - 오전 11시: 화성 동탄 롯데프리미엄 아울렛 도착 및 쇼핑\n    - 오후 1시: 점심 식사 (화성 지역의 유명한 한식 혹은 특색 있는 식당)\n    - 오후 2시30분: 제부도 탐방 (바다와 자연 경관 즐기기)\n    - 오후 5시: 화성 방문 전시관 혹은 문화시설 둘러보기\n    - 저녁 7시: 화성시 내 숙소 체크인 및 저녁 식사\n\n이 여행 계획은 날씨 예보 및 개인 취향에 따라 유연하게 조정 가능합니다. 중간에 휴식 시간을 충분히 가지며, 각 지역의 문화와 자연을 만끽하세요. 안전한 여행 되시길 바랍니다!"},
        {"role": "user", "content": quest},
    ]

    return messages

###############################################################################################

# question = '이틀동안 강원도 여행 계획을 작성해줘'
# infos = [[{'location': '강원도', 'day': '20240229', 'time': '0600', 'forecast_info': {'TMP': '0', 'UUU': '-0.3', 'VVV': '-0.6', 'VEC': '34', 'WSD': '0.7', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '90', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '0700', 'forecast_info': {'TMP': '0', 'UUU': '-0.2', 'VVV': '-0.8', 'VEC': '21', 'WSD': '0.9', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '90', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '0800', 'forecast_info': {'TMP': '0', 'UUU': '0.1', 'VVV': '-0.8', 'VEC': '353', 'WSD': '0.8', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '90', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '0900', 'forecast_info': {'TMP': '1', 'UUU': '0.2', 'VVV': '-0.6', 'VEC': '342', 'WSD': '0.6', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '85', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1000', 'forecast_info': {'TMP': '3', 'UUU': '0', 'VVV': '0.6', 'VEC': '180', 'WSD': '0.6', 'SKY': '4', 'PTY': '0', 'POP': '30', 'WAV': '0', 'PCP': '강수없음', 'REH': '80', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1100', 'forecast_info': {'TMP': '4', 'UUU': '0.4', 'VVV': '-0.5', 'VEC': '321', 'WSD': '0.6', 'SKY': '4', 'PTY': '0', 'POP': '30', 'WAV': '0', 'PCP': '강수없음', 'REH': '70', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1200', 'forecast_info': {'TMP': '5', 'UUU': '0.6', 'VVV': '-0.3', 'VEC': '297', 'WSD': '0.7', 'SKY': '4', 'PTY': '0', 'POP': '30', 'WAV': '0', 'PCP': '강수없음', 'REH': '60', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1300', 'forecast_info': {'TMP': '6', 'UUU': '0.9', 'VVV': '0.4', 'VEC': '246', 'WSD': '1', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '55', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1400', 'forecast_info': {'TMP': '7', 'UUU': '1.5', 'VVV': '-0.4', 'VEC': '285', 'WSD': '1.6', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '50', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1500', 'forecast_info': {'TMP': '8', 'UUU': '2.1', 'VVV': '-0.9', 'VEC': '293', 'WSD': '2.3', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '50', 'SNO': '적설없음', 'TMX': '9.0'}}, {'location': '강원도', 'day': '20240229', 'time': '1600', 'forecast_info': {'TMP': '8', 'UUU': '2', 'VVV': '-1.3', 'VEC': '303', 'WSD': '2.4', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '45', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1700', 'forecast_info': {'TMP': '8', 'UUU': '1.7', 'VVV': '-0.6', 'VEC': '289', 'WSD': '1.8', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '40', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1800', 'forecast_info': {'TMP': '7', 'UUU': '1.4', 'VVV': '-0.2', 'VEC': '278', 'WSD': '1.4', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '45', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '1900', 'forecast_info': {'TMP': '5', 'UUU': '1.7', 'VVV': '-0.7', 'VEC': '292', 'WSD': '1.8', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '50', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '2000', 'forecast_info': {'TMP': '4', 'UUU': '1.7', 'VVV': '-1.2', 'VEC': '305', 'WSD': '2.1', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '55', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '2100', 'forecast_info': {'TMP': '3', 'UUU': '1.7', 'VVV': '-1.3', 'VEC': '307', 'WSD': '2.1', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '60', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '2200', 'forecast_info': {'TMP': '2', 'UUU': '1.8', 'VVV': '-1.3', 'VEC': '306', 'WSD': '2.2', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '60', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240229', 'time': '2300', 'forecast_info': {'TMP': '1', 'UUU': '1.7', 'VVV': '-1.1', 'VEC': '303', 'WSD': '2', 'SKY': '3', 'PTY': '0', 'POP': '20', 'WAV': '0', 'PCP': '강수없음', 'REH': '60', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0000', 'forecast_info': {'TMP': '0', 'UUU': '1.9', 'VVV': '-1.1', 'VEC': '300', 'WSD': '2.2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '55', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0100', 'forecast_info': {'TMP': '-1', 'UUU': '2.3', 'VVV': '-1.2', 'VEC': '298', 'WSD': '2.6', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '55', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0200', 'forecast_info': {'TMP': '-2', 'UUU': '2.7', 'VVV': '-1.5', 'VEC': '299', 'WSD': '3.1', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '60', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0300', 'forecast_info': {'TMP': '-2', 'UUU': '3', 'VVV': '-1.7', 'VEC': '300', 'WSD': '3.4', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '60', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0400', 'forecast_info': {'TMP': '-3', 'UUU': '2.9', 'VVV': '-1.8', 'VEC': '302', 'WSD': '3.4', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '55', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0500', 'forecast_info': {'TMP': '-4', 'UUU': '2.8', 'VVV': '-1.9', 'VEC': '304', 'WSD': '3.4', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '45', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0600', 'forecast_info': {'TMP': '-5', 'UUU': '2.7', 'VVV': '-1.9', 'VEC': '305', 'WSD': '3.3', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '45', 'SNO': '적설없음', 'TMN': '-6.0'}}, {'location': '강원도', 'day': '20240301', 'time': '0700', 'forecast_info': {'TMP': '-6', 'UUU': '2.6', 'VVV': '-1.6', 'VEC': '302', 'WSD': '3.1', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강 수없음', 'REH': '45', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0800', 'forecast_info': {'TMP': '-5', 'UUU': '3.1', 'VVV': '-1.9', 'VEC': '302', 'WSD': '3.6', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '40', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '0900', 'forecast_info': {'TMP': '-5', 'UUU': '3.6', 'VVV': '-2.1', 'VEC': '300', 'WSD': '4.2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '40', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1000', 'forecast_info': {'TMP': '-3', 'UUU': '3.9', 'VVV': '-2', 'VEC': '297', 'WSD': '4.4', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '30', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1100', 'forecast_info': {'TMP': '-2', 'UUU': '4.1', 'VVV': '-1.9', 'VEC': '295', 'WSD': '4.5', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '25', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1200', 'forecast_info': {'TMP': '-1', 'UUU': '4.4', 'VVV': '-1.6', 'VEC': '290', 'WSD': '4.7', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '20', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1300', 'forecast_info': {'TMP': '-1', 'UUU': '4.8', 'VVV': '-1.5', 'VEC': '287', 'WSD': '5', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '20', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1400', 'forecast_info': {'TMP': '-1', 'UUU': '4.9', 'VVV': '-1.8', 'VEC': '290', 'WSD': '5.2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '20', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1500', 'forecast_info': {'TMP': '-1', 'UUU': '4.5', 'VVV': '-2.2', 'VEC': '296', 'WSD': '5', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '20', 'SNO': '적설없음', 'TMX': '0.0'}}, {'location': '강원도', 'day': '20240301', 'time': '1600', 'forecast_info': {'TMP': '-2', 'UUU': '4.1', 'VVV': '-2.2', 'VEC': '298', 'WSD': '4.7', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '20', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1700', 'forecast_info': {'TMP': '-2', 'UUU': '3.7', 'VVV': '-1.9', 'VEC': '297', 'WSD': '4.2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '25', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1800', 'forecast_info': {'TMP': '-3', 'UUU': '2.9', 'VVV': '-1.4', 'VEC': '296', 'WSD': '3.2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '25', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '1900', 'forecast_info': {'TMP': '-4', 'UUU': '2', 'VVV': '-0.7', 'VEC': '289', 'WSD': '2.1', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '30', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '2000', 'forecast_info': {'TMP': '-5', 'UUU': '1.9', 'VVV': '-0.6', 'VEC': '288', 'WSD': '2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '35', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '2100', 'forecast_info': {'TMP': '-5', 'UUU': '1.9', 'VVV': '-0.5', 'VEC': '285', 'WSD': '2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '40', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '2200', 'forecast_info': {'TMP': '-6', 'UUU': '2', 'VVV': '-0.4', 'VEC': '281', 'WSD': '2', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '40', 'SNO': '적설없음'}}, {'location': '강원도', 'day': '20240301', 'time': '2300', 'forecast_info': {'TMP': '-6', 'UUU': '1.8', 'VVV': '-0.1', 'VEC': '273', 'WSD': '1.8', 'SKY': '1', 'PTY': '0', 'POP': '0', 'WAV': '0', 'PCP': '강수없음', 'REH': '50', 'SNO': '적설없음'}}]]

# aaaaa = recommend_weather(question, infos, '20240229')
