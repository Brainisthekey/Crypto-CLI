from decimal import Decimal
from enum import Enum
import requests
from exchange_processor import CryptoExchangeProcessor
from HTTPclient.binance_client import BinanceClient

class BinanceExchangeProcessor(CryptoExchangeProcessor):
    path_to_time = '/time'
    path_to_candle = '/klines'
    path_to_order = '/order'

    def __init__(self, client=BinanceClient):
        super().__init__(client)


    def get_server_time(self):
        return self.client.request(type=self.client.RequestType.GET, path=self.path_to_time)

    def show_candles(self, symbol: str, interval: Enum, startTime = None,
                     endTime = None, limit: int = None) -> requests.models.Response:

        params = {
            'symbol' : symbol,
            'interval' : Enum,
            'startTime' : startTime,
            'endTime' : endTime,
            'limit' : limit
        }
        return self.client.request(type=self.client.RequestType.GET, path=self.path_to_candle, params=params)

    def place_order(self, symbol: str, side:Enum, type:Enum, timeInForce:Enum = None, quantity:Decimal = None,
                    quoteOrderQty:Decimal = None, price:Decimal = None, newClientOrderId: str = None,
                    stopPrice:Decimal = None, icebergQty:Decimal = None, newOrderRespType:Enum = None,
                    recvWindow = None, timestamp = None) -> requests.models.Response:

        body = {
            'symbol': symbol,
            'Enum': side,
            'timeInForce': timeInForce,
            'quantity': quantity,
            'quoteOrderQty': quoteOrderQty,
            'price': price,
            'newClientOrderId': newClientOrderId,
            'stopPrice': stopPrice,
            'icebergQty': icebergQty,
            'newOrderRespType': newOrderRespType,
            'recvWindow': recvWindow,
            'timestamp': timestamp,
        }

        return self.client.request(type=self.client.RequestType.POST,
                                   path=self.path_to_order,
                                   body=body)