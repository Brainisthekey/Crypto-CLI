from src.clients.http_client import HTTPClient
import hmac
from urllib.parse import urlencode
import hashlib

class BinanceClient(HTTPClient):
    def __init__(
        self,
        apiKey: str = None,
        secretKey: str = None,
        BASE_PATH: str = "https://api.binance.com/api/v3",
        suported_codes = None
    ):
        self.secretKey=secretKey
        super().__init__(
            headers={"X-MBX-APIKEY": apiKey}, 
            BASE_PATH=BASE_PATH,
            suported_codes=suported_codes
        )

    def get_signature(self, params):
        signature = hmac.new(
            self.secretKey.encode("utf-8"), 
            urlencode(params).encode("utf-8"), 
            hashlib.sha256).hexdigest()
        return signature