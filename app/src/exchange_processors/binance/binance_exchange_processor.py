from decimal import Decimal
from enum import Enum
from src.exchange_processors.models import GetAccount, ShowCandles
import requests
import time
from src.clients.binance_main_client.binance_client import BinanceClient
from src.exchange_processors.exchange_processor import CryptoExchangeProcessor


class BinanceExchangeProcessor(CryptoExchangeProcessor):

    path_to_candle = "/klines"
    path_to_order = "/order"
    path_to_account = "/account"

    def __init__(self, client: BinanceClient):
        self.client = client
        self.timestamp = int(time.time() * 1000)
        super().__init__(client)

    def show_candles(
                self,
                symbol: str,
                interval = Enum
    ) -> ShowCandles:

        params = {
            "symbol": symbol,
            "interval": interval,
        }
        ticker = self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_candle, params=params
        )
        price = ticker.json()[-1][1]
        return ShowCandles(symbol=symbol, price=round(float(price), 1))

    def place_order(
                self,
                symbol: str,
                side = None,
                type = None,
                quantity: Decimal = None,
                price: Decimal = None,
    ) -> requests.models.Response:

        data = {
            "symbol": symbol,
            "side": side,
            "type" : type,
            "quantity": quantity,
            "price": price,
            "timestamp": self.timestamp,
        }
        data['signature'] = self.client.get_signature(params={key : val for (key, val) in data.items() if data[key] is not None})
        return self.client.request(
            type=self.client.RequestType.POST, path=self.path_to_order, data=data
        )

    def get_account(self) -> GetAccount:
        balances_binance = {}
        params = {"timestamp": self.timestamp}
        params['signature'] = self.client.get_signature(params)
        get_account_response_json = self.client.request(
            type=self.client.RequestType.GET, path=self.path_to_account, params=params
        ).json()
        for balances in get_account_response_json['balances']:
            for key, val in balances.items():
                zero_values = ('0.00000000','0.00')
                if key == 'free' and val not in zero_values:
                    balances_binance[balances['asset']] = balances['free']
        return GetAccount(balances = balances_binance) 

api_key = ''
secret_key = ''

client = BinanceExchangeProcessor(client=BinanceClient(
                                                        apiKey=api_key,
                                                        secretKey=secret_key,
                                                        suported_codes=[200, 400, 401]
))

#print(client.get_account())
#print(client.place_order(symbol='BTCUSDT', side='SELL', type='MARKET', quantity=Decimal('0.3')).json())
#print(client.show_candles(symbol='BTCUSDT', interval='1h').dict())
