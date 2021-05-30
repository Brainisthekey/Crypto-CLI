import unittest
from unittest import mock
from exchange_processors.main_client import CryptoExchangeProcessor
from http_client.client import HTTPClient


class CryptoExchangeProcessorTest(unittest.TestCase):

    @mock.patch('exchange_processors.main_client.CryptoExchangeProcessor.__abstractmethods__', set())
    def test_client(self):
        exchange_processor = CryptoExchangeProcessor(client=HTTPClient())
        self.assertTrue(exchange_processor.get_account())


