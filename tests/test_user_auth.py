import pytest
import requests
from lib.assertions import Assertions
from lib.BaseCase import BaseCase
from lib.my_requests import MyRequests


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self):
        data = {
            "email": "vinkotov@example.com",
            "password": '1234'
        }

        # url = 'https://playground.learnqa.ru/api/user/login'
        # response_auth = requests.post(url=url, data=data)
        response_auth = MyRequests.post(url="/user/login", data=data)
        self.auth_sid = self.get_cookie(response_auth, 'auth_sid')
        self.token = self.get_header(response_auth, 'x-csrf-token')
        self.user_id = self.get_json_value(response_auth, 'user_id')

    def test_auth_user(self):

        # response = requests.get(url='https://playground.learnqa.ru/api/user/auth',
        #                         headers={'x-csrf-token': self.token},
        #                         cookies={'auth_sid': self.auth_sid})

        response = MyRequests.get(
            url="/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            2,
            "User id from auth method is not equal to user id from check method")

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == 'no_cookie':
            # response = requests.get(url='https://playground.learnqa.ru/api/user/auth',
            #                         headers={'x-csrf-token': self.token})
            response = MyRequests.get(url='/user/auth', headers={'x-csrf-token': self.token})
        else:
            # response = requests.get(url='https://playground.learnqa.ru/api/user/auth',
            #                         cookies={'auth_sid': self.auth_sid})
            response = MyRequests.get(url='/user/auth',
                                    cookies={'auth_sid': self.auth_sid})
        Assertions.assert_json_value_by_name(
            response,
            'user_id',
            0,
            f"User is authorize with condition {condition}"
        )
