from decimal import Decimal
from enum import Enum
from exchange_processors.models import ShowCandles
import requests
import time
from exchange_processors.binance.binance_client import BinanceClient
from exchange_processors.main_client import CryptoExchangeProcessor



class BinanceExchangeProcessor(CryptoExchangeProcessor):

    timestamp = int(time.time() * 1000)
    path_to_candle = "/klines"
    path_to_order = "/order"
    path_to_account = "/account"

    def __init__(self, client: BinanceClient):
        self.client = client
        super().__init__(client)

    def show_candles(
                self,
                symbol: str,
                interval = Enum,
                startTime=None,
                endTime=None,
                limit: int = None,
    ) -> ShowCandles:

        params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": startTime,
            "endTime": endTime,
            "limit": limit,
        }
        ticker = self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_candle, params=params
        )
        price = ticker.json()[-1][1]
        return ShowCandles(symbol=symbol, price=price)

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
        data['signature'] = self.client.get_signature(params={key : val for (key, val) in data.items() if data[key] is not None})
        return self.client.request(
            type=self.client.RequestType.POST, path=self.path_to_order, data=data
        )

    def get_account(self) -> requests.models.Response:
    
        params = {"timestamp": self.timestamp}
        params['signature'] = self.client.get_signature(params)
        return  self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_account, params=params
        )

api_key = ''
secret_key = ''

client = BinanceExchangeProcessor(client=BinanceClient(
                                                        apiKey=api_key,
                                                        secretKey=secret_key,
                                                        suported_code=[200, 400]
))
#print(client.get_account().json())
#print(client.place_order(symbol='BTCUSDT', side='SELL', type='MARKET', quantity='0.3').json())

#print(client.show_candles(symbol='BTCUSDT', interval='1h').json()[-1])
print(client.show_candles(symbol='BTCUSDT', interval='1h'))
