import pytest
import requests

user_agents = [
    'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) '
    'Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 '
    'Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
    'Safari/537.36 Edg/91.0.100.0',
    'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 '
    'Mobile/15E148 Safari/604.1'
]

@pytest.mark.parametrize('agent', user_agents)
@pytest.mark.xfail
def test_user_agent_method_api(agent):
    response = requests.get(
        url='https://playground.learnqa.ru/ajax/api/user_agent_check',
        headers={"User-Agent": agent}
    )
    platforms = ['Mobile', 'Web', 'Googlebot']
    browsers = ['Chrome', 'No', 'Unknown']
    devices = ['iOS', 'No', 'iPhone','Android', 'Unknown']
    assert response.status_code == 200, 'Response have incorrect status code'
    assert response.json(), 'Response dont have body JSON'
    assert response.json()['platform'] in platforms, 'In response platform value not in platforms list'
    assert response.json()['browser'] in browsers, 'In response JSON browser value not in browsers list'
    assert response.json()['device'] in devices, 'In response JSON device value not in devices list'