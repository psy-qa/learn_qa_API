import requests

response = requests.get('https://playground.learnqa.ru/api/hello')
print(response.status_code)
print(response.json()['answer'])


payload = {"name": "Username"}

response1 = requests.get(url="https://playground.learnqa.ru/api/hello",params=payload)
print(response1.text)
