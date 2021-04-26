from decimal import Decimal
from enum import Enum
from abc import ABC, abstractmethod
from http_client.client import HTTPClient


class CryptoExchangeProcessor(ABC):
    @abstractmethod
    def __init__(self, client: HTTPClient):
        self.client = client

    @abstractmethod
    def get_server_time(self):
        pass

    @abstractmethod
    def show_candles(
        self,
        symbol: str,
        interval: Enum,
        startTime=None,
        endTime=None,
        limit: int = None,
    ):
        pass

    @abstractmethod
    def place_order(
        self,
        symbol: str,
        side: Enum,
        type: Enum,
        timeInForce: Enum = None,
        quantity: Decimal = None,
        quoteOrderQty: Decimal = None,
        price: Decimal = None,
        newClientOrderId: str = None,
        stopPrice: Decimal = None,
        icebergQty: Decimal = None,
        newOrderRespType: Enum = None,
        recvWindow: int = None,
        timestamp: int = None,
    ):
        pass

    # What is the type LONG ?
    # How i can user Enum type?
    # In get server time we don't need a params
