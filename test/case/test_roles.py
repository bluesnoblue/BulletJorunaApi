import requests
import unittest
import json

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global headers
        data = {'username': 'blues', 'password': '123456'}
        r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                          headers={'Content-Type': 'application/json'})
        token = r.json()['access_token']
        headers = {'Authorization': 'jwt ' + token}

    def test_get_roles(self):
        r = requests.get('http://127.0.0.1:5000/roles', headers=headers)
        self.assertEqual(r.status_code,200)

    # def test_post_roles(self):
    #     r = requests.post('http://127.0.0.1:5000/roles', headers=headers)
    #     self.assertEqual(r.status_code, 200)

    # def test_get_role(self):
    #     r = requests.get('http://127.0.0.1:5000/role/1', headers=headers)
    #     self.assertEqual(r.status_code, 200)

    # def test_del_role(self):
    #     r = requests.delete('http://127.0.0.1:5000/role/1', headers=headers)
    #     self.assertEqual(r.status_code, 200)

