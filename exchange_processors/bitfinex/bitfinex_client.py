from http_client.client import HTTPClient

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
