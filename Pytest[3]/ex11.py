import requests


def test_cookie_method_api():
    response = requests.post("https://playground.learnqa.ru/api/homework_cookie")
    assert response.status_code == 200, 'This response have incorrect status code'
    assert response.cookies, 'This response dont have cookie in headers'
    assert response.cookies['HomeWork'] == "hw_value", "Response have diff cookie in headers"
    print(response.cookies['HomeWork'])