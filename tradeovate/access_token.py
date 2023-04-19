import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://demo.tradovateapi.com/v1/auth/accesstokenrequest"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "name": os.environ["TRADOVATE_NAME"],
    "password": os.environ["TRADOVATE_PASSWORD"],
    "appId": "Sample App",
    "appVersion": "1.0",
    "cid": 8,
    "deviceId": "123e4567-e89b-12d3-a456-426614174000",
    "sec": "f03741b6-f634-48d6-9308-c8fb871150c2"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(data)
if response.status_code == 200:
    response_json = response.json()
    print(json.dumps(response_json, indent=2))
else:
    print(f"Request failed with status code {response.status_code}")
