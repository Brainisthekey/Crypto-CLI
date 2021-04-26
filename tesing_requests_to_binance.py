import hmac
import hashlib
import time
from urllib.parse import urlencode
import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.environ.get('API_KEY')
secretKey = os.environ.get('SECRET_KEY')

request_url = "https://api.binance.com/api/v3/myTrades?"

timestamp = int(time.time() * 1000)
print(timestamp)

querystring = urlencode({"timestamp": timestamp, "symbol": "BTCUSDT"})
print(querystring)

signature = hmac.new(
    secretKey.encode("utf-8"), querystring.encode("utf-8"), hashlib.sha256
).hexdigest()
print(signature)

request_url += querystring + "&signature=" + signature

response = requests.get(request_url, headers={"X-MBX-APIKEY": apiKey})
print(r.json()[5])
