from decimal import Decimal
from enum import Enum
import requests
import hmac
import hashlib
import time
import json
import base64
from urllib.parse import urlencode
from exchange_processors.bitfinex.bitfinex_client import BitfinexClient
from exchange_processors.main_client import CryptoExchangeProcessor



class BitfinexExchangeProcessor(CryptoExchangeProcessor):

    nonce = str(int(round(time.time() * 10000)))
    path_to_info = '/v1/account_infos'
    path_to_ticker = '/v1/pubticker'
    path_to_order = '/v1/order/new'

    def __init__(self, client: BitfinexClient):
        self.client = client
        super().__init__(client)

    def get_signature(self, data):

        signature = hmac.new(
            self.client.secretKey.encode(), data, hashlib.sha384).hexdigest()
        return signature
    
    def update_headers(self, params):

        data = base64.b64encode(json.dumps(params).encode())
        self.client.args['headers']['X-BFX-SIGNATURE'] = self.get_signature(data=data)
        self.client.args['headers']['X-BFX-PAYLOAD'] = data

    def get_account(self):

        params = {
                'nonce' : self.nonce,
                'request' : self.path_to_info
        }
        self.update_headers(params=params)
        return self.client.request(
                                type=self.client.RequestType.POST, 
                                path=self.path_to_info
        )
    def show_candles(self, symbol):

        return self.client.request(
                                type=self.client.RequestType.GET, 
                                path=self.path_to_ticker + f'/{symbol}',
        )
    
    def place_order(
                self,
                symbol: str,
                side: str,
                amount: float,
                price: float,
                type
    ):
        params = {
                'nonce' : self.nonce,
                'request' : self.path_to_order,
                'symbol' : symbol,
                'side' : side,
                'amount' : amount,
                #'amount' : str(amount),
                'type' : type,
                'price' : price
                #'price' : str(price)
        }
        self.update_headers(params=params)
        return self.client.request(
                                type=self.client.RequestType.POST, 
                                path=self.path_to_order,
        )
api_key = '9VJLKBW3ubIksjd96zdYPBeNV46kTuY9O6cjVzVtoLy'
api_secret = 'L7yiqJjO3d5J1iRqxb6hY8FVHyKR3BrhfAKka2CFE3W'

client = BitfinexExchangeProcessor(client=BitfinexClient(
                                                        apiKey=api_key,
                                                        secretKey=api_secret,
                                                        suported_codes=[200, 400])
)
#print(client.get_account().text)
#print(client.show_candles(symbol='btcusd').text)
#print(client.place_order(symbol='btcusd', side='buy', amount='0.3', price='1000', type='market').text)
