import unittest
from unittest import mock
from exchange_processors.binance.binance_exchange_processor import BinanceExchangeProcessor
from exchange_processors.binance.binance_client import BinanceClient


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
        #Question there

