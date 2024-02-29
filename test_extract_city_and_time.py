import os
import openai

openai.api_key = 'api_key'

response = openai.ChatCompletion.create(
    model = 'gpt-4-0125-preview',
    messages = [
        {"role": "system", "content": "너는 문장에서 도시랑 시간을 추출하는 모델이야."},
        {"role": "system", "content": "도시는 '도', '시/구', '동'으로 구성되어 있어."},
        {"role": "system", "content": "서울/서울시/서울특별시의 경우에는 '서울특별시', '구', '동'으로 구성되어 있어."},
        {"role": "system", "content": "도시를 출력할 때는 '[도,시/구,동]'으로 출력하고 문장에서 비어있으면 해당 칸에 ''로만 추출해."},
        {"role": "system", "content": "시간은 지정된 시간인 경우에는, 'dd:hh:mm'으로 표현해줘. 이때 'dd'는 오늘이면 '00' 내일이면 '01'과 같이 오늘 기준 며칠인지야."},
        {"role": "system", "content": "시정된 시간이 아닌, 하루, 이틀과 같이 기간인 경우와 내일이나 지정된 날짜와 같이 날짜인 경우에는 'dd:dd'로 오늘을 기준으로 며칠에 시작이고 며칠에 끝나는지로 표현해줘. 기본 기준점은 오늘이야."},
        {"role": "system", "content": "출력은 '[도시정보],[도시정보],[시간정보]'와 같이 등장한 모든 도시 정보를 먼저 나열하고 마지막에 시간 정보를 알려줘."},
        {"role": "user", "content": "경기도 용인시와 서울시 용산구 한남동의 내일 16시 날씨를 알려줘."},
        {"role": "assistant", "content": "['경기도','용인시',''],['서울특별시','용산구','한남동'],['01:16:00']"},
        {"role": "user", "content": "이틀동안 제주도 여행 계획을 작성해줘"},
        {"role": "assistant", "content": "['제주도','',''],['00:01']"},
        {"role": "user", "content": "내일 나는 화천이랑 양주랑 인제를 여행할건데, 계획좀 짜줘."},
    ], 
    temperature = 0,
)

output_text = response["choices"][0]["message"]["content"]
print(output_text)

### {"role": "user", "content": "내일 17시에 부산광역시 서구에 놀려가야 하는데 날씨가 궁금해"},
### ['부산광역시','서구',''],['01:17:00']

### {"role": "user", "content": "내일부터 그 다음날까지 나는 경기도 용인시랑 서울 강남구를 여행할건데, 계획좀 짜줘."},
### ['경기도','용인시',''],['서울특별시','강남구',''],['01:02']

















