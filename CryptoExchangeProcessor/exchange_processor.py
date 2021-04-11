from HTTPclient.binance_client import BinanceClient
from HTTPclient.client import HTTPClient
from abc import ABC, abstractmethod

class CryptoExchangeProcessor(ABC):

    @abstractmethod
    def __init__(self, client:HTTPClient):
        self.client = client

    @abstractmethod
    def get_server_time(self):
        pass

    @abstractmethod
    def show_candles(self):
        pass

    @abstractmethod
    def place_order(self):
        pass


