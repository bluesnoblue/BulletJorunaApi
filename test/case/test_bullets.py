import requests
import unittest


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global headers
        data = {'username': 'blues', 'password': '123456'}
        r = requests.post('http://127.0.0.1:5000/login', json=data)
        token = r.json()['access_token']
        headers = {'Authorization': 'jwt ' + token}

    def test1_get_bullets(self):
        r = requests.get('http://127.0.0.1:5000/bullets')
        self.assertEqual(r.status_code, 401)

        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        self.assertEqual(r.status_code, 200)

    def test2_post_bullets(self):
        r = requests.post('http://127.0.0.1:5000/bullets')
        self.assertEqual(r.status_code, 401)

        r = requests.post('http://127.0.0.1:5000/bullets', headers=headers)
        self.assertEqual(r.status_code, 499)

        data = {'type': 1, 'content': 'test'}
        r = requests.post('http://127.0.0.1:5000/bullets', headers=headers, json=data)
        self.assertEqual(r.status_code, 201)

        data = {'type': 1, 'content': 'test', 'timestamp': 2}
        r = requests.post('http://127.0.0.1:5000/bullets', headers=headers, json=data)
        self.assertEqual(r.status_code, 201)

        data = {'type': 2, 'content': 'test'}
        r = requests.post('http://127.0.0.1:5000/bullets', headers=headers, json=data)
        self.assertEqual(r.status_code, 201)

        data = {'type': 2, 'content': 'test', 'timestamp': 3}
        r = requests.post('http://127.0.0.1:5000/bullets', headers=headers, json=data)
        self.assertEqual(r.status_code, 201)

    def test_3_update_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets',headers=headers)
        bullets = r.json()['data']
        data = {'content': 'update_test', 'timestamp': 4}
        for bullet in bullets:
            r = requests.patch(f'http://127.0.0.1:5000/bullet/{bullet["id"]}', headers=headers, json=data)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.json()['content'], 'update_test')

    def test4_finish_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        bullets = r.json()['data']
        for bullet in bullets:
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/finish', headers=headers)
            self.assertEqual(r.status_code, 204)
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/finish', headers=headers)
            self.assertEqual(r.status_code, 499)
            self.assertEqual(r.json()['error'], 'bullet can not finish')

    def test5_reopen_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        bullets = r.json()['data']
        for bullet in bullets:
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/reopen', headers=headers)
            self.assertEqual(r.status_code, 204)
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/reopen', headers=headers)
            self.assertEqual(r.status_code, 499)
            self.assertEqual(r.json()['error'], 'bullet can not reopen')

    def test6_cancel_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        bullets = r.json()['data']
        for bullet in bullets:
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/cancel', headers=headers)
            self.assertEqual(r.status_code, 204)
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/cancel', headers=headers)
            self.assertEqual(r.status_code, 499)
            self.assertEqual(r.json()['error'], 'bullet can not cancel')

    def test7_reopen_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        bullets = r.json()['data']
        for bullet in bullets:
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/reopen', headers=headers)
            self.assertEqual(r.status_code, 204,msg=bullet['status'])
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/reopen', headers=headers)
            self.assertEqual(r.status_code, 499)
            self.assertEqual(r.json()['error'], 'bullet can not reopen')

    def test8_delay_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        bullets = r.json()['data']
        for bullet in bullets:
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/delay', headers=headers)
            self.assertEqual(r.status_code, 499)

            data = {'timestamp': bullet['time']+1}
            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/delay', headers=headers, json=data)
            self.assertEqual(r.status_code, 204)

            r = requests.post(f'http://127.0.0.1:5000/bullet/{bullet["id"]}/delay', headers=headers, json=data)
            self.assertEqual(r.status_code, 499)
            self.assertEqual(r.json()['error'], 'bullet can not delay')

    def test9_del_bullet(self):
        r = requests.get('http://127.0.0.1:5000/bullets', headers=headers)
        bullets = r.json()['data']
        for bullet in bullets:
            r = requests.delete(f'http://127.0.0.1:5000/bullet/{bullet["id"]}')
            self.assertEqual(r.status_code, 401)
            r = requests.delete(f'http://127.0.0.1:5000/bullet/{bullet["id"]}', headers=headers)
            self.assertEqual(r.status_code, 204)
            r = requests.delete(f'http://127.0.0.1:5000/bullet/{bullet["id"]}', headers=headers)
            self.assertEqual(r.status_code, 499)
