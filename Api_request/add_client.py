'''
curl -X 'POST' \
  'http://192.168.1.9:8000/client/client_signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "prajjwalpandey641@gmail.com",
  "password": "Hello12345"
}'

'''

import requests
import json

url = "http://192.168.1.9:8000/client/client_signup"
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
