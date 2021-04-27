import hmac
from http_client.client import HTTPClient
import hmac
import hashlib
import base64
import json

class BitfinexClient(HTTPClient):

    def __init__(
        self,
        BASE_PATH: str = "https://api.bitfinex.com",
        apiKey: str = None,
        secretKey: str = None,
        suported_codes=None,
    ):
        self.secretKey = secretKey
        super().__init__(
            headers= {
                'Content-Type': 'application/json',
                'X-BFX-PAYLOAD': '',
                'X-BFX-APIKEY': apiKey,
                'X-BFX-SIGNATURE': ''
            },
            BASE_PATH=BASE_PATH,
            suported_codes=suported_codes
        )
    def get_signature(self, data):

        signature = hmac.new(
            self.secretKey.encode(), data, hashlib.sha384).hexdigest()
        return signature
        
    def update_headers(self, params):

        data = base64.b64encode(json.dumps(params).encode())
        self.args['headers']['X-BFX-SIGNATURE'] = self.get_signature(data=data)
        self.args['headers']['X-BFX-PAYLOAD'] = data
