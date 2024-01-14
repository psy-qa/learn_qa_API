import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

methods = ['get', 'post', 'put', 'delete']

print('first question')
response_get = requests.get(url)
print(response_get.text)
response_post = requests.post(url)
print(response_post.text)
response_put = requests.put(url)
print(response_put.text)
response_delete = requests.delete(url)
print(response_delete.text)
print("\n")

print('second question')

response_head = requests.patch(url)
print(response_head.status_code)
response_patch = requests.patch(url)
print(response_patch.status_code)
print("\n")

print('third question')
response1 = requests.get(url=url, params={"method": "GET"})
print(response1.text)
response2 = requests.post(url=url, data={"method": "POST"})
print(response2.text)
response3 = requests.put(url=url, data={"method": "PUT"})
print(response3.text)
response4 = requests.delete(url=url, data={"method": "DELETE"})
print(response4.text)
print("\n")

for i in methods:
    if i == 'get':
        for j in methods:
            response = requests.get(url=url, params={'method': j.upper()})
            print(response.text)
            response = requests.get(url=url, data={'method': j.upper()})
            print(response.text)
        print('\n')
    elif i == 'post':
        for j in methods:
            response = requests.post(url=url, data={'method': j.upper()})
            print(response.text)
            response = requests.post(url=url, params={'method': j.upper()})
            print(response.text)
        print('\n')
    elif i == 'put':
        for j in methods:
            response = requests.put(url=url, data={'method': j.upper()})
            print(response.text)
            response = requests.put(url=url, params={'method': j.upper()})
            print(response.text)
        print('\n')
    elif i == 'delete':
        for j in methods:
            response = requests.put(url=url, data={'method': j.upper()})
            print(response.text)
            response = requests.put(url=url, params={'method': j.upper()})
            print(response.text)
        print('\n')
