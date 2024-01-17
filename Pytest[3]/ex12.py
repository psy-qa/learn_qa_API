import requests

def test_method_headers_api():

    response = requests.post("https://playground.learnqa.ru/api/homework_header")
    print('\n', response.headers)
    print(response.headers['x-secret-homework-header'])
    assert response.status_code == 200, 'This response have incorrect status code'
    assert 'x-secret-homework-header' in response.headers, 'Reponse dont have needed header in headers'
    assert response.headers['x-secret-homework-header'] == 'Some secret value', "Response have diff value in x-secret-homework-header "