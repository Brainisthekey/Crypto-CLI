from unittest import mock

from exchange_processors.bitfinex.bitfinex_client import BitfinexClient

def test_bitfinex_client():

    client = BitfinexClient(
                    BASE_PATH='test_base_patch',
                    apiKey='test_apiKey',
                    secretKey='test_secretKey',
                    suported_codes=[777]
    )
    assert client.__getattribute__('BASE_PATH') == 'test_base_patch'
    assert client.__getattribute__('secretKey') == 'test_secretKey'
    assert client.__getattribute__('suported_codes') == [777]
    assert client.__getattribute__('headers') == {
                                                    'Content-Type': 'application/json',
                                                    'X-BFX-PAYLOAD': '',
                                                    'X-BFX-APIKEY': 'test_apiKey',
                                                    'X-BFX-SIGNATURE': ''
    }

def test_get_signature():
    client = BitfinexClient(
                BASE_PATH='test_base_patch',
                apiKey='test_apiKey',
                secretKey='test_secretKey',
                suported_codes=[777]
    )
    return_value_signature = '07a3295f786c77fb782f1e89d2f1ee86abdff6a37cb7b4f49bd7c30d1697257746ad405f9118ea2d29fd86dc5e40a358'
    data = b'InRlc3Rfc2lnbmF0dXJlIg=='
    assert client.get_signature(data) == return_value_signature

@mock.patch('exchange_processors.bitfinex.bitfinex_client.BitfinexClient.get_signature')
def test_update_headers(mock_signature):
    client = BitfinexClient(
            BASE_PATH='test_base_patch',
            apiKey='test_apiKey',
            secretKey='test_secretKey',
            suported_codes=[777]
    )
    mock_signature.return_value = '060812e040090120d068ca10e3004196f10c8569c010ae44ea4542d22145eddfbd51d2c40c4c0bc534b02e5d86427b54'
    client.update_headers(params='test_params')
    assert client.headers == {
        'Content-Type': 'application/json',
        'X-BFX-PAYLOAD': b'InRlc3RfcGFyYW1zIg==',
        'X-BFX-APIKEY': 'test_apiKey',
        'X-BFX-SIGNATURE': '060812e040090120d068ca10e3004196f10c8569c010ae44ea4542d22145eddfbd51d2c40c4c0bc534b02e5d86427b54'
    }