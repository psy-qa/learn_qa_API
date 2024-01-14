import time

import requests

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

get_token = requests.get(url=url).json()
token = get_token['token']
seconds = get_token["seconds"]
print(get_token)
result_execute = requests.get(url=url, params={"token": token}).json()
print(result_execute['status'])
print("\n")
time.sleep(seconds)
try:
    result_execute_complite = requests.get(url=url, params={"token": token}).json()
    if result_execute_complite['result'] and result_execute_complite['status']:
        if result_execute_complite['status'] == 'Job is ready':
            print('Результат: ', result_execute_complite['result'], '\n', 'Статус: ',
                  result_execute_complite['status'], sep='')
        else:
            print('WRONG RESPONSE PARAMS')
except:
    print('WRONG REQUEST')
