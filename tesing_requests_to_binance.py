import hmac
import hashlib
import time
from urllib.parse import urlencode
import requests

api_key = ""
api_secret = ""

request_url = "https://api.binance.com/api/v3/myTrades?"

timestamp = int(time.time() * 1000)
print(timestamp)

querystring = urlencode({"timestamp": timestamp, "symbol": "BTCUSDT"})
print(querystring)

signature = hmac.new(
    api_secret.encode("utf-8"), querystring.encode("utf-8"), hashlib.sha256
).hexdigest()
print(signature)

request_url += querystring + "&signature=" + signature

r = requests.get(request_url, headers={"X-MBX-APIKEY": api_key})
print(r.json()[30])
