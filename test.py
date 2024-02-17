import requests

BASE_URL = "http://127.0.0.1:8000/"
LOGIN_URL = "account/login/"

# GET/ account 
response = requests.get(f"{BASE_URL}{LOGIN_URL}")
# print(response.json()['message'])
# print(response.status_code)

# POST/ account
data = {
    "username" : "admin", 
    "password" : "admin"
}
response = requests.post(f"{BASE_URL}{LOGIN_URL}", data=data)
print(response.json()['message'])
print(response.status_code)


