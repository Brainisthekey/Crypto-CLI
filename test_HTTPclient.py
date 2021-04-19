
from enum import Enum
from HTTPclient.client import HTTPClient
import pytest
from unittest.mock import Mock, patch
from unittest import mock
from unittest import TestCase
import requests
# @pytest.fixture(scope='module')
# def init():

#     inciali_init = HTTPClient(headers = {'apiKey' : 'apiKey', 'secretKey' : 'secretKey'}, 
#                               suported_codes = [200, 404], 
#                               BASE_PATH = 'https://api.binance.com/api/v3/')
#     return inciali_init


# class HTTPClient_test(TestCase):

#     headers = 'headers'
#     args = {'headers' : headers}
#     suported_code = [200]
#     BASE_PATH = 'https://api.binance.com/api/v3/'
#     type = 'GET'
#     path = 'time'

#     @pytest.mark.parametrize('_type, _path, _params, _body',
#                             [
#                                 ('GET', 'time', {'params': 'params'}, {'body' : 'body'})
#                             ]
#                             )
#     @mock.patch('requests.get')
#     def test_request(type = _type, _path, _params, _body, mock_request):
#         init = HTTPClient(self.headers, self.suported_code, self.BASE_PATH)
#         if type == _type:
#             mock_response = Mock(name='mock response',
#                                 **{'status_code' : 200, 'json.return_value' : {"serverTime" : "1618816799512"}})
#             mock_request.return_value = mock_response
#             assert init.request(type=_type, path=path, params=params, body=body) == requests.models.Response



class Test1(TestCase):

    path = 'time'
    type = 'GET'
    params = {'params' : None}
    body = {'body' : None}
    args = {'headers': 'headers'}
    BASE_PATH = 'https://api.binance.com/api/v3/'
    
    @mock.patch('HTTPclient.client.requests')
    def test_request(self, path):
        client = HTTPClient('', '', '')
        client.handle_response = Mock()
        client.RequestType = Mock()
        client.RequestType.GET = Mock(return_value='GET')
        assert client.request(type=client.RequestType.GET, path=self.path, params=self.params, body=self.body) == requests.models.Response