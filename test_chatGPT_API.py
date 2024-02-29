


import os
import openai

openai.api_key = 'api_key'

response = openai.ChatCompletion.create(
    model = 'gpt-4-0125-preview',
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

output_text = response["choices"][0]["message"]["content"]
print(output_text)





















