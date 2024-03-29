from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.BaseCase import BaseCase


class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        register_data = self.prepare_registration_data()
        # response_1 = requests.post(url='https://playground.learnqa.ru/api/user', data=register_data)
        response_1 = MyRequests.post(url='/user', data=register_data)

        Assertions.assert_code_status(response_1, 200)
        Assertions.assert_json_has_key(response_1, 'id')

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response_1, 'id')

        # #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        # response_2 = requests.post(url='https://playground.learnqa.ru/api/user/login', data=login_data)
        response_2 = MyRequests.post(url='/user/login', data=login_data)

        auth_sid = self.get_cookie(response_2, 'auth_sid')
        token = self.get_header(response_2, 'x-csrf-token')

        # EDIT
        new_name = 'Changed_name'

        # response_3 = requests.put(url=f'https://playground.learnqa.ru/api/user/{user_id}',
        #                           headers={'x-csrf-token': token},
        #                           cookies={'auth_sid': auth_sid},
        #                           data={'firstName': new_name})
        response_3 = MyRequests.put(url=f'/user/{user_id}',
                                    headers={'x-csrf-token': token},
                                    cookies={'auth_sid': auth_sid},
                                    data={'firstName': new_name})

        Assertions.assert_code_status(response_3, 200)

        # GET

        # response_4 = requests.get(url=f'https://playground.learnqa.ru/api/user/{user_id}',
        #                           headers={'x-csrf-token': token},
        #                           cookies={'auth_sid': auth_sid})
        response_4 = MyRequests.get(url=f'/user/{user_id}',
                                    headers={'x-csrf-token': token},
                                    cookies={'auth_sid': auth_sid})
        Assertions.assert_json_value_by_name(response_4, 'firstName', new_name, 'Wrong name of the user after edit')
