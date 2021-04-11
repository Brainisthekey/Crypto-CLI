from client import HTTPClient


class BinanceClient(HTTPClient):

    apiKey = ''
    secretKey = ''

    def __init__(self, apiKey: str = None, secretKey: str = None, BASE_PATH: str = 'https://api.binance.com'):
        super().__init__(headers= {
            'apiKey' : apiKey,
            'secretKey' : secretKey },
             BASE_PATH=BASE_PATH)
        self.apiKey = apiKey
        self.secretKey = secretKey