import requests


class TestFirstAPI:

    def test_hello_call(self):
        url = 'https://playground.learnqa.ru/api/hello'
        name = 'Valera Zhmishenko'
        data = {"name": name}
        response = requests.get(url=url, params=data)

        assert response.status_code == 200, "WRONG RESPONSE CODE"

        response_dict = response.json()

        assert 'answer' in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict.get('answer')

        assert expected_response_text == actual_response_text, "Actual text in the response is not correct"