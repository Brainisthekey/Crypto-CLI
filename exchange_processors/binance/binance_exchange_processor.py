from decimal import Decimal
from enum import Enum
import requests
import hmac
import hashlib
import time
from urllib.parse import urlencode
from exchange_processors.binance.binance_client import BinanceClient
from exchange_processors.main_client import CryptoExchangeProcessor

timestamp = int(time.time() * 1000)

class BinanceExchangeProcessor(CryptoExchangeProcessor):

    path_to_time = "/time"
    path_to_candle = "/klines"
    path_to_order = "/order"
    path_to_account = "/account"

    def __init__(self, client: BinanceClient):
        self.client = client
        super().__init__(client)

    def get_signature(self, params):

        signature = hmac.new(
            (self.client.secretKey).encode("utf-8"), 
            urlencode(params).encode("utf-8"), 
            hashlib.sha256
        ).hexdigest()
        return signature

    def get_server_time(self):
        return self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_time
        )

    def show_candles(
        self,
        symbol: str,
        interval: Enum,
        startTime=None,
        endTime=None,
        limit: int = None,
    ) -> requests.models.Response:

        params = {
            "symbol": symbol,
            "interval": Enum,
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
        recvWindow=None,
        timestamp=None,
    ) -> requests.models.Response:

        body = {
            "symbol": symbol,
            "Enum": side,
            "timeInForce": timeInForce,
            "quantity": quantity,
            "quoteOrderQty": quoteOrderQty,
            "price": price,
            "newClientOrderId": newClientOrderId,
            "stopPrice": stopPrice,
            "icebergQty": icebergQty,
            "newOrderRespType": newOrderRespType,
            "recvWindow": recvWindow,
            "timestamp": timestamp,
        }

        return self.client.request(
            type=self.client.RequestType.POST, path=self.path_to_order, body=body
        )

    def get_account(
        self,
        timestamp,
        recvWindow=None
    )-> requests.models.Response:
    
        params = {"timestamp": timestamp}
        params['signature'] = self.get_signature(params)
        return self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_account, params=params
        )

api_key = '7wIVSwRr656l2K1bxt9JML7SBAt61Y1Vx96w8TULoicc3u0TczZz1SWXzHZUC467'
secret_key = '0F5qtVFgc4sbHwBa76ECgI54zEtXWXaUGyv5lvQ3wJReftzfgE5ymGTy88q5DCxa'

clientt = BinanceExchangeProcessor(client=BinanceClient(
                                                        apiKey=api_key,
                                                        secretKey=secret_key,
                                                        suported_code=[200]
))
print(clientt.get_account(timestamp=timestamp).json())