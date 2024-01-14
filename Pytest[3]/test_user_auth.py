import requests


class TestUserAuth:

    def test_auth_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": '1234'
        }
        url = 'https://playground.learnqa.ru/api/user/login'
        response_auth = requests.post(url=url, data=data)
        print(response_auth.text)
        assert "auth_sid" in response_auth.cookies, "There is no auth token in response"
        assert "x-csrf-token" in response_auth.headers, "There is no csrf token in response"
        assert "user_id" in response_auth.json(), "There is no user id in response"

        auth_sid = response_auth.cookies['auth_sid']
        token = response_auth.headers['x-csrf-token']
        user_id = response_auth.json()['user_id']

        response = requests.get(url= 'https://playground.learnqa.ru/api/user/auth',
                                headers={'x-csrf-token': token},
                                cookies={'auth_sid': auth_sid})

        assert 'user_id' in response.json(), 'There is no user id in the second response'
        user_id_from_check_method = response.json()['user_id']

        assert user_id_from_check_method == user_id, "User id from auth method is not equal to user id from check method"
