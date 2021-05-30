import unittest
from decimal import Decimal
from unittest import mock
from exchange_processors.binance.binance_exchange_processor import BinanceExchangeProcessor
from exchange_processors.binance.binance_client import BinanceClient
from tests.data import json_get_account_200,json_get_account_400, json_get_account_401, json_get_candles, json_place_order


class BinanceExchProcessorTest(unittest.TestCase):

    @mock.patch('time.time')
    def test_binance_exchange_processor(self, mock_time):
        mock_time.return_value = '0'
        client_binance = BinanceExchangeProcessor(client=BinanceClient(
            apiKey='test_api_key',
            secretKey='test_secret_key',
            suported_codes=[200, 400]
        ))
        assert hasattr(client_binance, 'path_to_candle') == True
        assert hasattr(client_binance, 'path_to_order') == True
        assert hasattr(client_binance, 'path_to_account') == True
        assert client_binance.__getattribute__('timestamp') == 0
        # Question there

    @mock.patch('http_client.client.HTTPClient.request')
    @mock.patch('exchange_processors.binance.binance_client.BinanceClient.get_signature')
    @mock.patch('time.time')
    def test_binance_get_account(self, mock_time, mock_signature, mock_request):
        mock_time.return_value = '0'
        mock_signature.return_value = '3f9168044ce99b6e1e6544c7e148626a4454b54a67675b8bf14e684916a57ee7'
        client_binance = BinanceExchangeProcessor(client=BinanceClient(
            apiKey='test_api_key',
            secretKey='test_secret_key',
            suported_codes=[200, 400, 401]
        ))
        assert client_binance.__getattribute__('timestamp') == 0
        mock_response = mock.Mock(
            **{'status_code': 200,
               'json.return_value': json_get_account_200
               }
        )
        mock_request.return_value = mock_response
        assert client_binance.get_account().json() == json_get_account_200
        mock_response = mock.Mock(
            **{'status_code': 400,
               'json.return_value': json_get_account_400
               }
        )
        mock_request.return_value = mock_response
        assert client_binance.get_account().json() == json_get_account_400
        mock_response = mock.Mock(
            **{'status_code': 401,
               'json.return_value': json_get_account_401
               }
        )
        mock_request.return_value = mock_response
        assert client_binance.get_account().json() == json_get_account_401


    @mock.patch('http_client.client.HTTPClient.request')
    def test_show_candles(self, mock_request):
        return_value = {'symbol': 'BTCUSDT', 'price': '35734.9'}
        symbol = 'BTCUSDT'
        interval = '1h'
        client_binance = BinanceExchangeProcessor(client=BinanceClient(
            apiKey='test_api_key',
            secretKey='test_secret_key',
            suported_codes=[200, 400]
        ))
        mock_response = mock.Mock(
            **{'status_code': 200,
               'json.return_value': json_get_candles,
               }
        )
        mock_request.return_value = mock_response
        assert client_binance.show_candles(symbol=symbol, interval=interval).__dict__ == return_value


    @mock.patch('time.time')
    @mock.patch('http_client.client.HTTPClient.request')
    @mock.patch('exchange_processors.binance.binance_client.BinanceClient.get_signature')
    def test_place_order(self, mock_get_signature, mock_request, mock_time):
        signature_return_value = 'a06452c5cfb3360c6f23291df33024bd6eaec7618ac2343a1b3b3a31ebe17f90'
        mock_time.return_value = '0'
        mock_get_signature.return_value = signature_return_value
        symbol = 'BTCUSDT'
        side = 'SELL'
        type = 'MARKET'
        quantity = Decimal('0.3')
        client_binance = BinanceExchangeProcessor(client=BinanceClient(
            apiKey='test_api_key',
            secretKey='test_secret_key',
            suported_codes=[200, 400]
        ))
        mock_response = mock.Mock(
            **{'status_code': 400, 'json.return_value': json_place_order}
        )
        mock_request.return_value = mock_response
        assert client_binance.place_order(
            symbol=symbol,
            side=side,
            type=type,
            quantity=quantity
        ).json() == json_place_order
