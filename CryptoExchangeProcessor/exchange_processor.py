from HTTPclient.binance_client import BinanceClient
from HTTPclient.client import HTTPClient
from abc import ABC, abstractmethod

class CryptoExchangeProcessor(ABC):

    def __init__(self, symbol: str, price:float):
        #In main diagram client use HTTPclient
        #But i think logicaly user BinanceClient() but rename it
        self.client = BinanceClient()
        self.symbol = symbol
        self.price = price

    @abstractmethod
    def GetServerTime(self):
        pass

    @abstractmethod
    def ShowCandles(self):
        pass

    @abstractmethod
    def PlaceOrder(self):
        pass

class BinanceExchangeProcessor(CryptoExchangeProcessor):

    def __init(self):
        client = BinanceClient()

    def GetServerTime(self):
        HTTPClient.request()

    def ShowCandles(self):
        pass

    def PlaceOrder(self):
        pass

class BittrexExchangeProcessor(CryptoExchangeProcessor):

    def GetServerTime(self):
        pass

    def ShowCandles(self):
        pass

    def PlaceOrder(self):
        pass

