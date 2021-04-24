from HTTPclient.client import HTTPClient
import unittest
from unittest import mock
import pytest



clientt = HTTPClient(BASE_PATH='https://api.binance.com/api/v3/', suported_codes=[404])

@mock.patch('HTTPclient.client.requests.get')
def test_request(mock_request_get, type=HTTPClient.RequestType.GET, path='1'):
    mock_request_get.return_value = mock.Mock(**{'status_code' : 404, 'text.return_value' : "<html><body><h2>404 Not found</h2></body></html>"})
    assert clientt.request(type=type, path=path) == mock_request_get(type=type, path=path).text


