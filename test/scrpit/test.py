import requests
import json

data = {'username': 'blues', 'password': '123456'}
r = requests.post('http://127.0.0.1:5000/login', data=json.dumps(data),
                  headers={'Content-Type': 'application/json'})
token = r.json()['access_token']
headers = {'Authorization': 'jwt ' + token}


data = {'name':'root','permissions':'1'}
r = requests.post('http://127.0.0.1:5000/roles',data=data,headers=headers)
print(r.status_code)
print(r.json())

# r = requests.get('http://127.0.0.1:5000/roles',data=data,headers=headers)
# print(r.status_code)
# print(r.json())

r = requests.delete('http://127.0.0.1:5000/role/4',data=data,headers=headers)
print(r.status_code)
print(r.json())


