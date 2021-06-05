from src.exchange_processors.models import ShowCandles
import time
from src.clients.bitfinex_main_client.bitfinex_client import BitfinexClient
from src.exchange_processors.exchange_processor import CryptoExchangeProcessor




class BitfinexExchangeProcessor(CryptoExchangeProcessor):

    nonce = str(int(round(time.time() * 10000)))
    path_to_info = '/v1/balances'
    path_to_ticker = '/v1/pubticker'
    path_to_order = '/v1/order/new'

    def __init__(self, client: BitfinexClient):
        self.client = client
        super().__init__(client)

    def get_account(self):

        params = {
                'nonce' : self.nonce,
                'request' : self.path_to_info
        }
        self.client.update_headers(params=params)
        return self.client.request(
                                type=self.client.RequestType.POST, 
                                path=self.path_to_info
        )
    def show_candles(self,
                     symbol: str,
                     interval: str = None,
    ) -> ShowCandles:

        ticker = self.client.request(
                                type=self.client.RequestType.GET, 
                                path=self.path_to_ticker + f'/{symbol}',
        )
        price = ticker.json()['last_price']
        return ShowCandles(symbol=symbol.upper(), price=price)
    
    def place_order(
                self,
                symbol: str,
                side: str,
                type: str,
                quantity: str,
                price: str,
    ):
        params = {
                'nonce' : self.nonce,
                'request' : self.path_to_order,
                'symbol' : symbol,
                'side' : side,
                'amount' : quantity,
                'type' : type,
                'price' : price
        }
        self.client.update_headers(params=params)
        return self.client.request(
                            type=self.client.RequestType.POST,
                            path=self.path_to_order
        )


api_key = ''
api_secret = ''

client = BitfinexExchangeProcessor(client=BitfinexClient(
                                                        apiKey=api_key,
                                                        secretKey=api_secret,
                                                        suported_codes=[200, 400])
)
#print(client.get_account().text)
#print(client.show_candles(symbol='btcusd'))
#print(client.place_order(symbol='btcusd', side='buy', quantity='0.3', price='1000.0', type='market').text)