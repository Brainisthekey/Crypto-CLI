from enum import Enum

import requests

from exchange_processor import CryptoExchangeProcessor
from HTTPclient.binance_client import BinanceClient

class BinanceExchangeProcessor(CryptoExchangeProcessor):

    def __init__(self, client=BinanceClient):
        super().__init__(client)
        self.path_to_time = '/time'
        self.path_to_candle = '/klines'
        self.client = client

    def get_server_time(self):
        self.args = self.client.args.update({'url': self.client.BASE_PATH + self.path_to_time})
        return self.client.request(type=self.client.RequestType.GET,**self.args)

    def show_candles(self, symbol: str, interval: Enum, startTime = None,
                     endTime = None, limit: int = None) -> requests.models.Response:

        self.params = {
            'symbol' : symbol,
            'interval' : Enum,
            'startTime' : startTime,
            'endTime' : endTime,
            'limit' : limit
        }
        self.args = self.args = self.client.args.update({'url': self.client.BASE_PATH + self.path_to_candle})
        return self.client.request(type=self.client.RequestType.GET, **self.args, params=self.params)

    def place_order(self):
        pass