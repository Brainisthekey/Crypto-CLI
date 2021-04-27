from decimal import Decimal
from enum import Enum
from typing import DefaultDict
import requests
import hmac
import hashlib
import time
from urllib.parse import urlencode
from exchange_processors.binance.binance_client import BinanceClient
from exchange_processors.main_client import CryptoExchangeProcessor
from collections import defaultdict



class BinanceExchangeProcessor(CryptoExchangeProcessor):

    timestamp = int(time.time() * 1000)
    path_to_candle = "/klines"
    path_to_order = "/order"
    path_to_account = "/account"

    def __init__(self, client: BinanceClient):
        self.client = client
        super().__init__(client)

    def get_signature(self, params):
        #Что то нужно придумать, ибо так обращаться к переменной
        #И для этого специально её инициализировать в BinanceClient такое себе
        signature = hmac.new(
            (self.client.secretKey).encode("utf-8"), 
            urlencode(params).encode("utf-8"), 
            hashlib.sha256).hexdigest()
        return signature

    def show_candles(
                self,
                symbol: str,
                interval = Enum,
                startTime=None,
                endTime=None,
                limit: int = None,
    ) -> requests.models.Response:

        params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": startTime,
            "endTime": endTime,
            "limit": limit,
        }
        return self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_candle, params=params
        )

    def place_order(
                self,
                symbol: str,
                side = None,
                type = None,
                timeInForce: Enum = None,
                quantity: Decimal = None,
                quoteOrderQty: Decimal = None,
                price: Decimal = None,
                newClientOrderId: str = None,
                stopPrice: Decimal = None,
                icebergQty: Decimal = None,
                newOrderRespType: Enum = None,
                recvWindow=None,
    ) -> requests.models.Response:

        data = {
            "symbol": symbol,
            "side": side,
            "type" : type,
           "timeInForce": timeInForce,
            "quantity": quantity,
            "price": price,
           "quoteOrderQty": quoteOrderQty,
           "newClientOrderId": newClientOrderId,
           "stopPrice": stopPrice,
           "icebergQty": icebergQty,
           "newOrderRespType": newOrderRespType,
           "recvWindow": recvWindow,
            "timestamp": self.timestamp,
        }
        data['signature'] = self.get_signature(params={key : val for (key, val) in data.items() if data[key] is not None})
        return self.client.request(
            type=self.client.RequestType.POST, path=self.path_to_order, data=data
        )

    def get_account(self) -> requests.models.Response:
    
        params = {"timestamp": self.timestamp}
        params['signature'] = self.get_signature(params)
        return self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_account, params=params
        )

api_key = '7wIVSwRr656l2K1bxt9JML7SBAt61Y1Vx96w8TULoicc3u0TczZz1SWXzHZUC467'
secret_key = '0F5qtVFgc4sbHwBa76ECgI54zEtXWXaUGyv5lvQ3wJReftzfgE5ymGTy88q5DCxa'

client = BinanceExchangeProcessor(client=BinanceClient(
                                                        apiKey=api_key,
                                                        secretKey=secret_key,
                                                        suported_code=[200, 400]
))
#print(client.get_account().json())
#print(client.place_order(symbol='BTCUSDT', side='SELL', type='MARKET', quantity='0.3').json())
#print(client.show_candles(symbol='BTCUSDT', interval='1h').json())