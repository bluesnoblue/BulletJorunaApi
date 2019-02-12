import requests

data = {'username':'blues','password':'123456'}
r = requests.post('http://127.0.0.1:5000/users',data=data)
print(r.status_code)
print(r.json())