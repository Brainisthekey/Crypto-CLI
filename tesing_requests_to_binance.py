import hmac
import hashlib
import time
from urllib.parse import urlencode
import requests
import os
from dotenv import load_dotenv

#https://stackoverflow.com/questions/48592450/binance-api-call-with-sha56-and-python-requests/48592499#48592499?newreg=07b8cc778fbe4674a093b1cc7e2b4838

load_dotenv()

apiKey = os.environ.get('API_KEY')
secretKey = os.environ.get('SECRET_KEY')

# request_url = "https://api.binance.com/api/v3/myTrades?"

# timestamp = int(time.time() * 1000)
# print(timestamp)

# querystring = urlencode({"timestamp": timestamp, "symbol": "BTCUSDT"})
# print(querystring)

# signature = hmac.new(
#     secretKey.encode("utf-8"), querystring.encode("utf-8"), hashlib.sha256
# ).hexdigest()
# print(signature)

# request_url += querystring + "&signature=" + signature

# r = requests.get(request_url, headers={"X-MBX-APIKEY": apiKey})
# print(r.json()[30])

request_url = "https://api.binance.com/api/v3/myTrades"

timestamp = int(time.time() * 1000)
print(timestamp)

params = {"timestamp": timestamp, "symbol": "BTCUSDT"}

signature = hmac.new(
    secretKey.encode("utf-8"), urlencode(params).encode("utf-8"), hashlib.sha256
).hexdigest()
print(signature)

params['signature'] = signature

r = requests.get(request_url, headers={"X-MBX-APIKEY": apiKey}, params=params)
print(r.json()[3])