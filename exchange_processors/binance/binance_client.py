from http_client.client import HTTPClient



class BinanceClient(HTTPClient):
    def __init__(
        self,
        apiKey: str = None,
        secretKey: str = None,
        BASE_PATH: str = "https://api.binance.com/api/v3",
        suported_code = None
    ):
        self.secretKey=secretKey
        super().__init__(
            headers={"X-MBX-APIKEY": apiKey}, 
            BASE_PATH=BASE_PATH,
            suported_codes=suported_code
        )