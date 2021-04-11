from decimal import Decimal
from enum import Enum
import requests
from exchange_processor import CryptoExchangeProcessor
from HTTPclient.binance_client import BinanceClient

class BinanceExchangeProcessor(CryptoExchangeProcessor):

    def __init__(self, client=BinanceClient):
        super().__init__(client)
        self.path_to_time = '/time'
        self.path_to_candle = '/klines'
        self.path_to_order = '/order'
        self.client = client

    def get_server_time(self):
        args = self.client.args.update({'url': self.client.BASE_PATH + self.path_to_time})
        return self.client.request(type=self.client.RequestType.GET, path=args['url'], params=args['headers'])

    def show_candles(self, symbol: str, interval: Enum, startTime = None,
                     endTime = None, limit: int = None) -> requests.models.Response:

        params = {
            'symbol' : symbol,
            'interval' : Enum,
            'startTime' : startTime,
            'endTime' : endTime,
            'limit' : limit
        }
        params.update({'headers' : self.client.args['headers']})
        self.args = self.client.args.update({'url': self.client.BASE_PATH + self.path_to_candle})
        return self.client.request(type=self.client.RequestType.GET, path=self.args['url'], params=params)

    def place_order(self, symbol: str, side:Enum, type:Enum, timeInForce:Enum = None, quantity:Decimal = None,
                    quoteOrderQty:Decimal = None, price:Decimal = None, newClientOrderId: str = None,
                    stopPrice:Decimal = None, icebergQty:Decimal = None, newOrderRespType:Enum = None,
                    recvWindow = None, timestamp = None) -> requests.models.Response:
        params = {

        }
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
        params['headers'] = self.client.args['headers']
        args = self.client.args.update({'url': self.client.BASE_PATH + self.path_to_order})
        return self.client.request(type=self.client.RequestType.POST,
                                   path=args['url'],
                                   params=params,
                                   body=body)