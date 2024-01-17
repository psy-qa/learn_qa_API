from lib.my_requests import MyRequests
from lib.BaseCase import BaseCase
from lib.assertions import Assertions


# id  = b'{"id":"89689"}'

class TestUserRegister(BaseCase):

    def test_create_user_succefuly(self):
        data = self.prepare_registration_data()
        # response = requests.post(url='https://playground.learnqa.ru/api/user', data=data)
        response = MyRequests.post(url='/user', data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')


    def test_create_user_with_existing_email(self):
        email = 'qqq123test@mail.ru'
        data = self.prepare_registration_data(email)
        # response = requests.post(url='https://playground.learnqa.ru/api/user', data=data)
        response = MyRequests.post(url='/user', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'UTF-8') == f"Users with email '{email}' already exists", f'Unexpected responce content {response.content}'
