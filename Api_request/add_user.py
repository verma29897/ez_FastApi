import requests
import json

url = "http://192.168.1.9:8000/ops/users/"
headers = {
    "Content-Type": "application/json"
}
data = {
    "email": "test@example.com",
    "password": "securepassword",
    
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.text)
