import requests
import unittest
import json


class TestAuth(unittest.TestCase):

    def test_register2(self):
        data = {'username':'blues','password':'123456'}
        r = requests.post('http://127.0.0.1:5000/users',data=data)
        self.assertEqual(r.status_code,499)

    def test_register3(self):
        data = {'password':'123456'}
        r = requests.post('http://127.0.0.1:5000/users',data=data)
        self.assertEqual(r.status_code,499)

    def test_register4(self):
        data = {'username':'blues'}
        r = requests.post('http://127.0.0.1:5000/users',data=data)
        self.assertEqual(r.status_code,499)

    def test_login(self):
        data = {'username': 'blues', 'password': '123456'}
        r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                          headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code,200,'登陆失败')

    def test_login2(self):
        data = {'username': 'blues', 'password': '1234567'}
        r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                          headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code,403,'登陆失败失败')

    def test_login3(self):
        data = {'username': 'x', 'password': '123456'}
        r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                          headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code,403,'登陆失败失败')

    def test_login4(self):
        data = {'password': '123456'}
        r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                          headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code,401,'登陆失败失败')

    def test_login5(self):
        data = {'username': 'x'}
        r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                          headers={'Content-Type': 'application/json'})
        self.assertEqual(r.status_code,401,'登陆失败失败')

    def test_get_user(self):
        data = {'username': 'blues', 'password': '123456'}
        r = requests.post('http://127.0.0.1:5000/login',data=json.dumps(data),headers={'Content-Type':'application/json'})
        self.assertEqual(r.status_code, 200, '登陆失败')
        token = r.json()['access_token']
        headers = {'Authorization':'jwt '+token}
        r = requests.get('http://127.0.0.1:5000/user', headers=headers)
        self.assertEqual(r.status_code, 201, '获取个人信息失败')

    def test_get_user2(self):
        r = requests.get('http://127.0.0.1:5000/user')
        self.assertEqual(r.status_code, 401, '获取个人信息失败')