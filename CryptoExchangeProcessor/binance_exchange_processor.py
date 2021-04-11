from exchange_processor import CryptoExchangeProcessor
from HTTPclient.binance_client import BinanceClient

class BinanceExchangeProcessor(CryptoExchangeProcessor):

    def __init__(self, client=BinanceClient):
        super().__init__(client)
        self.path_to_time = '/time'
        self.client = client

    def get_server_time(self):
        self.args = self.client.args.update({'url': self.client.BASE_PATH + self.path_to_time})
        return self.client.request(type=self.client.RequestType.GET,**self.args)


    def show_candles(self):
        pass

    def place_order(self):
        pass