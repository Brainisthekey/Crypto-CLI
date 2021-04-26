from http_client.client import HTTPClient


class BinanceClient(HTTPClient):
    def __init__(
        self,
        apiKey: str = None,
        secretKey: str = None,
        BASE_PATH: str = "https://api.binance.com/api/v3/",
    ):

        super().__init__(
            headers={"apiKey": apiKey, "secretKey": secretKey}, BASE_PATH=BASE_PATH
        )
