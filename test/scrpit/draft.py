import requests

BASE_URL = 'http://127.0.0.1:5000'

data = {'username': 'blues', 'password': '123456'}
r = requests.post(BASE_URL + '/login', json=data)
print(r.status_code)

token = r.json()['access_token']

headers = {'Authorization': 'jwt ' + token}
r = requests.get(BASE_URL + '/bullets', headers=headers)
print(r.status_code)
print(r.json())

# data = {'type': 1, 'content': 'test'}
# r = requests.post(BASE_URL + '/bullets', headers=headers, json=data)
# print(r.status_code)
# print(r.json())

data = {'content': 'update_test', 'timestamp': 2}
r = requests.patch(BASE_URL + '/bullet/7', headers=headers, json=data)
if r.status_code != 204:
    print(r.status_code)
    print(r.json())
else:
    print(r.status_code)
