import requests
import pytest

class TestFirstAPI:

    names = [
        ("Vitalik"),
        ("Arseniy"),
        ("Konstantin"),
        ("Valera Zhmishenko"),
        ("")
    ]


    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {"name": name}
        response = requests.get(url=url, params=data)

        assert response.status_code == 200, "WRONG RESPONSE CODE"

        response_dict = response.json()

        assert 'answer' in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = 'Hello, someone'
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict.get('answer')

        assert expected_response_text == actual_response_text, "Actual text in the response is not correct"