import unittest
from unittest import mock
import abc
from exchange_processors.main_client import CryptoExchangeProcessor
from http_client.client import HTTPClient

class CryptoFake(CryptoExchangeProcessor):
    def __init__(self, client: HTTPClient):
        self.client = client
        super().__init__(client)

    def show_candles(self):
        pass

    def place_order(self):
        pass

    def get_account(self):
        pass


class CryptoExchangeProcessorTest(unittest.TestCase):

    @mock.patch.object(abc, 'ABC', autospec=True)
    @mock.patch.object(abc, 'abstractmethod', autospec=True)
    def test_client(self, mock_abstractmethod, mock_ABC):
        face_client = mock.Mock()
        cl = CryptoFake(face_client)




