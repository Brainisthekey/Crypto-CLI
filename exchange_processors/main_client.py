from decimal import Decimal
from enum import Enum
from abc import ABC, abstractmethod
from http_client.client import HTTPClient
from exchange_processors.models import ShowCandles


class CryptoExchangeProcessor(ABC):
    @abstractmethod
    def __init__(self, client: HTTPClient):
        self.client = client

    @abstractmethod
    def show_candles(
                self,
                symbol: str,
                interval: str = None,
    ) -> ShowCandles:
        pass

    @abstractmethod
    def place_order(
                self,
                symbol: str,
                side: str,
                type: str,
                quantity: float,
                price: float,
    ):
        pass
    @abstractmethod
    def get_account(
                self,
                timestamp=None,
                recvWindow=None,
    ):
        pass
