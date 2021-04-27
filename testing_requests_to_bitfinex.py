import time
import json
import base64
import requests
import hashlib
import hmac
from requests import Response


api_key = '9VJLKBW3ubIksjd96zdYPBeNV46kTuY9O6cjVzVtoLy'
api_secret = 'L7yiqJjO3d5J1iRqxb6hY8FVHyKR3BrhfAKka2CFE3W'

url = 'https://api.bitfinex.com'
request = '/v1/balances'

params = {
    'nonce' : str(int(round(time.time() * 10000))),
    'request' : request
    }

data = base64.b64encode(json.dumps(params).encode())

sign = hmac.new(api_secret.encode(), data, hashlib.sha384).hexdigest()
print(sign)


headers = {
    'X-BFX-APIKEY' : api_key,
    'X-BFX-SIGNATURE': sign,
    'X-BFX-PAYLOAD' : data,
}

response = requests.post(url=url + request, headers=headers)

print(response.status_code)
print(response.text)

